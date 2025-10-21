# 🤖 Akıllı Müşteri Destek Sistemi

> **Gemini 2.5 Flash ile Güçlendirilmiş Yapay Zeka Tabanlı Müşteri Destek Platformu**

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/langchain-latest-green.svg)](https://langchain.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📋 İçindekiler

- [Genel Bakış](#-genel-bakış)
- [Özellikler](#-özellikler)
- [Mimari](#-mimari)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Proje Yapısı](#-proje-yapısı)
- [API Anahtarı](#-api-anahtarı)
- [Katkıda Bulunma](#-katkıda-bulunma)
- [Lisans](#-lisans)

## 🎯 Genel Bakış

Bu proje, Google'ın **Gemini 2.5 Flash** modeli ve **LangChain** framework'ü kullanarak geliştirilmiş, akıllı bir müşteri destek sistemidir. Sistem, müşteri mesajlarını analiz eder, otomatik yanıtlar üretir, kalite kontrolü yapar ve destek biletleri oluşturur.

### 🌟 Temel Yetenekler

- 🧠 **Akıllı Mesaj Analizi**: Kategori, aciliyet ve duygu analizi
- 💬 **Otomatik Yanıt Üretimi**: Bağlama duyarlı, empatik yanıtlar
- ✅ **Kalite Kontrolü**: Yanıtların profesyonellik, empati, çözüm ve netlik skorları
- 🎫 **Ticket Yönetimi**: Otomatik destek bileti oluşturma
- 📚 **Bilgi Tabanı**: Hazır çözümler ve makale arama
- 🧠 **Memory Sistemi**: Konuşma geçmişi ve müşteri profili takibi
- 📊 **Analytics Dashboard**: Gerçek zamanlı istatistikler ve metrikler

## ✨ Özellikler

### 🔍 Analiz Motoru

- **Kategori Tespiti**: Teknik, Billing, Genel
- **Aciliyet Seviyesi**: Düşük, Orta, Yüksek
- **Duygu Analizi**: Olumlu, Nötr, Olumsuz
- **Anahtar Kelime Çıkarımı**: Otomatik kelime etiketleme

### 💡 Akıllı Yanıt Sistemi

- Müşteri geçmişine göre kişiselleştirilmiş yanıtlar
- Bilgi tabanı entegrasyonu
- Çözüm odaklı yaklaşım
- Profesyonel ve empatik ton

### 📈 Kalite Değerlendirmesi

Her yanıt 4 kriterde değerlendirilir:

1. **Profesyonellik** (1-10): İş dili kalitesi
2. **Empati** (1-10): Müşteri anlayışı
3. **Çözüm** (1-10): Problem çözme yeteneği
4. **Netlik** (1-10): Açıklık ve anlaşılırlık

### 🗄️ Veri Yönetimi

- **Hibrit Memory**: Buffer + Window memory sistemi
- **Müşteri Profilleri**: Etkileşim geçmişi ve tercihler
- **Ticket Sistemi**: Otomatik bilet oluşturma ve takip
- **Bilgi Tabanı**: Kategorize edilmiş çözüm makaleleri

## 🏗️ Mimari

```
┌─────────────────────────────────────────────────────────┐
│                    Streamlit UI                         │
│                  (Web Arayüzü)                          │
└─────────────────┬───────────────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────────────┐
│            SmartCustomerSupportSystem                   │
│                  (Ana Orkestratör)                      │
└─────────────────┬───────────────────────────────────────┘
                  │
        ┌─────────┼─────────┐
        │         │         │
┌───────▼──┐ ┌───▼────┐ ┌──▼──────┐
│ Chains   │ │ Tools  │ │ Memory  │
│          │ │        │ │         │
│ Analysis │ │ Ticket │ │ Hybrid  │
│ Response │ │ KB     │ │ Customer│
│ Quality  │ │ Customer│ │        │
└──────────┘ └────────┘ └─────────┘
        │         │         │
        └─────────┼─────────┘
                  │
         ┌────────▼────────┐
         │  Gemini 2.5 Flash│
         │   (LLM Model)   │
         └─────────────────┘
```

### 📦 Komponent Açıklaması

#### **Chains (Zincirler)**
- `analysis_chain.py`: Mesaj analizi
- `response_chain.py`: Yanıt üretimi
- `quality_chain.py`: Kalite değerlendirmesi

#### **Tools (Araçlar)**
- `ticket_tool.py`: Destek bileti yönetimi
- `knowledge_tool.py`: Bilgi tabanı arama
- `customer_tool.py`: Müşteri veritabanı erişimi

#### **Memory (Bellek)**
- `hybrid_memory.py`: Konuşma geçmişi
- `customer_memory.py`: Müşteri profilleri

## 🚀 Kurulum

### Gereksinimler

- Python 3.12 veya üzeri
- pip (Python paket yöneticisi)
- Google API Key (Gemini için)

### Adım 1: Projeyi Klonlayın

```bash
git clone https://github.com/kullanici-adi/akilli-musteri-destek.git
cd akilli-musteri-destek
```

### Adım 2: Virtual Environment Oluşturun

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Adım 3: Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

### Adım 4: Ortam Değişkenlerini Ayarlayın

`.env` dosyası oluşturun:

```bash
# .env dosyası
GOOGLE_API_KEY=your_google_api_key_here
GEMINI_MODEL=gemini-2.5-flash
DEBUG=True
LOG_LEVEL=INFO
```

## 💻 Kullanım

### Web Arayüzü (Önerilen)

```bash
streamlit run app.py
```

Tarayıcınızda `http://localhost:8501` adresine gidin.

### Komut Satırı

```bash
python main.py
```

### Python Kodu ile Kullanım

```python
from main import SmartCustomerSupportSystem

# Sistem başlat
system = SmartCustomerSupportSystem()

# Müşteri talebini işle
result = system.handle_customer_request(
    customer_id="CUS001",
    message="Uygulamam çöküyor, yardım!"
)

# Sonuçları kontrol et
print(f"Yanıt: {result['response']}")
print(f"Kalite: {result['quality']['genel_skor']}/10")
```

## 📁 Proje Yapısı

```
akilli-musteri-destek/
│
├── 📄 main.py                    # Ana program (CLI)
├── 📄 app.py                     # Streamlit web arayüzü
├── 📄 .env                       # Ortam değişkenleri
├── 📄 requirements.txt           # Python bağımlılıkları
├── 📄 README.md                  # Bu dosya
│
├── 📁 chains/                    # LangChain zincirleri
│   ├── __init__.py
│   ├── analysis_chain.py        # Mesaj analizi
│   ├── response_chain.py        # Yanıt üretimi
│   └── quality_chain.py         # Kalite kontrolü
│
├── 📁 tools/                     # LangChain araçları
│   ├── __init__.py
│   ├── ticket_tool.py           # Ticket yönetimi
│   ├── knowledge_tool.py        # Bilgi tabanı
│   └── customer_tool.py         # Müşteri DB
│
├── 📁 memory/                    # Bellek sistemleri
│   ├── __init__.py
│   ├── hybrid_memory.py         # Hibrit memory
│   └── customer_memory.py       # Müşteri profilleri
│
├── 📁 utils/                     # Yardımcı modüller
│   ├── __init__.py
│   └── model_factory.py         # LLM model factory
│
├── 📁 streaming/                 # Streaming handlers
│   ├── __init__.py
│   └── handlers.py              # Callback handlers
│
└── 📁 tests/                     # Test dosyaları
    ├── __init__.py
    └── test_integration.py      # Entegrasyon testleri
```

## 🔑 API Anahtarı

### Google AI Studio'dan API Key Alma

1. [Google AI Studio](https://makersuite.google.com/app/apikey) adresine gidin
2. Google hesabınızla giriş yapın
3. "Create API Key" butonuna tıklayın
4. Anahtarı kopyalayın ve `.env` dosyasına ekleyin

```bash
GOOGLE_API_KEY=AIzaSy...your_key_here
```

## 🧪 Testler

### Tüm Testleri Çalıştırma

```bash
python tests/test_integration.py
```

### Test Senaryoları

- ✅ Temel iş akışı testi
- ✅ Ticket oluşturma testi
- ✅ Bilgi tabanı arama testi
- ✅ Müşteri bilgisi getirme testi
- ✅ Memory sistemi testi
- ✅ Tüm senaryolar testi

## 📊 Özellik Detayları

### Desteklenen Kategoriler

| Kategori | Açıklama | Örnek |
|----------|----------|-------|
| 🔧 Teknik | Yazılım sorunları | "Uygulama çöküyor" |
| 💳 Billing | Faturalandırma | "Faturamda hata var" |
| 📋 Genel | Diğer talepler | "Yeni özellikler?" |

### Aciliyet Seviyeleri

| Seviye | Emoji | Yanıt Süresi |
|--------|-------|--------------|
| 🔴 Yüksek | Kritik | < 1 saat |
| 🟡 Orta | Normal | < 4 saat |
| 🟢 Düşük | Rutin | < 24 saat |

### Kalite Metrikleri

Her yanıt şu kriterlerde değerlendirilir:

- **Profesyonellik**: İş dili standardı (1-10)
- **Empati**: Müşteri anlayışı (1-10)
- **Çözüm**: Problem çözme (1-10)
- **Netlik**: İletişim kalitesi (1-10)
- **Genel Skor**: Ortalama puan (1-10)

## 🛠️ Geliştirme

### Yeni Özellik Ekleme

1. İlgili modülü (`chains/`, `tools/`, `memory/`) açın
2. Yeni sınıfınızı oluşturun
3. `__init__.py` dosyasına ekleyin
4. `main.py` içinde kullanın
5. Test yazın

### Örnek: Yeni Tool Ekleme

```python
# tools/new_tool.py
from langchain.tools import BaseTool

class NewTool(BaseTool):
    name: str = "new_tool"
    description: str = "Tool açıklaması"
    
    class Config:
        arbitrary_types_allowed = True
        extra = 'allow'
    
    def _run(self, query: str) -> str:
        # Tool mantığı
        return "Sonuç"
```