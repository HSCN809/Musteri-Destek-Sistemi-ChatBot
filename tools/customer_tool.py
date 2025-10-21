"""
Müşteri Veritabanı Tool'u - Pydantic v2 Final
"""
from langchain.tools import BaseTool
from typing import Dict, Any


class CustomerDatabaseTool(BaseTool):
    name: str = "customer_database"
    description: str = "Müşteri bilgilerini getirme"
    
    class Config:
        arbitrary_types_allowed = True
        extra = 'allow'
    
    def __init__(self, **data):
        super().__init__(**data)
        # Normal Python attribute olarak ekle
        object.__setattr__(self, 'customers', self._load_customers())
    
    def _load_customers(self) -> Dict[str, Dict[str, Any]]:
        """Örnek müşteri verileri"""
        return {
            "CUS001": {
                "name": "Ahmet Yılmaz",
                "email": "ahmet@email.com",
                "plan": "Premium",
                "join_date": "2023-01-15",
                "last_login": "2024-01-20",
                "status": "Aktif",
                "phone": "+90 555 123 4567",
                "location": "İstanbul"
            },
            "CUS002": {
                "name": "Ayşe Demir",
                "email": "ayse@email.com", 
                "plan": "Standart",
                "join_date": "2023-03-10",
                "last_login": "2024-01-19",
                "status": "Aktif",
                "phone": "+90 555 234 5678",
                "location": "Ankara"
            },
            "CUS003": {
                "name": "Mehmet Kaya",
                "email": "mehmet@email.com",
                "plan": "Premium",
                "join_date": "2023-11-05",
                "last_login": "2024-01-18",
                "status": "Aktif",
                "phone": "+90 555 345 6789",
                "location": "İzmir"
            },
            "CUS004": {
                "name": "Zeynep Şahin",
                "email": "zeynep@email.com",
                "plan": "Trial",
                "join_date": "2024-01-20",
                "last_login": "2024-01-20",
                "status": "Aktif",
                "phone": "+90 555 456 7890",
                "location": "Bursa"
            }
        }
    
    def _run(self, query: str) -> str:
        try:
            parts = query.split('|||')
            customer_id = parts[0].strip().upper()
            action = parts[1].strip().upper() if len(parts) > 1 and parts[1].strip() else "GET"
            
            if action == "GET":
                if customer_id in self.customers:
                    customer = self.customers[customer_id]
                    return f"""
👤 Müşteri Bilgileri - {customer_id}

📛 Ad Soyad: {customer['name']}
📧 E-posta: {customer['email']}
📞 Telefon: {customer.get('phone', 'Belirtilmemiş')}
🏠 Konum: {customer.get('location', 'Belirtilmemiş')}
💼 Plan: {customer['plan']}
📅 Üyelik Tarihi: {customer['join_date']}
🔐 Son Giriş: {customer['last_login']}
✅ Durum: {customer['status']}
"""
                else:
                    return f"❌ Müşteri bulunamadı: {customer_id}"
            
            elif action == "LIST":
                if not self.customers:
                    return "🔭 Henüz hiç müşteri kaydı yok."
                
                output = "📋 Müşteri Listesi:\n\n"
                for cust_id, customer in self.customers.items():
                    output += f"• {cust_id}: {customer['name']} - {customer['email']} ({customer['plan']})\n"
                
                return output
            
            else:
                return "❌ Bilinmeyen işlem. GET veya LIST kullanın."
                
        except Exception as e:
            return f"❌ Müşteri veritabanı hatası: {str(e)}"
    
    def _arun(self, query: str):
        raise NotImplementedError("Async desteklenmiyor")