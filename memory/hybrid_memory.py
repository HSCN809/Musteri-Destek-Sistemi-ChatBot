"""
Hibrit Memory Sistemi - Transformers'sız versiyon
"""
from langchain.memory import (
    ConversationBufferMemory,
    ConversationBufferWindowMemory
)
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Dict, List, Any


class HybridMemorySystem:
    """
    Hibrit memory sistemi - ConversationSummaryBufferMemory yerine 
    ConversationBufferMemory kullanıyor (transformers gerektirmez)
    """
    
    def __init__(self, llm: ChatGoogleGenerativeAI):
        self.llm = llm
        
        # Ana memory - Tüm konuşmayı tutar (transformers gerektirmez)
        self.main_memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        
        # Son 5 mesajı tam olarak tut
        self.recent_memory = ConversationBufferWindowMemory(
            k=5,
            memory_key="recent_messages",
            return_messages=True
        )
        
        # Müşteri metadata'sı
        self.metadata = {}
    
    def add_interaction(self, customer_input: str, ai_response: str, 
                       metadata: Dict = None):
        """
        Yeni etkileşim ekle
        
        Args:
            customer_input: Müşteri mesajı
            ai_response: AI yanıtı
            metadata: Ek bilgiler
        """
        # Her iki memory'ye de ekle
        self.main_memory.save_context(
            {"input": customer_input},
            {"output": ai_response}
        )
        
        self.recent_memory.save_context(
            {"input": customer_input},
            {"output": ai_response}
        )
        
        # Metadata'yı sakla
        if metadata:
            self.metadata.update(metadata)
    
    def get_context(self) -> str:
        """
        Mevcut konuşma bağlamını getir
        
        Returns:
            Konuşma özeti ve son mesajlar
        """
        try:
            # Ana konteksti al
            main_context = self.main_memory.load_memory_variables({})
            
            # Son mesajları al
            recent_context = self.recent_memory.load_memory_variables({})
            
            context_parts = []
            
            if main_context.get('chat_history'):
                # Mesaj sayısını kontrol et
                messages = main_context['chat_history']
                if isinstance(messages, list):
                    msg_count = len(messages)
                    context_parts.append(f"Konuşma Geçmişi: {msg_count} mesaj mevcut")
            
            if recent_context.get('recent_messages'):
                context_parts.append(f"Son Mesajlar: {recent_context['recent_messages']}")
            
            if self.metadata:
                context_parts.append(f"Müşteri Bilgileri: {self._format_metadata()}")
            
            return "\n\n".join(context_parts) if context_parts else "Yeni konuşma başlatıldı."
            
        except Exception as e:
            return f"Memory bağlamı alınamadı: {str(e)}"
    
    def get_recent_messages(self) -> List[str]:
        """Son mesajları liste olarak getir"""
        try:
            recent = self.recent_memory.load_memory_variables({})
            messages = recent.get('recent_messages', [])
            
            if isinstance(messages, str):
                return [msg.strip() for msg in messages.split('\n') if msg.strip()]
            elif isinstance(messages, list):
                return [str(msg) for msg in messages]
            return []
        except:
            return []
    
    def clear(self):
        """Tüm memory'yi temizle"""
        self.main_memory.clear()
        self.recent_memory.clear()
        self.metadata = {}
    
    def get_stats(self) -> Dict[str, Any]:
        """Memory istatistikleri"""
        recent_msg_count = len(self.get_recent_messages())
        return {
            "recent_messages": recent_msg_count,
            "metadata_count": len(self.metadata),
            "memory_type": "Hibrit (Buffer + Window) - No Transformers"
        }
    
    def _format_metadata(self) -> str:
        """Metadata'yı string formatına çevir"""
        if not self.metadata:
            return "Bilgi yok"
        
        parts = [f"{k}: {v}" for k, v in self.metadata.items()]
        return ", ".join(parts)