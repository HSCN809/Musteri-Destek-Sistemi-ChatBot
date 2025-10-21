"""
Müşteri yanıtı üreten Chain
"""
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Dict


class ResponseGenerationChain:
    """Müşteri için profesyonel yanıt üretir"""
    
    def __init__(self, llm: ChatGoogleGenerativeAI):
        self.llm = llm
        self.chain = self._create_chain()
    
    def _create_chain(self) -> LLMChain:
        """Yanıt üretim chain'ini oluştur"""
        prompt = PromptTemplate(
            input_variables=["customer_message", "analysis", "context"],
            template="""
            Profesyonel bir müşteri destek temsilcisi olarak yanıt oluştur.
            
            Müşteri Mesajı: {customer_message}
            
            Analiz Sonuçları: {analysis}
            
            Bağlam Bilgisi: {context}
            
            Lütfen şu kurallara uy:
            1. Nazik ve profesyonel ol
            2. Empatik bir dil kullan
            3. Çözüm odaklı ol
            4. Net ve anlaşılır yaz
            5. Müşterinin sorununu tam olarak ele al
            
            Yanıtını doğrudan yaz, giriş veya başlık ekleme.
            """
        )
        
        return LLMChain(llm=self.llm, prompt=prompt)
    
    def generate(self, customer_message: str, analysis: Dict[str, str], 
                 context: str = "") -> str:
        """
        Müşteri için yanıt üret
        
        Args:
            customer_message: Müşteri mesajı
            analysis: Analiz sonuçları
            context: Ek bağlam bilgisi
            
        Returns:
            Üretilen yanıt
        """
        try:
            # Analizi string formatına çevir
            analysis_str = self._format_analysis(analysis)
            
            response = self.chain.run(
                customer_message=customer_message,
                analysis=analysis_str,
                context=context if context else "Yeni müşteri talebi"
            )
            
            return response.strip()
            
        except Exception as e:
            return f"Üzgünüz, bir hata oluştu. Lütfen daha sonra tekrar deneyin. Hata: {str(e)}"
    
    def _format_analysis(self, analysis: Dict[str, str]) -> str:
        """Analiz sonuçlarını string formatına çevir"""
        parts = []
        for key, value in analysis.items():
            if key != 'hata':
                parts.append(f"{key}: {value}")
        return ", ".join(parts)