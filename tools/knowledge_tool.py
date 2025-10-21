"""
Bilgi Tabanı Tool'u - Pydantic v2 Final
"""
from langchain.tools import BaseTool
from typing import Dict, List, Any


class KnowledgeBaseTool(BaseTool):
    name: str = "knowledge_base"
    description: str = "Bilgi tabanında arama yapma"
    
    class Config:
        arbitrary_types_allowed = True
        extra = 'allow'
    
    def __init__(self, **data):
        super().__init__(**data)
        # Normal Python attribute olarak ekle
        object.__setattr__(self, 'articles', self._load_articles())
    
    def _load_articles(self) -> Dict[str, List[Dict[str, Any]]]:
        """Örnek makaleler yükle"""
        return {
            "teknik": [
                {
                    "title": "Uygulama Çökme Sorunu",
                    "content": "Uygulama çöktüğünde şu adımları izleyin: 1. Uygulamayı yeniden başlatın 2. Cihazı yeniden başlatın 3. Son sürüme güncelleyin",
                    "tags": ["çökme", "yeniden başlatma", "güncelleme"]
                },
                {
                    "title": "Şifre Sıfırlama",
                    "content": "Şifrenizi sıfırlamak için: 1. Giriş sayfasında 'Şifremi unuttum' tıklayın 2. E-posta adresinizi girin 3. Gelen link ile yeni şifre oluşturun",
                    "tags": ["şifre", "güvenlik", "giriş"]
                },
                {
                    "title": "İnternet Bağlantı Sorunu",
                    "content": "İnternet bağlantınızda sorun varsa: 1. Wi-Fi bağlantınızı kontrol edin 2. Modemi yeniden başlatın 3. Ağ ayarlarını sıfırlayın",
                    "tags": ["internet", "bağlantı", "wifi"]
                }
            ],
            "billing": [
                {
                    "title": "Fatura Sorgulama",
                    "content": "Faturanızı görüntülemek için: Hesabım > Faturalar bölümünden geçmiş faturalarınızı görebilirsiniz.",
                    "tags": ["fatura", "ödeme", "hesap"]
                },
                {
                    "title": "Ücret İtirazı",
                    "content": "Ücret itirazı için: destek@firma.com adresine fatura numarası ile başvurun.",
                    "tags": ["ücret", "itiraz", "geri ödeme"]
                },
                {
                    "title": "Ödeme Yöntemleri",
                    "content": "Kabul edilen ödeme yöntemleri: Kredi kartı, banka kartı, PayPal, havale. Ödemeler 3 iş günü içinde işlenir.",
                    "tags": ["ödeme", "kart", "paypal"]
                }
            ],
            "genel": [
                {
                    "title": "Yeni Özellikler",
                    "content": "Yeni özellikler her ay güncellenir. Gelişmeleri blog sayfamızdan takip edebilirsiniz.",
                    "tags": ["güncelleme", "özellik", "yenilik"]
                },
                {
                    "title": "İletişim Bilgileri",
                    "content": "Bize 7/24 ulaşabilirsiniz: Telefon: 0850 123 45 67, E-posta: destek@firma.com, Canlı destek: Uygulama içi",
                    "tags": ["iletişim", "destek", "telefon"]
                },
                {
                    "title": "Hesap Silme",
                    "content": "Hesabınızı silmek için: Ayarlar > Hesap > Hesabı Sil bölümünden işlemi gerçekleştirebilirsiniz.",
                    "tags": ["hesap", "silme", "iptal"]
                }
            ]
        }
    
    def _run(self, query: str) -> str:
        try:
            parts = query.split('|||')
            search_query = parts[0].strip().lower()
            category = parts[1].strip().lower() if len(parts) > 1 and parts[1].strip() else ""
            
            if not search_query:
                return "❌ Lütfen bir arama sorgusu girin."
            
            results = []
            
            # Kategoriye göre ara
            if category and category in self.articles:
                articles = self.articles[category]
                for article in articles:
                    if (search_query in article['title'].lower() or 
                        search_query in article['content'].lower() or
                        any(search_query in tag.lower() for tag in article['tags'])):
                        results.append(article)
            
            # Tüm kategorilerde ara
            else:
                for cat_articles in self.articles.values():
                    for article in cat_articles:
                        if (search_query in article['title'].lower() or 
                            search_query in article['content'].lower() or
                            any(search_query in tag.lower() for tag in article['tags'])):
                            results.append(article)
            
            if not results:
                category_info = f" ({category})" if category else ""
                return f"❌ '{search_query}'{category_info} için makale bulunamadı. Farklı kelimeler deneyin."
            
            # Sonuçları formatla
            output = f"🔍 '{search_query}' için {len(results)} makale bulundu:\n\n"
            
            for i, article in enumerate(results, 1):
                output += f"📖 {i}. {article['title']}\n"
                output += f"   📄 {article['content']}\n"
                output += f"   🏷️ Etiketler: {', '.join(article['tags'])}\n\n"
            
            return output
            
        except Exception as e:
            return f"❌ Bilgi tabanı arama hatası: {str(e)}"
    
    def _arun(self, query: str):
        raise NotImplementedError("Async desteklenmiyor")