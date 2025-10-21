"""
Integration Test Dosyası
"""
import sys
sys.path.append('..')

from main import SmartCustomerSupportSystem


def test_basic_flow():
    """Temel iş akışı testi"""
    print("=" * 60)
    print("TEST 1: Temel İş Akışı")
    print("=" * 60)
    
    system = SmartCustomerSupportSystem()
    
    result = system.handle_customer_request(
        customer_id="CUS001",
        message="Uygulamam çöküyor"
    )
    
    assert result["success"] == True, "İşlem başarısız"
    assert "response" in result, "Yanıt bulunamadı"
    assert "analysis" in result, "Analiz bulunamadı"
    
    print("✅ Test geçti!")
    print(f"Yanıt: {result['response'][:100]}...")
    

def test_ticket_creation():
    """Ticket oluşturma testi"""
    print("\n" + "=" * 60)
    print("TEST 2: Ticket Oluşturma")
    print("=" * 60)
    
    system = SmartCustomerSupportSystem()
    
    result = system.create_ticket("Test ticket detayı")
    
    assert "TKT" in result, "Ticket ID bulunamadı"
    
    print("✅ Test geçti!")
    print(result)


def test_knowledge_base():
    """Bilgi tabanı arama testi"""
    print("\n" + "=" * 60)
    print("TEST 3: Bilgi Tabanı Arama")
    print("=" * 60)
    
    system = SmartCustomerSupportSystem()
    
    result = system.search_knowledge_base("şifre", "teknik")
    
    assert "KB" in result, "Makale bulunamadı"
    
    print("✅ Test geçti!")
    print(result[:200] + "...")


def test_customer_info():
    """Müşteri bilgisi getirme testi"""
    print("\n" + "=" * 60)
    print("TEST 4: Müşteri Bilgileri")
    print("=" * 60)
    
    system = SmartCustomerSupportSystem()
    
    result = system.get_customer_info("CUS001")
    
    assert "Ahmet Yılmaz" in result, "Müşteri adı bulunamadı"
    
    print("✅ Test geçti!")
    print(result)


def test_memory_system():
    """Memory sistemi testi"""
    print("\n" + "=" * 60)
    print("TEST 5: Memory Sistemi")
    print("=" * 60)
    
    system = SmartCustomerSupportSystem()
    
    # İlk mesaj
    result1 = system.handle_customer_request(
        customer_id="CUS001",
        message="Merhaba, adım Ahmet"
    )
    
    # İkinci mesaj - önceki mesajı hatırlamalı
    result2 = system.handle_customer_request(
        customer_id="CUS001",
        message="Benim adımı hatırlıyor musun?"
    )
    
    stats = system.get_memory_stats()
    
    assert stats["recent_messages"] >= 2, "Memory çalışmıyor"
    
    print("✅ Test geçti!")
    print(f"Memory stats: {stats}")


def test_all_scenarios():
    """Tüm test senaryolarını çalıştır"""
    print("\n" + "=" * 60)
    print("TEST 6: Tüm Senaryolar")
    print("=" * 60)
    
    system = SmartCustomerSupportSystem()
    
    scenarios = [
        ("Teknik", "Uygulamam çöküyor"),
        ("Billing", "Faturamda hata var"),
        ("Genel", "Yeni özellikler ne zaman gelir"),
        ("Şikayet", "Bu hizmetten memnun değilim"),
        ("Takip", "Ticket durumu nedir")
    ]
    
    for name, message in scenarios:
        result = system.handle_customer_request(
            customer_id="CUS001",
            message=message
        )
        
        assert result["success"] == True, f"{name} senaryosu başarısız"
        print(f"✅ {name} senaryosu geçti")
    
    print("\n✅ Tüm senaryolar geçti!")


def run_all_tests():
    """Tüm testleri çalıştır"""
    print("\n" + "🧪" * 30)
    print("INTEGRATION TESTLER BAŞLIYOR")
    print("🧪" * 30 + "\n")
    
    try:
        test_basic_flow()
        test_ticket_creation()
        test_knowledge_base()
        test_customer_info()
        test_memory_system()
        test_all_scenarios()
        
        print("\n" + "=" * 60)
        print("🎉 TÜM TESTLER BAŞARIYLA GEÇTİ!")
        print("=" * 60)
        
    except AssertionError as e:
        print(f"\n❌ TEST HATASI: {e}")
    except Exception as e:
        print(f"\n❌ BEKLENMEYEN HATA: {e}")


if __name__ == "__main__":
    run_all_tests()