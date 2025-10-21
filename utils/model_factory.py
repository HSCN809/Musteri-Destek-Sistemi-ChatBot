"""
Model Factory - Sadece Gemini
"""
import os
from typing import Optional, Any
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


class ModelFactory:
    """
    LLM model factory - Sadece Gemini
    """
    
    @staticmethod
    def create_llm(
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        streaming: bool = False,
        callbacks: Optional[list] = None
    ) -> ChatGoogleGenerativeAI:
        """
        Gemini modeli oluştur
        
        Args:
            temperature: Model sıcaklığı
            max_tokens: Maksimum token sayısı
            streaming: Streaming aktif mi
            callbacks: Callback handler'lar
            
        Returns:
            ChatGoogleGenerativeAI instance
        """
        api_key = os.getenv("GOOGLE_API_KEY")
        
        if not api_key:
            raise ValueError(
                "Google API anahtarı bulunamadı! "
                ".env dosyasına GOOGLE_API_KEY ekleyin."
            )
        
        model_name = os.getenv("GEMINI_MODEL", "gemini-pro")
        
        return ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=api_key,
            temperature=temperature,
            max_output_tokens=max_tokens,
            streaming=streaming,
            callbacks=callbacks if callbacks else []
        )
    
    @staticmethod
    def get_model_info() -> dict:
        """Model bilgilerini getir"""
        return {
            "name": "Google Gemini Pro",
            "description": "Google'ın en yeni AI modeli",
            "strengths": ["Hızlı", "Çok dilli", "Ücretsiz tier"],
            "max_tokens": 30720,
            "context_window": 32768
        }


# Kolay kullanım için helper fonksiyon
def create_llm(**kwargs) -> ChatGoogleGenerativeAI:
    """
    Hızlı LLM oluşturma
    
    Örnek:
        llm = create_llm(temperature=0.5)
        llm = create_llm(streaming=True)
    """
    return ModelFactory.create_llm(**kwargs)