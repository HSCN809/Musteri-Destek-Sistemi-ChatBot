"""
Müşteri mesajlarını analiz eden Chain
"""
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Dict


class CustomerAnalysisChain:
    """Müşteri mesajını analiz eder"""
    
    def __init__(self, llm: ChatGoogleGenerativeAI):
        self.llm = llm
        self.chain = self._create_chain()
    
    def _create_chain(self) -> LLMChain:
        """Analiz chain'ini oluştur"""
        prompt = PromptTemplate(
            input_variables=["customer_message"],
            template="""
            Müşteri mesajını analiz et ve aşağıdaki bilgileri çıkar:
            
            Müşteri Mesajı: {customer_message}
            
            Lütfen şu formatta yanıt ver:
            Kategori: [teknik/billing/genel]
            Aciliyet: [düşük/orta/yüksek]
            Duygu: [olumlu/nötr/olumsuz]
            Anahtar Kelimeler: [virgülle ayrılmış]
            
            Yanıtını sadece bu format ile ver, başka açıklama ekleme.
            """
        )
        
        return LLMChain(llm=self.llm, prompt=prompt)
    
    def analyze(self, customer_message: str) -> Dict[str, str]:
        """
        Müşteri mesajını analiz et
        
        Args:
            customer_message: Müşteri mesajı
            
        Returns:
            Analiz sonuçları içeren dictionary
        """
        try:
            result = self.chain.run(customer_message=customer_message)
            
            # Sonucu parse et
            analysis = self._parse_result(result)
            return analysis
            
        except Exception as e:
            return {
                "kategori": "genel",
                "aciliyet": "orta",
                "duygu": "nötr",
                "anahtar_kelimeler": "",
                "hata": str(e)
            }
    
    def _parse_result(self, result: str) -> Dict[str, str]:
        """LLM çıktısını parse et"""
        lines = result.strip().split('\n')
        parsed = {}
        
        for line in lines:
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip().lower().replace(' ', '_')
                value = value.strip()
                parsed[key] = value
        
        return parsed