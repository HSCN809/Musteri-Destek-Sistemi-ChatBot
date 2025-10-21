"""
Yanıt kalitesini kontrol eden Chain
"""
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Dict


class QualityControlChain:
    """Üretilen yanıtın kalitesini değerlendirir"""
    
    def __init__(self, llm: ChatGoogleGenerativeAI):
        self.llm = llm
        self.chain = self._create_chain()
    
    def _create_chain(self) -> LLMChain:
        """Kalite kontrol chain'ini oluştur"""
        prompt = PromptTemplate(
            input_variables=["response", "original_message"],
            template="""
            Müşteri destek yanıtının kalitesini değerlendir.
            
            Orijinal Mesaj: {original_message}
            
            Üretilen Yanıt: {response}
            
            Değerlendirme Kriterleri:
            1. Profesyonellik (1-10)
            2. Empati (1-10)
            3. Çözüm odaklılık (1-10)
            4. Netlik (1-10)
            
            Lütfen şu formatta yanıt ver:
            Profesyonellik: [puan]
            Empati: [puan]
            Çözüm: [puan]
            Netlik: [puan]
            Genel Skor: [toplam/4]
            İyileştirme: [kısa öneri]
            
            Sadece bu formatı kullan.
            """
        )
        
        return LLMChain(llm=self.llm, prompt=prompt)
    
    def evaluate(self, response: str, original_message: str) -> Dict[str, any]:
        """
        Yanıt kalitesini değerlendir
        
        Args:
            response: Üretilen yanıt
            original_message: Orijinal müşteri mesajı
            
        Returns:
            Kalite değerlendirmesi
        """
        try:
            result = self.chain.run(
                response=response,
                original_message=original_message
            )
            
            evaluation = self._parse_evaluation(result)
            return evaluation
            
        except Exception as e:
            return {
                "profesyonellik": 0,
                "empati": 0,
                "çözüm": 0,
                "netlik": 0,
                "genel_skor": 0,
                "iyileştirme": f"Değerlendirme hatası: {str(e)}"
            }
    
    def _parse_evaluation(self, result: str) -> Dict[str, any]:
        """Değerlendirme sonucunu parse et"""
        lines = result.strip().split('\n')
        evaluation = {}
        
        for line in lines:
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip().lower().replace(' ', '_')
                value = value.strip()
                
                # Sayısal değerleri float'a çevir
                try:
                    if key != 'iyileştirme':
                        value = float(value.split('/')[0])
                except:
                    pass
                
                evaluation[key] = value
        
        return evaluation