"""
Streamlit Web Arayüzü - Akıllı Müşteri Destek Sistemi
Geliştirilmiş ve Optimize Edilmiş Versiyon
"""
import streamlit as st
from main import SmartCustomerSupportSystem
import time

# Sayfa konfigürasyonu
st.set_page_config(
    page_title="Akıllı Müşteri Destek - Gemini",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Geliştirilmiş CSS
st.markdown("""
<style>
    /* Ana başlık */
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        background: linear-gradient(120deg, #1f77b4, #4dabf7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 2rem;
        padding: 1rem;
    }
    
    /* Sidebar iyileştirme */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        padding: 0.5rem;
    }
    
    /* Metrik kartları */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 1rem;
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
    }
    
    /* Chat container */
    .chat-container {
        max-height: 600px;
        overflow-y: auto;
        padding: 1.5rem;
        background: #f8f9fa;
        border-radius: 1rem;
        margin-bottom: 1rem;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);
    }
    
    /* Butonlar */
    .stButton>button {
        border-radius: 0.5rem;
        font-weight: 500;
        transition: all 0.3s ease;
        border: none;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #f0f2f6;
        border-radius: 0.5rem;
        font-weight: 500;
    }
    
    /* Alert messages */
    .stAlert {
        border-radius: 0.5rem;
        border-left: 4px solid;
    }
    
    /* Chat mesajları */
    [data-testid="stChatMessage"] {
        background-color: #ffffff;
        border-radius: 1rem;
        padding: 1rem;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    /* Input alanları */
    .stTextInput>div>div>input,
    .stTextArea>div>div>textarea {
        border-radius: 0.5rem;
        border: 2px solid #e0e0e0;
        transition: border-color 0.3s ease;
    }
    
    .stTextInput>div>div>input:focus,
    .stTextArea>div>div>textarea:focus {
        border-color: #1f77b4;
        box-shadow: 0 0 0 2px rgba(31, 119, 180, 0.1);
    }
    
    /* Selectbox */
    .stSelectbox>div>div {
        border-radius: 0.5rem;
    }
    
    /* Metrikler için özel stil */
    [data-testid="stMetricValue"] {
        font-size: 1.5rem;
        font-weight: 700;
    }
    
    /* Progress bar */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
    }
    
    /* Scrollbar özelleştirme */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #888;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #555;
    }
    
    /* Responsive düzenleme */
    @media (max-width: 768px) {
        .main-header {
            font-size: 1.8rem;
        }
    }
</style>
""", unsafe_allow_html=True)


# Session state başlat
def init_session_state():
    """Session state'i başlat"""
    if 'system' not in st.session_state:
        st.session_state.system = None
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'current_customer' not in st.session_state:
        st.session_state.current_customer = "CUS001"
    if 'current_tab' not in st.session_state:
        st.session_state.current_tab = "💬 Sohbet"
    if 'system_ready' not in st.session_state:
        st.session_state.system_ready = False

init_session_state()


def initialize_system():
    """Sistemi başlat"""
    try:
        with st.spinner("🚀 Sistem başlatılıyor (Gemini 2.5 Flash)..."):
            st.session_state.system = SmartCustomerSupportSystem()
            st.session_state.system_ready = True
        return True
    except Exception as e:
        st.error(f"❌ Sistem başlatılamadı: {str(e)}")
        st.info("💡 Lütfen .env dosyasına GOOGLE_API_KEY ekleyin.")
        st.session_state.system_ready = False
        return False


def display_chat():
    """Geliştirilmiş sohbet arayüzü"""
    # Ana başlık
    st.markdown("""
    <div style="margin-bottom: 1.5rem;">
        <h2 style="color: #1f77b4; margin: 0;">💬 Müşteri Sohbeti</h2>
        <p style="color: #666; font-size: 0.9rem; margin-top: 0.3rem;">
            Müşteri: <strong>{}</strong>
        </p>
    </div>
    """.format(st.session_state.current_customer), unsafe_allow_html=True)
    
    # Müşteri bilgilerini göster
    if st.session_state.system:
        with st.expander("👤 Müşteri Profili", expanded=False):
            info = st.session_state.system.get_customer_info(st.session_state.current_customer)
            st.text(info)
    
    st.divider()
    
    # Chat geçmişi
    if st.session_state.chat_history:
        for i, chat in enumerate(st.session_state.chat_history):
            # Kullanıcı mesajı
            with st.chat_message("user", avatar="👤"):
                st.write(chat["message"])
                st.caption(f"Mesaj #{i+1}")
            
            # Asistan yanıtı
            with st.chat_message("assistant", avatar="🤖"):
                st.write(chat["response"])
                
                # Analiz detayları - Daha kompakt
                with st.expander("📊 Analiz Detayları"):
                    col1, col2, col3, col4 = st.columns(4)
                    
                    analysis = chat.get("analysis", {})
                    quality = chat.get("quality", {})
                    
                    with col1:
                        kategori = analysis.get("kategori", "N/A")
                        emoji = "🔧" if kategori == "teknik" else "💳" if kategori == "billing" else "📋"
                        st.metric("Kategori", f"{emoji} {kategori.capitalize()}")
                    
                    with col2:
                        aciliyet = analysis.get("aciliyet", "N/A")
                        color = "🔴" if aciliyet == "yüksek" else "🟡" if aciliyet == "orta" else "🟢"
                        st.metric("Aciliyet", f"{color} {aciliyet.capitalize()}")
                    
                    with col3:
                        duygu = analysis.get("duygu", "N/A")
                        emoji = "😊" if duygu == "olumlu" else "😐" if duygu == "nötr" else "😟"
                        st.metric("Duygu", f"{emoji} {duygu.capitalize()}")
                    
                    with col4:
                        skor = quality.get("genel_skor", 0)
                        emoji = "⭐" if skor >= 8 else "👍" if skor >= 6 else "👎"
                        st.metric("Kalite", f"{emoji} {skor}/10")
                    
                    # İyileştirme önerisi varsa göster
                    if quality.get("iyileştirme"):
                        st.info(f"💡 **İyileştirme:** {quality.get('iyileştirme')}")
    else:
        st.info("💬 Henüz sohbet yok. İlk mesajınızı yazın!")
        
        # Örnek sorular
        st.subheader("💡 Örnek Sorular:")
        example_questions = [
            "Uygulamam çöküyor, nasıl çözebilirim?",
            "Faturamda hata var",
            "Şifremi nasıl sıfırlayabilirim?",
            "Yeni özellikler ne zaman gelecek?"
        ]
        
        cols = st.columns(2)
        for idx, question in enumerate(example_questions):
            with cols[idx % 2]:
                if st.button(f"📝 {question}", key=f"example_{idx}", use_container_width=True):
                    st.session_state.example_clicked = question
                    st.rerun()


def display_dashboard():
    """Geliştirilmiş dashboard"""
    # Başlık
    st.markdown("""
    <div style="margin-bottom: 1.5rem;">
        <h2 style="color: #1f77b4; margin: 0;">📊 Performans Dashboard</h2>
        <p style="color: #666; font-size: 0.9rem; margin-top: 0.3rem;">
            Gerçek zamanlı sistem metrikleri ve analizler
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.chat_history:
        # Üst metrikler
        col1, col2, col3, col4 = st.columns(4)
        
        total_chats = len(st.session_state.chat_history)
        avg_quality = sum(chat.get("quality", {}).get("genel_skor", 0) for chat in st.session_state.chat_history) / total_chats
        high_urgency = sum(1 for chat in st.session_state.chat_history if chat.get("analysis", {}).get("aciliyet") == "yüksek")
        categories = [chat.get("analysis", {}).get("kategori", "genel") for chat in st.session_state.chat_history]
        tech_issues = categories.count("teknik")
        
        with col1:
            st.metric(
                "📨 Toplam Sohbet",
                total_chats,
                delta=f"+{total_chats} yeni" if total_chats > 0 else None
            )
        
        with col2:
            st.metric(
                "⭐ Ortalama Kalite",
                f"{avg_quality:.1f}/10",
                delta=f"{avg_quality - 7:.1f}" if avg_quality >= 7 else f"{avg_quality - 7:.1f}",
                delta_color="normal" if avg_quality >= 7 else "inverse"
            )
        
        with col3:
            st.metric(
                "🚨 Yüksek Aciliyet",
                high_urgency,
                delta="Kritik" if high_urgency > 0 else "Normal",
                delta_color="inverse" if high_urgency > 0 else "normal"
            )
        
        with col4:
            st.metric(
                "🔧 Teknik Sorunlar",
                tech_issues,
                delta=f"{(tech_issues/total_chats)*100:.0f}% oran"
            )
        
        st.divider()
        
        # Son yanıt kalitesi detayları
        if st.session_state.chat_history:
            st.subheader("📈 Son Yanıt Kalite Analizi")
            latest = st.session_state.chat_history[-1]["quality"]
            
            if latest:
                col1, col2, col3, col4 = st.columns(4)
                
                metrics = [
                    ("Profesyonellik", latest.get('profesyonellik', 0), "💼"),
                    ("Empati", latest.get('empati', 0), "❤️"),
                    ("Çözüm", latest.get('çözüm', 0), "✅"),
                    ("Netlik", latest.get('netlik', 0), "💡")
                ]
                
                for col, (label, value, emoji) in zip([col1, col2, col3, col4], metrics):
                    with col:
                        st.metric(
                            f"{emoji} {label}",
                            f"{value}/10",
                            delta="İyi" if value >= 7 else "Geliştirilmeli",
                            delta_color="normal" if value >= 7 else "inverse"
                        )
                
                if latest.get('iyileştirme'):
                    st.info(f"💡 **İyileştirme Önerisi:** {latest.get('iyileştirme')}")
        
        st.divider()
        
        # Kategori ve aciliyet dağılımı
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Kategori Dağılımı")
            categories_dict = {}
            for chat in st.session_state.chat_history:
                cat = chat.get("analysis", {}).get("kategori", "Bilinmeyen")
                categories_dict[cat] = categories_dict.get(cat, 0) + 1
            
            for cat, count in categories_dict.items():
                emoji = "🔧" if cat == "teknik" else "💳" if cat == "billing" else "📋"
                percentage = (count / total_chats) * 100
                st.write(f"{emoji} **{cat.capitalize()}:** {count} ({percentage:.1f}%)")
                st.progress(percentage / 100)
        
        with col2:
            st.subheader("🚦 Aciliyet Dağılımı")
            urgencies = {}
            for chat in st.session_state.chat_history:
                urg = chat.get("analysis", {}).get("aciliyet", "Bilinmeyen")
                urgencies[urg] = urgencies.get(urg, 0) + 1
            
            for urg, count in urgencies.items():
                emoji = "🔴" if urg == "yüksek" else "🟡" if urg == "orta" else "🟢"
                percentage = (count / total_chats) * 100
                st.write(f"{emoji} **{urg.capitalize()}:** {count} ({percentage:.1f}%)")
                st.progress(percentage / 100)
        
        st.divider()
        
        # Memory istatistikleri
        st.subheader("🧠 Memory İstatistikleri")
        if st.session_state.system:
            stats = st.session_state.system.get_memory_stats()
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("💬 Son Mesajlar", stats.get('recent_messages', 0))
            with col2:
                st.metric("📝 Metadata", stats.get('metadata_count', 0))
            with col3:
                st.metric("💾 Memory Tipi", "Hibrit", help=stats.get('memory_type', 'N/A'))
    
    else:
        # Boş state için öneri kartları
        st.info("💬 Henüz sohbet yok. İlk mesajınızı yazarak başlayın!")
        
        st.subheader("🎯 Dashboard Özellikleri:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 📊 Metrikler
            - ✅ Toplam sohbet sayısı
            - ⭐ Yanıt kalite skoru
            - 🚨 Acil durum takibi
            - 🔧 Kategori analizi
            """)
        
        with col2:
            st.markdown("""
            ### 📈 Analizler
            - 💬 Gerçek zamanlı istatistikler
            - 📊 Kategori dağılımları
            - 🎯 Kalite değerlendirmesi
            - 🧠 Memory takibi
            """)


def display_test_scenarios():
    """Geliştirilmiş test senaryoları"""
    # Başlık
    st.markdown("""
    <div style="margin-bottom: 1.5rem;">
        <h2 style="color: #1f77b4; margin: 0;">🧪 Test Laboratuvarı</h2>
        <p style="color: #666; font-size: 0.9rem; margin-top: 0.3rem;">
            Hazır senaryolar ile sistemi test edin
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 Sistemi test etmek için hazır senaryoları kullanın veya özel senaryo oluşturun.")
    
    # Hızlı test butonu
    col1, col2 = st.columns([3, 1])
    with col1:
        st.subheader("⚡ Hızlı Test")
    with col2:
        if st.button("🎯 Tümünü Çalıştır", type="primary"):
            st.session_state.run_all_tests = True
    
    test_scenarios = [
        {
            "title": "Teknik Sorun",
            "message": "Uygulamanız sürekli çöküyor, nasıl çözebilirim?",
            "customer": "CUS001",
            "icon": "🔧",
            "description": "Kritik teknik destek senaryosu"
        },
        {
            "title": "Fatura Sorusu",
            "message": "Bu ay faturamda garip bir ücret var, açıklayabilir misiniz?",
            "customer": "CUS002",
            "icon": "💳",
            "description": "Finansal sorun yönetimi"
        },
        {
            "title": "Genel Soru",
            "message": "Yeni özellikler ne zaman gelecek?",
            "customer": "CUS003",
            "icon": "❓",
            "description": "Genel bilgilendirme talebi"
        },
        {
            "title": "Şifre Sıfırlama",
            "message": "Şifremi unuttum, nasıl sıfırlayabilirim?",
            "customer": "CUS001",
            "icon": "🔐",
            "description": "Güvenlik ve erişim desteği"
        }
    ]
    
    # Grid layout için senaryolar
    cols = st.columns(2)
    
    for idx, scenario in enumerate(test_scenarios):
        with cols[idx % 2]:
            with st.container():
                st.markdown(f"""
                <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                            padding: 1rem; border-radius: 0.5rem; color: white; margin-bottom: 1rem;'>
                    <h3>{scenario['icon']} {scenario['title']}</h3>
                    <p style='font-size: 0.9rem; opacity: 0.9;'>{scenario['description']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                with st.expander("📋 Senaryo Detayları", expanded=False):
                    st.write(f"**👤 Müşteri:** {scenario['customer']}")
                    st.write(f"**💬 Mesaj:** {scenario['message']}")
                
                if st.button(f"▶️ Çalıştır", key=f"test_{scenario['title']}", use_container_width=True):
                    run_test_scenario(scenario)
    
    st.divider()
    
    # Özel test senaryosu
    st.subheader("🎯 Özel Test Senaryosu")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        custom_message = st.text_area(
            "Test mesajınızı yazın:",
            placeholder="Örnek: Hesabımı nasıl silebilirim?",
            key="custom_test_message",
            height=100
        )
    
    with col2:
        custom_customer = st.selectbox(
            "Müşteri Seç",
            ["CUS001", "CUS002", "CUS003", "CUS004"],
            key="custom_test_customer"
        )
        
        st.write("")
        st.write("")
        
        if st.button("🚀 Özel Testi Çalıştır", type="primary", use_container_width=True):
            if custom_message and st.session_state.system:
                run_test_scenario({
                    "title": "Özel Test",
                    "message": custom_message,
                    "customer": custom_customer,
                    "icon": "🎯"
                })
            else:
                st.warning("⚠️ Lütfen bir test mesajı yazın.")


def run_test_scenario(scenario):
    """Test senaryosunu çalıştır"""
    with st.spinner(f"⏳ Test senaryosu çalıştırılıyor: {scenario['title']}..."):
        result = st.session_state.system.handle_customer_request(
            scenario['customer'],
            scenario['message']
        )
    
    if result["success"]:
        st.success(f"✅ {scenario['title']} senaryosu başarılı!")
        
        # Sonuçları göster
        tabs = st.tabs(["📝 Yanıt", "📊 Analiz", "⭐ Kalite"])
        
        with tabs[0]:
            st.markdown(f"""
            <div style='background: #f8f9fa; padding: 1.5rem; border-radius: 0.5rem; 
                        border-left: 4px solid #28a745;'>
                {result["response"]}
            </div>
            """, unsafe_allow_html=True)
        
        with tabs[1]:
            col1, col2 = st.columns(2)
            with col1:
                st.json(result["analysis"])
            with col2:
                if result.get("ticket_id"):
                    st.info(f"🎫 **Oluşturulan Ticket:**\n\n{result['ticket_id']}")
        
        with tabs[2]:
            st.json(result["quality"])
        
        # Chat geçmişine ekle
        st.session_state.chat_history.append({
            "message": scenario['message'],
            "response": result["response"],
            "analysis": result["analysis"],
            "quality": result["quality"]
        })
        
        time.sleep(1)
        st.rerun()
    else:
        st.error(f"❌ Senaryo başarısız: {result.get('error', 'Bilinmeyen hata')}")


def sidebar_content():
    """Sidebar içeriği"""
    with st.sidebar:
        # BÜYÜK BAŞLIK
        st.markdown("""
        <div style="text-align: center; padding: 1.5rem 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 1rem; margin-bottom: 1.5rem;">
            <div style="font-size: 4rem; margin-bottom: 0.5rem;">🤖</div>
            <h1 style="font-size: 1.8rem; margin: 0; color: white; font-weight: 700;">AI Destek Asistanı</h1>
            <p style="color: rgba(255,255,255,0.9); font-size: 0.9rem; margin-top: 0.5rem;">Akıllı Müşteri Destek</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### ⚙️ Kontrol Paneli")
        
        st.divider()
        
        # Sistem durumu
        if st.session_state.system_ready:
            st.success("✅ Sistem Aktif")
            st.caption("🤖 Model: Gemini 2.5 Flash")
        else:
            st.warning("⚠️ Sistem Hazır Değil")
        
        st.divider()
        
        # Müşteri seçimi
        st.subheader("👤 Müşteri Seçimi")
        customer_options = ["CUS001", "CUS002", "CUS003", "CUS004", "➕ Yeni Müşteri"]
        customer_id = st.selectbox(
            "Müşteri ID",
            customer_options,
            index=0,
            label_visibility="collapsed"
        )
        
        if customer_id == "➕ Yeni Müşteri":
            customer_id = st.text_input("Yeni Müşteri ID:", "CUS005", key="new_customer")
        
        st.session_state.current_customer = customer_id
        
        st.divider()
        
        # Sistem kontrolleri
        st.subheader("🎛️ Sistem Kontrolleri")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🔄 Sistemi\nBaşlat", use_container_width=True):
                if initialize_system():
                    st.success("✅ Hazır!")
                    time.sleep(1)
                    st.rerun()
        
        with col2:
            if st.button("🗑️ Sohbeti\nTemizle", use_container_width=True):
                st.session_state.chat_history = []
                if st.session_state.system:
                    st.session_state.system.reset_session()
                st.success("✅ Temizlendi!")
                time.sleep(1)
                st.rerun()
        
        st.divider()
        
        # Navigasyon
        st.subheader("🧭 Navigasyon")
        
        nav_options = {
            "💬 Sohbet": "chat",
            "📊 Dashboard": "dashboard",
            "🧪 Test Senaryoları": "test"
        }
        
        for label, key in nav_options.items():
            if st.button(label, key=f"nav_{key}", use_container_width=True):
                st.session_state.current_tab = label
                st.rerun()
        
        st.divider()
        
        # Hızlı araçlar
        st.subheader("🛠️ Hızlı Araçlar")
        
        with st.expander("🔍 Bilgi Tabanı"):
            kb_query = st.text_input("Ara:", key="kb_search", placeholder="Şifre sıfırlama...")
            kb_category = st.selectbox("Kategori:", ["Tümü", "Teknik", "Billing", "Genel"], key="kb_cat")
            
            if st.button("🔍 Ara", key="kb_btn", use_container_width=True):
                if st.session_state.system and kb_query:
                    cat_map = {"Tümü": None, "Teknik": "teknik", "Billing": "billing", "Genel": "genel"}
                    result = st.session_state.system.search_knowledge_base(kb_query, cat_map.get(kb_category))
                    st.text_area("Sonuçlar:", result, height=200, key="kb_results")
        
        with st.expander("👤 Müşteri Bilgileri"):
            if st.button("📋 Bilgileri Göster", key="cust_info", use_container_width=True):
                if st.session_state.system:
                    info = st.session_state.system.get_customer_info(st.session_state.current_customer)
                    st.text_area("Müşteri:", info, height=200, key="cust_display")
        
        with st.expander("🎫 Ticket Oluştur"):
            ticket_detail = st.text_area("Detay:", key="ticket_detail", placeholder="Sorun açıklaması...")
            if st.button("✅ Oluştur", key="create_ticket", use_container_width=True):
                if st.session_state.system and ticket_detail:
                    result = st.session_state.system.create_ticket(ticket_detail)
                    st.success(result)
        
        st.divider()
        
        # İstatistikler
        if st.session_state.chat_history:
            st.subheader("📈 Hızlı İstatistikler")
            st.metric("💬 Toplam Sohbet", len(st.session_state.chat_history))
            
            avg_quality = sum(chat.get("quality", {}).get("genel_skor", 0) 
                            for chat in st.session_state.chat_history) / len(st.session_state.chat_history)
            st.metric("⭐ Ort. Kalite", f"{avg_quality:.1f}/10")


def main():
    """Ana uygulama"""
    
    # Başlık - Emoji ile
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0 1rem 0;">
        <div style="font-size: 4rem; margin-bottom: 0.5rem;">🤖</div>
        <h1 style="
            font-size: 2.5rem;
            font-weight: bold;
            background: linear-gradient(120deg, #1f77b4, #4dabf7);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin: 0;
        ">Akıllı Müşteri Destek Sistemi</h1>
        <p style="color: #666; font-size: 1rem; margin-top: 0.5rem;">
            ⚡ Powered by Gemini 2.5 Flash
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Sidebar
    sidebar_content()
    
    # Ana içerik
    if not st.session_state.system:
        # İlk yükleme
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.info("👋 Hoş geldiniz! Başlamak için sistemi başlatın.")
            if st.button("🚀 Sistemi Başlat", type="primary", use_container_width=True):
                if initialize_system():
                    st.success("✅ Sistem hazır!")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("❌ Sistem başlatılamadı.")
            st.stop()
    
    # Seçilen tab'a göre içerik göster
    if st.session_state.current_tab == "💬 Sohbet":
        display_chat()
    elif st.session_state.current_tab == "📊 Dashboard":
        display_dashboard()
    elif st.session_state.current_tab == "🧪 Test Senaryoları":
        display_test_scenarios()
    
    # Chat input - Her zaman en altta
    st.divider()
    
    # Örnek mesaj tıklandıysa
    if hasattr(st.session_state, 'example_clicked'):
        message = st.session_state.example_clicked
        del st.session_state.example_clicked
    else:
        message = st.chat_input("💬 Mesajınızı yazın...", key="main_chat_input")
    
    if message:
        # Kullanıcı mesajını göster
        with st.chat_message("user", avatar="👤"):
            st.write(message)
        
        # Asistan yanıtı
        with st.chat_message("assistant", avatar="🤖"):
            response_placeholder = st.empty()
            response_placeholder.markdown("⌨️ *Yanıt yazılıyor...*")
            
            try:
                start_time = time.time()
                
                # İşlemi gerçekleştir
                result = st.session_state.system.handle_customer_request(
                    customer_id=st.session_state.current_customer,
                    message=message
                )
                
                if result["success"]:
                    # Yanıtı göster
                    response_placeholder.markdown(result["response"])
                    
                    # İşlem süresi
                    duration = time.time() - start_time
                    
                    # Chat geçmişine ekle
                    st.session_state.chat_history.append({
                        "message": message,
                        "response": result["response"],
                        "analysis": result["analysis"],
                        "quality": result["quality"],
                        "duration": duration
                    })
                    
                    # Başarı mesajı
                    st.success(f"✅ Yanıt oluşturuldu! ({duration:.2f}s)")
                    
                    # Ticket oluşturulduysa bildir
                    if result.get("ticket_id"):
                        st.info(f"🎫 Ticket oluşturuldu: {result['ticket_id']}")
                    
                else:
                    response_placeholder.markdown("❌ Üzgünüm, bir hata oluştu. Lütfen tekrar deneyin.")
                    st.error(f"Hata: {result.get('error', 'Bilinmeyen hata')}")
                    
            except Exception as e:
                response_placeholder.markdown("❌ Sistem hatası oluştu.")
                st.error(f"Beklenmeyen hata: {str(e)}")
            
            # Sayfayı yenile
            time.sleep(0.5)
            st.rerun()


if __name__ == "__main__":
    main()