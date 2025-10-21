"""
Streaming Handler - Gemini için
"""
from langchain.callbacks.base import BaseCallbackHandler
from typing import Any, Dict, List
import time


class CustomerServiceStreamingHandler(BaseCallbackHandler):
    """Streaming callback handler"""
    
    def __init__(self, placeholder):
        self.placeholder = placeholder
        self.full_response = ""
        self.start_time = None
    
    def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any) -> None:
        """LLM başladığında"""
        self.full_response = ""
        self.start_time = time.time()
        self.placeholder.markdown("⌨️ *Yanıt yazılıyor...*")
    
    def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        """Yeni token geldiğinde"""
        self.full_response += token
        self.placeholder.markdown(self.full_response + "▌")
    
    def on_llm_end(self, response: Any, **kwargs: Any) -> None:
        """LLM bitirdiğinde"""
        self.placeholder.markdown(self.full_response)
        
        # İstatistikleri göster
        if self.start_time:
            duration = time.time() - self.start_time
            token_count = len(self.full_response.split())
            st.sidebar.info(f"⏱️ Yanıt süresi: {duration:.2f}s | 📊 Token sayısı: {token_count}")
    
    def on_llm_error(self, error: Exception, **kwargs: Any) -> None:
        """Hata oluştuğunda"""
        self.placeholder.markdown(f"❌ Hata: {str(error)}")