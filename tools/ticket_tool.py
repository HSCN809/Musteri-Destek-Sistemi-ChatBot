"""
Destek Bileti Yönetim Tool'u - Pydantic v2 Final
"""
from langchain.tools import BaseTool
from typing import Dict, Any
import uuid
import datetime


class TicketManagementTool(BaseTool):
    name: str = "ticket_management"
    description: str = "Destek bileti oluşturma ve yönetme"
    
    class Config:
        # Pydantic'e extra field'lara izin ver
        arbitrary_types_allowed = True
        extra = 'allow'
    
    def __init__(self, **data):
        super().__init__(**data)
        # Normal Python attribute olarak ekle (Pydantic'in dışında)
        object.__setattr__(self, 'tickets', {})
    
    def _run(self, query: str) -> str:
        try:
            parts = query.split('|||')
            action = parts[0].upper().strip()
            
            if action == "CREATE":
                description = parts[1] if len(parts) > 1 else "Genel talep"
                ticket_id = f"TKT-{str(uuid.uuid4())[:8].upper()}"
                
                # Ticket kaydı oluştur
                ticket_data = {
                    "id": ticket_id,
                    "description": description,
                    "status": "Açık",
                    "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "priority": "Yüksek" if any(word in description.lower() for word in ['acil', 'kritik', 'çöküyor', 'çalışmıyor']) else "Normal"
                }
                
                # Ticket'ı sakla
                self.tickets[ticket_id] = ticket_data
                
                return f"✅ Destek bileti oluşturuldu: {ticket_id}\n" \
                       f"📝 Açıklama: {description}\n" \
                       f"🚨 Öncelik: {ticket_data['priority']}\n" \
                       f"⏰ Tarih: {ticket_data['created_at']}"
            
            elif action == "STATUS":
                ticket_id = parts[1] if len(parts) > 1 else ""
                if not ticket_id:
                    return "❌ Lütfen bir ticket ID girin."
                
                if ticket_id in self.tickets:
                    ticket = self.tickets[ticket_id]
                    return f"ℹ️ Bilet {ticket_id}:\n" \
                           f"📝 Açıklama: {ticket['description']}\n" \
                           f"📊 Durum: {ticket['status']}\n" \
                           f"🚨 Öncelik: {ticket['priority']}\n" \
                           f"⏰ Oluşturulma: {ticket['created_at']}"
                else:
                    return f"❌ Ticket bulunamadı: {ticket_id}"
            
            elif action == "LIST":
                if not self.tickets:
                    return "🔭 Henüz hiç ticket oluşturulmamış."
                
                output = "📋 Açık Ticket'lar:\n\n"
                for ticket_id, ticket in self.tickets.items():
                    output += f"• {ticket_id}: {ticket['description'][:50]}... ({ticket['status']})\n"
                
                return output
            
            else:
                return "❌ Bilinmeyen işlem. CREATE, STATUS veya LIST kullanın."
                
        except Exception as e:
            return f"❌ Ticket işlemi hatası: {str(e)}"
    
    def _arun(self, query: str):
        raise NotImplementedError("Async desteklenmiyor")