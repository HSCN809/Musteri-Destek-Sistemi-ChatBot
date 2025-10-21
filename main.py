"""
Akıllı Müşteri Destek Sistemi - Ana Program
Tamamen Gemini Modeli ile
"""
import os
import sys
from dotenv import load_dotenv

# Modülleri içe aktar
from chains.analysis_chain import CustomerAnalysisChain
from chains.response_chain import ResponseGenerationChain
from chains.quality_chain import QualityControlChain
from memory.hybrid_memory import HybridMemorySystem
from memory.customer_memory import CustomerProfileMemory
from tools.ticket_tool import TicketManagementTool
from tools.knowledge_tool import KnowledgeBaseTool
from tools.customer_tool import CustomerDatabaseTool
from utils.model_factory import create_llm

# Ortam değişkenlerini yükle
load_dotenv()

class SmartCustomerSupportSystem:
    """Akıllı Müşteri Destek Sistemi - Ana Sınıf"""
    
    def __init__(self, streaming_handler=None):
        """Sistemi başlat"""
        print("🚀 Akıllı Müşteri Destek Sistemi başlatılıyor...")
        
        # LLM'i başlat
        callbacks = [streaming_handler] if streaming_handler else None
        self.llm = create_llm(
            temperature=0.7,
            streaming=streaming_handler is not None,
            callbacks=callbacks
        )
        
        # Komponentleri başlat
        self._initialize_components()
        
        print("✅ Sistem başarıyla başlatıldı! (Gemini Pro)\n")
    
    def _initialize_components(self):
        """Tüm sistem komponentlerini başlat"""
        # Tool'ları başlat
        self.ticket_tool = TicketManagementTool()
        self.knowledge_tool = KnowledgeBaseTool()
        self.customer_tool = CustomerDatabaseTool()
        
        # Chain'leri başlat
        self.analysis_chain = CustomerAnalysisChain(self.llm)
        self.response_chain = ResponseGenerationChain(self.llm)
        self.quality_chain = QualityControlChain(self.llm)
        
        # Memory sistemlerini başlat
        self.hybrid_memory = HybridMemorySystem(self.llm)
        self.customer_memory = CustomerProfileMemory()
        
        print("📦 Komponentler yüklendi:")
        print("   ✓ Analysis Chain")
        print("   ✓ Response Chain")
        print("   ✓ Quality Chain")
        print("   ✓ Hybrid Memory")
        print("   ✓ Customer Memory")
        print("   ✓ Ticket Tool")
        print("   ✓ Knowledge Tool")
        print("   ✓ Customer Database Tool")
    
    def handle_customer_request(self, customer_id: str, message: str) -> dict:
        """
        Müşteri talebini işle - Tam iş akışı
        
        Args:
            customer_id: Müşteri ID'si
            message: Müşteri mesajı
            
        Returns:
            dict: İşlem sonucu
        """
        print(f"\n{'='*60}")
        print(f"📞 Yeni Müşteri Talebi")
        print(f"{'='*60}")
        print(f"Müşteri ID: {customer_id}")
        print(f"Mesaj: {message}\n")
        
        result = {
            'customer_id': customer_id,
            'message': message,
            'analysis': None,
            'response': None,
            'quality': None,
            'ticket_id': None,
            'articles': None,
            'success': True
        }
        
        try:
            # 1. Müşteri bilgilerini al
            print("🔍 Müşteri bilgileri alınıyor...")
            customer_info = self.customer_tool._run(f"{customer_id}|||GET")
            print(f"   Müşteri bilgileri alındı\n")
            
            # 2. Müşteri mesajını analiz et
            print("🔍 Mesaj analizi yapılıyor...")
            analysis = self.analysis_chain.analyze(message)
            result['analysis'] = analysis
            print(f"   Kategori: {analysis.get('kategori', 'N/A')}")
            print(f"   Aciliyet: {analysis.get('aciliyet', 'N/A')}")
            print(f"   Duygu: {analysis.get('duygu', 'N/A')}\n")
            
            # 3. Bilgi tabanından ilgili makaleleri bul
            if analysis.get('kategori') != 'genel':
                print("📚 Bilgi tabanı sorgulanıyor...")
                category = analysis.get('kategori', '')
                articles = self.knowledge_tool._run(f"{message}|||{category}")
                result['articles'] = articles
                print(f"   Makaleler bulundu\n")
            
            # 4. Memory context'ini al
            context = self.hybrid_memory.get_context()
            
            # 5. Yanıt oluştur
            print("💭 Yanıt oluşturuluyor...")
            response = self.response_chain.generate(
                customer_message=message,
                analysis=analysis,
                context=context
            )
            result['response'] = response
            print(f"   Yanıt hazır!\n")
            
            # 6. Kalite kontrolü yap
            print("✅ Kalite kontrolü yapılıyor...")
            quality = self.quality_chain.evaluate(response, message)
            result['quality'] = quality
            print(f"   Kalite Skoru: {quality.get('genel_skor', 0)}/10")
            
            if quality.get('genel_skor', 0) < 7:
                print(f"   ⚠️ İyileştirme Önerileri: {quality.get('iyileştirme', 'Yok')}\n")
            else:
                print(f"   ✓ Kalite standartları karşılandı\n")
            
            # 7. Yüksek aciliyetse ticket oluştur
            if analysis.get('aciliyet') in ['yüksek', 'kritik']:
                print("🎟️ Destek bileti oluşturuluyor...")
                ticket_result = self.ticket_tool._run(f"CREATE|||{message}")
                result['ticket_id'] = ticket_result
                print(f"   {ticket_result}\n")
            
            # 8. Memory'ye kaydet
            self.hybrid_memory.add_interaction(message, response)
            self.customer_memory.update_interaction(
                customer_id, 
                analysis.get('kategori', 'genel'),
                analysis.get('duygu', 'nötr')
            )
            
            # Sonuçları göster
            print(f"{'='*60}")
            print(f"📝 SONUÇ ÖZETİ")
            print(f"{'='*60}")
            print(f"\n{response}\n")
            print(f"{'='*60}\n")
            
            return result
            
        except Exception as e:
            print(f"❌ Hata: {str(e)}")
            result['success'] = False
            result['error'] = str(e)
            return result
    
    def search_knowledge_base(self, query: str, category: str = None) -> str:
        """Bilgi tabanında arama yap"""
        search_query = f"{query}|||{category}" if category else f"{query}|||"
        return self.knowledge_tool._run(search_query)
    
    def create_ticket(self, details: str) -> str:
        """Yeni ticket oluştur"""
        return self.ticket_tool._run(f"CREATE|||{details}")
    
    def get_customer_info(self, customer_id: str) -> str:
        """Müşteri bilgilerini getir"""
        return self.customer_tool._run(f"{customer_id}|||GET")
    
    def get_memory_stats(self) -> dict:
        """Memory istatistiklerini getir"""
        return self.hybrid_memory.get_stats()
    
    def get_customer_statistics(self, customer_id: str) -> dict:
        """Müşteri istatistiklerini getir"""
        return self.customer_memory.get_statistics(customer_id)
    
    def reset_session(self):
        """Session'ı sıfırla"""
        self.hybrid_memory.clear()
        print("Session sıfırlandı!")


def main():
    """Ana fonksiyon"""
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║     AKILLI MÜŞTERİ DESTEK SİSTEMİ                       ║
    ║     Tamamen Google Gemini Pro ile                       ║
    ╚══════════════════════════════════════════════════════════╝
    """)
    
    try:
        # Sistemi başlat
        system = SmartCustomerSupportSystem()
        
        # Menü göster
        while True:
            print("\n" + "="*60)
            print("📋 ANA MENÜ")
            print("="*60)
            print("1. 🎯 Test Senaryolarını Çalıştır")
            print("2. 🔍 Bilgi Tabanında Ara")
            print("3. 🎟️ Ticket Oluştur")
            print("4. 👤 Müşteri Bilgilerini Gör")
            print("5. 📊 Sistem İstatistikleri")
            print("6. ❌ Çıkış")
            print("="*60)
            
            choice = input("\nSeçiminiz (1-6): ").strip()
            
            if choice == '1':
                run_test_scenarios(system)
            elif choice == '2':
                query = input("Arama sorgusu: ")
                category = input("Kategori (teknik/billing/genel - boş bırakabilirsiniz): ")
                result = system.search_knowledge_base(query, category if category else None)
                print(f"\n{result}\n")
            elif choice == '3':
                details = input("Ticket detayı: ")
                result = system.create_ticket(details)
                print(f"\n{result}\n")
            elif choice == '4':
                customer_id = input("Müşteri ID: ")
                result = system.get_customer_info(customer_id)
                print(f"\n{result}\n")
            elif choice == '5':
                stats = system.get_memory_stats()
                print(f"\n📊 Sistem İstatistikleri:")
                for key, value in stats.items():
                    print(f"   {key}: {value}")
                print()
            elif choice == '6':
                print("\n👋 Sistemden çıkılıyor... Güle güle!")
                break
            else:
                print("\n⚠️ Geçersiz seçim! Lütfen 1-6 arası bir değer girin.")
    
    except KeyboardInterrupt:
        print("\n\n⚠️ Program kullanıcı tarafından durduruldu.")
    except Exception as e:
        print(f"\n❌ Kritik hata: {str(e)}")
        sys.exit(1)


def run_test_scenarios(system):
    """Test senaryolarını çalıştır"""
    scenarios = [
        {
            'customer_id': 'CUS001',
            'message': 'Uygulamanız sürekli çöküyor, nasıl çözebilirim?'
        },
        {
            'customer_id': 'CUS002',
            'message': 'Bu ay faturamda garip bir ücret var, açıklayabilir misiniz?'
        },
        {
            'customer_id': 'CUS003',
            'message': 'Yeni özellikler ne zaman gelecek?'
        },
        {
            'customer_id': 'CUS001', 
            'message': 'Şifremi unuttum, nasıl sıfırlayabilirim?'
        }
    ]
    
    print("\n🧪 Test Senaryoları Başlıyor...\n")
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"\n{'#'*60}")
        print(f"# Senaryo {i}/{len(scenarios)}")
        print(f"{'#'*60}\n")
        
        result = system.handle_customer_request(
            scenario['customer_id'],
            scenario['message']
        )
        
        if result['success']:
            print(f"✅ Senaryo {i} başarılı!")
        else:
            print(f"❌ Senaryo {i} başarısız: {result.get('error', 'Bilinmeyen hata')}")
        
        if i < len(scenarios):
            input("\n⏸️ Devam etmek için Enter'a basın...")


if __name__ == "__main__":
    main()
