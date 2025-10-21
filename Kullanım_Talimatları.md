# 📖 Akıllı Müşteri Destek Sistemi - Kullanım Talimatı

## 🎯 Başlangıç Kılavuzu

Bu dokümanda, Akıllı Müşteri Destek Sistemi'ni nasıl kullanacağınızı adım adım öğreneceksiniz.

---

## 📋 İçindekiler

1. [İlk Kurulum](#1-ilk-kurulum)
2. [Web Arayüzü Kullanımı](#2-web-arayüzü-kullanımı)
3. [Komut Satırı Kullanımı](#3-komut-satırı-kullanımı)
4. [Özellik Kullanımları](#4-özellik-kullanımları)
5. [Sık Sorulan Sorular](#5-sık-sorulan-sorular)
6. [Sorun Giderme](#6-sorun-giderme)

---

## 1. İlk Kurulum

### 📦 Adım 1.1: Gerekli Yazılımları İndirin

**Python Kurulumu** (Henüz yoksa)

1. [Python.org](https://www.python.org/downloads/) adresine gidin
2. Python 3.12 veya üzeri sürümü indirin
3. Kurulum sırasında "Add Python to PATH" seçeneğini işaretleyin

**Kurulumu Kontrol Edin:**
```bash
python --version
# Çıktı: Python 3.12.x olmalı
```

### 🔑 Adım 1.2: Google API Key Alın

1. [Google AI Studio](https://makersuite.google.com/app/apikey) adresine gidin
2. Google hesabınızla giriş yapın
3. **"Create API Key"** butonuna tıklayın
4. Oluşturulan anahtarı kopyalayın

### ⚙️ Adım 1.3: Projeyi Kurun

**Terminal/Komut İstemi'ni açın ve şu komutları çalıştırın:**

```bash
# 1. Proje klasörüne gidin
cd akilli-musteri-destek

# 2. Virtual environment oluşturun
python -m venv venv

# 3. Virtual environment'ı aktifleştirin
# Windows için:
venv\Scripts\activate

# Mac/Linux için:
source venv/bin/activate

# 4. Bağımlılıkları yükleyin
pip install -r requirements.txt
```

### 🔐 Adım 1.4: API Anahtarını Ayarlayın

`.env` dosyasını düzenleyin veya oluşturun:

```bash
# .env
GOOGLE_API_KEY=AIzaSy...buraya_kendi_api_keyinizi_yapistirin
GEMINI_MODEL=gemini-2.5-flash
DEBUG=True
```

**✅ Kurulum Tamamlandı!** Artık sistemi kullanmaya başlayabilirsiniz.

---

## 2. Web Arayüzü Kullanımı

### 🚀 Adım 2.1: Sistemi Başlatın

```bash
streamlit run app.py
```

Tarayıcınızda otomatik olarak `http://localhost:8501` adresi açılacak.

### 🎨 Adım 2.2: Arayüz Tanıtımı

#### **Ana Bileşenler:**

```
┌─────────────────────────────────────────────────────┐
│  🤖 Akıllı Müşteri Destek Sistemi                  │
│     Powered by Gemini 2.5 Flash                    │
└─────────────────────────────────────────────────────┘
┌────────────┬────────────────────────────────────────┐
│            │  💬 Sohbet Alanı                       │
│  Sidebar   │  - Müşteri mesajları                   │
│  (Sol)     │  - AI yanıtları                        │
│            │  - Analiz detayları                    │
│  - Müşteri │                                         │
│  - Ayarlar │  📝 Mesaj Giriş Alanı                  │
│  - Araçlar │  [Mesajınızı buraya yazın...]          │
└────────────┴────────────────────────────────────────┘
```

### 💬 Adım 2.3: İlk Sohbeti Başlatın

1. **Müşteri Seçin**
   - Sol sidebar'da "👤 Müşteri Seçimi" bölümünden bir müşteri seçin
   - Varsayılan: CUS001

2. **Mesaj Yazın**
   - Sayfanın en altındaki mesaj kutusuna sorunuzu yazın
   - Örnek: "Uygulamam çöküyor, yardım edebilir misiniz?"

3. **Gönder**
   - Enter'a basın veya gönder butonuna tıklayın
   - AI yanıtını bekleyin (2-5 saniye)

4. **Sonuçları İnceleyin**
   - AI'ın verdiği yanıtı okuyun
   - "📊 Analiz Detayları" bölümünü açarak:
     - Mesaj kategorisini
     - Aciliyet seviyesini
     - Duygu analizini
     - Kalite skorunu görebilirsiniz

### 📊 Adım 2.4: Dashboard'u Kullanın

1. Sol sidebar'dan **"📊 Dashboard"** sekmesine tıklayın

2. **Görebileceğiniz Metrikler:**
   - 📨 Toplam sohbet sayısı
   - ⭐ Ortalama kalite skoru
   - 🚨 Yüksek aciliyet sayısı
   - 🔧 Teknik sorun oranı

3. **Grafikler:**
   - 📊 Kategori dağılımı (pasta grafik benzeri)
   - 🚦 Aciliyet dağılımı (renk kodlu)
   - 🧠 Memory istatistikleri

### 🧪 Adım 2.5: Test Senaryolarını Çalıştırın

1. Sol sidebar'dan **"🧪 Test Senaryoları"** sekmesine tıklayın

2. **Hazır Senaryolar:**
   - 🔧 Teknik Sorun
   - 💳 Fatura Sorusu
   - ❓ Genel Soru
   - 🔐 Şifre Sıfırlama

3. **Senaryo Çalıştırma:**
   - İstediğiniz senaryonun üzerine tıklayın
   - "▶️ Çalıştır" butonuna basın
   - Sonuçları 3 sekmede görüntüleyin:
     - 📝 Yanıt
     - 📊 Analiz
     - ⭐ Kalite

4. **Özel Test:**
   - Kendi mesajınızı yazın
   - Müşteri seçin
   - "🚀 Özel Testi Çalıştır" butonuna tıklayın

---

## 3. Komut Satırı Kullanımı

### 🖥️ Adım 3.1: Temel Kullanım

```bash
python main.py
```

### 📋 Adım 3.2: Ana Menü

Sistem başladığında şu menüyü göreceksiniz:

```
============================================================
📋 ANA MENÜ
============================================================
1. 🎯 Test Senaryolarını Çalıştır
2. 🔍 Bilgi Tabanında Ara
3. 🎟️ Ticket Oluştur
4. 👤 Müşteri Bilgilerini Gör
5. 📊 Sistem İstatistikleri
6. ❌ Çıkış
============================================================
```

### 🎯 Adım 3.3: Menü Seçenekleri

#### **1️⃣ Test Senaryolarını Çalıştır**

Otomatik olarak 4 test senaryosu çalışır:
- Teknik sorun
- Fatura sorgusu
- Genel soru
- Şifre sıfırlama

**Kullanım:**
```
Seçiminiz: 1
[Enter'a basın]
```

#### **2️⃣ Bilgi Tabanında Ara**

Çözüm makalelerinde arama yapın.

**Kullanım:**
```
Seçiminiz: 2
Arama sorgusu: şifre
Kategori (teknik/billing/genel): teknik
```

**Sonuç:**
```
🔍 'şifre' için 1 makale bulundu:

📖 1. Şifre Sıfırlama
   📄 Şifrenizi sıfırlamak için: 1. Giriş sayfasında...
   🏷️ Etiketler: şifre, güvenlik, giriş
```

#### **3️⃣ Ticket Oluştur**

Yeni destek bileti oluşturun.

**Kullanım:**
```
Seçiminiz: 3
Ticket detayı: Uygulama sürekli donuyor
```

**Sonuç:**
```
✅ Destek bileti oluşturuldu: TKT-ABC12345
📝 Açıklama: Uygulama sürekli donuyor
🚨 Öncelik: Yüksek
⏰ Tarih: 2025-10-21 14:30:00
```

#### **4️⃣ Müşteri Bilgilerini Gör**

Müşteri profilini görüntüleyin.

**Kullanım:**
```
Seçiminiz: 4
Müşteri ID: CUS001
```

**Sonuç:**
```
👤 Müşteri Bilgileri - CUS001

📛 Ad Soyad: Ahmet Yılmaz
📧 E-posta: ahmet@email.com
📞 Telefon: +90 555 123 4567
🏠 Konum: İstanbul
💼 Plan: Premium
```

#### **5️⃣ Sistem İstatistikleri**

Memory ve performans bilgilerini gösterir.

**Kullanım:**
```
Seçiminiz: 5
```

---

## 4. Özellik Kullanımları

### 🔍 4.1 Mesaj Analizi

Sistem her mesajı otomatik olarak analiz eder:

#### **Kategori Tespiti**
```python
"Uygulama çöküyor" → 🔧 Teknik
"Fatura sorunum var" → 💳 Billing
"Yeni özellikler?" → 📋 Genel
```

#### **Aciliyet Tespiti**
```python
"Kritik", "Acil", "Çöküyor" → 🔴 Yüksek
"Sorun", "Hata" → 🟡 Orta
"Bilgi", "Soru" → 🟢 Düşük
```

#### **Duygu Analizi**
```python
"Teşekkürler", "Memnunum" → 😊 Olumlu
"Bilgi almak istiyorum" → 😐 Nötr
"Çok kötü", "Memnun değilim" → 😟 Olumsuz
```

### 💬 4.2 Otomatik Yanıt Üretimi

**Sistem yanıt üretirken:**
1. ✅ Müşteri geçmişini kontrol eder
2. ✅ Bilgi tabanından ilgili makaleleri çeker
3. ✅ Bağlama uygun yanıt üretir
4. ✅ Empati ve profesyonellik dengesi kurar

**Örnek İş Akışı:**
```
Müşteri: "Şifremi unuttum"
         ↓
Analiz: Kategori=Teknik, Aciliyet=Orta
         ↓
Bilgi Tabanı: "Şifre Sıfırlama" makalesi bulundu
         ↓
Yanıt: "Şifrenizi sıfırlamak için şu adımları izleyin..."
         ↓
Kalite: 9.2/10
```

### ✅ 4.3 Kalite Kontrolü

Her yanıt 4 kriterde değerlendirilir:

| Kriter | Açıklama | İyi Skor |
|--------|----------|----------|
| 💼 Profesyonellik | İş dili kullanımı | > 7 |
| ❤️ Empati | Müşteri anlayışı | > 7 |
| ✅ Çözüm | Problem çözme | > 7 |
| 💡 Netlik | Açık iletişim | > 7 |

**Düşük skor alındığında:**
```
⚠️ Kalite Skoru: 5.8/10
💡 İyileştirme: Daha empatik bir dil kullanın
```

### 🎫 4.4 Otomatik Ticket Oluşturma

**Ticket ne zaman oluşturulur?**
- Aciliyet: Yüksek veya Kritik
- Kategori: Teknik sorunlar
- Anahtar kelimeler: "çöküyor", "çalışmıyor", "acil"

**Ticket Bilgileri:**
```
TKT-ABC12345
├── Açıklama: Müşteri mesajı
├── Durum: Açık
├── Öncelik: Yüksek/Normal
├── Oluşturma: Tarih/Saat
└── Kategori: Otomatik atanır
```

### 📚 4.5 Bilgi Tabanı Kullanımı

**Mevcut Kategoriler:**

1. **🔧 Teknik**
   - Uygulama Çökme Sorunu
   - Şifre Sıfırlama
   - İnternet Bağlantı Sorunu

2. **💳 Billing**
   - Fatura Sorgulama
   - Ücret İtirazı
   - Ödeme Yöntemleri

3. **📋 Genel**
   - Yeni Özellikler
   - İletişim Bilgileri
   - Hesap Silme

**Arama Örnekleri:**
```python
# Tüm kategorilerde ara
search_knowledge_base("şifre")

# Belirli kategoride ara
search_knowledge_base("fatura", "billing")

# Birden fazla kelime
search_knowledge_base("uygulama çöküyor")
```

### 🧠 4.6 Memory Sistemi

**Hibrit Memory Yapısı:**

```
┌─────────────────────────────────────┐
│     ConversationBufferMemory        │
│  (Tüm konuşma geçmişi - tam)        │
└─────────────────────────────────────┘
             +
┌─────────────────────────────────────┐
│   ConversationBufferWindowMemory    │
│     (Son 5 mesaj - detaylı)         │
└─────────────────────────────────────┘
             =
┌─────────────────────────────────────┐
│        Hybrid Memory System         │
│   (Optimize edilmiş bağlam)         │
└─────────────────────────────────────┘
```

**Müşteri Profili Takibi:**
- Toplam etkileşim sayısı
- En çok kullanılan kategori
- Yaygın duygu durumu
- Son etkileşim tarihi
- Özel tercihler

---

## 5. Sık Sorulan Sorular

### ❓ Genel Sorular

**S1: Sistem kaç dilde çalışıyor?**
> **C:** Şu anda yalnızca Türkçe desteklenmektedir. Gemini modeli çok dilli olduğu için gelecekte diğer diller eklenebilir.

**S2: Maksimum mesaj uzunluğu nedir?**
> **C:** Gemini 2.5 Flash modeli yaklaşık 32.000 token (karakter) destekler. Pratik kullanımda 2000-3000 kelimelik mesajlar sorunsuz işlenir.

**S3: Yanıt süresi ne kadar?**
> **C:** Ortalama yanıt süresi 2-5 saniye arasındadır. Karmaşık sorgularda 8-10 saniyeye kadar çıkabilir.

**S4: API kullanımı ücretli mi?**
> **C:** Google Gemini API'nin ücretsiz kotası vardır. Günlük 60 istek/dakika limiti bulunur. Detaylar için [Google AI fiyatlandırma](https://ai.google.dev/pricing) sayfasına bakın.

**S5: Veriler güvende mi?**
> **C:** Evet! Tüm konuşmalar lokal olarak saklanır. Google API'ye yalnızca mesaj metni gönderilir, kişisel bilgiler saklanmaz.

### 🔧 Teknik Sorular

**S6: Hangi Python sürümü gerekli?**
> **C:** Python 3.12 veya üzeri. Python 3.11 de çalışabilir ancak test edilmemiştir.

**S7: Virtual environment kullanmak zorunlu mu?**
> **C:** Zorunlu değil ama şiddetle önerilir. Paket çakışmalarını önler ve projeyi izole eder.

**S8: Streamlit yüklenmiyor, ne yapmalıyım?**
> **C:** 
> ```bash
> pip install --upgrade pip
> pip install streamlit --force-reinstall
> ```

**S9: "Module not found" hatası alıyorum.**
> **C:** Virtual environment'ı aktif ettiğinizden emin olun:
> ```bash
> # Windows
> venv\Scripts\activate
> 
> # Mac/Linux
> source venv/bin/activate
> ```

**S10: API key hatası alıyorum.**
> **C:** `.env` dosyasının doğru konumda olduğundan ve API key'in doğru olduğundan emin olun:
> ```bash
> # .env dosyası proje ana dizininde olmalı
> # API key'de boşluk veya tırnak işareti olmamalı
> GOOGLE_API_KEY=AIzaSy...
> ```

---

## 6. Sorun Giderme

### 🚨 Yaygın Hatalar ve Çözümler

#### **Hata 1: "Google API anahtarı bulunamadı!"**

**Neden:** `.env` dosyası bulunamadı veya API key eksik.

**Çözüm:**
```bash
# 1. .env dosyasının var olduğunu kontrol edin
dir .env  # Windows
ls -la .env  # Mac/Linux

# 2. Dosya yoksa oluşturun
echo GOOGLE_API_KEY=your_key_here > .env

# 3. API key'i kontrol edin
cat .env
```

#### **Hata 2: "TicketManagementTool" object has no field**

**Neden:** Pydantic sürüm uyumsuzluğu.

**Çözüm:**
```bash
# tools/*.py dosyalarının güncel olduğundan emin olun
# En son artifact versiyonlarını kullanın
```

#### **Hata 3: "Could not import transformers"**

**Neden:** ConversationSummaryBufferMemory transformers paketi istiyor.

**Çözüm:**
```bash
# memory/hybrid_memory.py dosyasının güncellenmiş versiyonunu kullanın
# ConversationBufferMemory kullanmalı
```

#### **Hata 4: Streamlit açılmıyor**

**Neden:** Port zaten kullanımda veya firewall engeli.

**Çözüm:**
```bash
# Farklı port kullanın
streamlit run app.py --server.port 8502

# Veya tarayıcı olmadan
streamlit run app.py --server.headless true
```

#### **Hata 5: Yanıt alamıyorum / timeout**

**Neden:** İnternet bağlantısı veya API kotası.

**Çözüm:**
1. İnternet bağlantınızı kontrol edin
2. [Google AI Studio](https://makersuite.google.com/) hesabınızı kontrol edin
3. API key'in aktif olduğundan emin olun
4. Günlük kota sınırını kontrol edin

#### **Hata 6: Memory hatası / out of memory**

**Neden:** Çok fazla konuşma geçmişi.

**Çözüm:**
```python
# Sohbeti temizleyin
system.reset_session()

# Veya Web arayüzünde
"🗑️ Sohbeti Temizle" butonuna tıklayın
```

### 🔍 Debug Modu

**Detaylı hata mesajları için:**

```bash
# .env dosyasında DEBUG modunu aktif edin
DEBUG=True
LOG_LEVEL=DEBUG
```

**Log kayıtlarını görüntüleyin:**

```python
# main.py başında ekleyin
import logging
logging.basicConfig(level=logging.DEBUG)
```

### 📞 Yardım Alma

Sorun çözemezseniz:

1. **GitHub Issues:** Yeni bir issue açın
2. **Email:** support@example.com
3. **Dokümantasyon:** README.md dosyasını inceleyin

**Issue açarken ekleyin:**
- Python versiyonu (`python --version`)
- İşletim sistemi
- Hata mesajının tamamı
- `.env` dosyası (API key hariç)
- Çalıştırdığınız komut

---

## 7. İleri Seviye Kullanım

### 🎨 7.1 Özelleştirme

#### **Yeni Müşteri Kategorisi Ekleme**

```python
# chains/analysis_chain.py içinde
template="""
...
Lütfen şu formatta yanıt ver:
Kategori: [teknik/billing/genel/destek/satış]  # ← Yeni kategori
...
"""
```

#### **Kalite Kriterleri Değiştirme**

```python
# chains/quality_chain.py içinde
template="""
...
Değerlendirme Kriterleri:
1. Profesyonellik (1-10)
2. Empati (1-10)
3. Çözüm odaklılık (1-10)
4. Netlik (1-10)
5. Hız (1-10)  # ← Yeni kriter
...
"""
```

#### **Bilgi Tabanına Makale Ekleme**

```python
# tools/knowledge_tool.py içinde
def _load_articles(self):
    return {
        "teknik": [
            # Yeni makale ekleyin
            {
                "title": "VPN Kurulumu",
                "content": "VPN kurmak için...",
                "tags": ["vpn", "güvenlik", "bağlantı"]
            }
        ]
    }
```

### 🔧 7.2 Python API Kullanımı

**Basit Örnek:**
```python
from main import SmartCustomerSupportSystem

# Sistem başlat
system = SmartCustomerSupportSystem()

# Tek seferlik sorgu
result = system.handle_customer_request(
    customer_id="CUS001",
    message="Yardıma ihtiyacım var"
)

print(result['response'])
```

**Gelişmiş Örnek:**
```python
import json
from main import SmartCustomerSupportSystem

# Sistem başlat
system = SmartCustomerSupportSystem()

# Müşteri bilgisi al
customer_info = system.get_customer_info("CUS001")

# Bilgi tabanında ara
articles = system.search_knowledge_base("şifre", "teknik")

# Ticket oluştur
ticket = system.create_ticket("Kritik sorun!")

# Memory stats
stats = system.get_memory_stats()

# Sonuçları JSON'a kaydet
with open('results.json', 'w', encoding='utf-8') as f:
    json.dump({
        'customer': customer_info,
        'articles': articles,
        'ticket': ticket,
        'stats': stats
    }, f, ensure_ascii=False, indent=2)
```

**Batch İşlem:**
```python
# Çoklu müşteri için toplu işlem
messages = [
    ("CUS001", "Sorunum var"),
    ("CUS002", "Fatura hatası"),
    ("CUS003", "Bilgi istiyorum")
]

results = []
for customer_id, message in messages:
    result = system.handle_customer_request(customer_id, message)
    results.append(result)

# Sonuçları analiz et
avg_quality = sum(r['quality']['genel_skor'] for r in results) / len(results)
print(f"Ortalama kalite: {avg_quality:.2f}/10")
```

### 📊 7.3 Analitik ve Raporlama

**Günlük Rapor Oluşturma:**
```python
from datetime import datetime
import pandas as pd

# Tüm sohbet verilerini topla
chat_data = []
for chat in st.session_state.chat_history:
    chat_data.append({
        'timestamp': datetime.now(),
        'customer_id': st.session_state.current_customer,
        'category': chat['analysis']['kategori'],
        'urgency': chat['analysis']['aciliyet'],
        'sentiment': chat['analysis']['duygu'],
        'quality': chat['quality']['genel_skor']
    })

# DataFrame oluştur
df = pd.DataFrame(chat_data)

# Analiz
print(f"Toplam sohbet: {len(df)}")
print(f"Ortalama kalite: {df['quality'].mean():.2f}")
print("\nKategori dağılımı:")
print(df['category'].value_counts())

# Excel'e kaydet
df.to_excel('daily_report.xlsx', index=False)
```

### 🚀 7.4 Performans Optimizasyonu

**Yanıt Hızını Artırma:**
```python
# utils/model_factory.py içinde
def create_llm(temperature=0.7, max_tokens=None):
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",  # Flash model daha hızlı
        temperature=0.5,  # Düşük sıcaklık daha hızlı
        max_output_tokens=1024,  # Kısa yanıtlar
        streaming=True  # Streaming aktif
    )
```

**Memory Optimizasyonu:**
```python
# memory/hybrid_memory.py içinde
self.recent_memory = ConversationBufferWindowMemory(
    k=3,  # 5 yerine 3 mesaj (daha az memory)
    memory_key="recent_messages",
    return_messages=True
)
```

---

## 8. En İyi Pratikler

### ✅ Yapılması Gerekenler

1. **Virtual environment kullanın**
   - Paket çakışmalarını önler
   - Projeyi izole eder

2. **API key'i güvende tutun**
   - `.env` dosyasını `.gitignore`'a ekleyin
   - Asla kod içinde hardcode etmeyin

3. **Düzenli backup alın**
   - Chat geçmişini düzenli kaydedin
   - Önemli konfigürasyonları yedekleyin

4. **Test senaryolarını çalıştırın**
   - Her güncelleme sonrası test edin
   - Yeni özellikler için test yazın

5. **Log kayıtlarını takip edin**
   - Hataları erken tespit edin
   - Performans sorunlarını izleyin

### ❌ Yapılmaması Gerekenler

1. **API key'i paylaşmayın**
   - GitHub'a pushlamamayın
   - Ekran görüntülerine dahil etmeyin

2. **Çok fazla konuşma biriktirmeyin**
   - Memory dolmasına neden olur
   - Düzenli temizleyin

3. **Timeout olmadan beklemeyin**
   - API çağrılarında timeout ayarlayın
   - Hata yönetimi ekleyin

4. **Test edilmemiş kod kullanmayın**
   - Önce test ortamında deneyin
   - Production'da dikkatli olun

---

## 9. Güncellemeler ve Bakım

### 🔄 Güncellemeleri Kontrol Etme

```bash
# Proje güncellemelerini çekin
git pull origin main

# Bağımlılıkları güncelleyin
pip install -r requirements.txt --upgrade
```

### 🧹 Düzenli Bakım

**Haftalık:**
- Sohbet geçmişini temizleyin
- Log dosyalarını kontrol edin

**Aylık:**
- API kullanımını kontrol edin
- Performans metriklerini inceleyin
- Yeni Gemini modellerini kontrol edin

**Yıllık:**
- Python versiyonunu güncelleyin
- Tüm paketleri major update yapın

---

## 📝 Sonuç

Bu kullanım talimatı, Akıllı Müşteri Destek Sistemi'ni etkili bir şekilde kullanmanız için gereken tüm bilgileri içermektedir.


