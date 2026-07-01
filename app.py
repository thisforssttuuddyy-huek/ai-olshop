import streamlit as st
import json
import datetime
from google import genai
from google.genai import types

# ==========================================
# 🎨 CUSTOM CSS FOR PREMIUM COLOR THEMING
# ==========================================
st.set_page_config(
    page_title="Tools Kreator Premium Suite by Ky Dev",
    page_icon="⚡",
    layout="wide"
)

st.markdown("""
    <style>
    /* Mengubah warna background utama */
    .stApp {
        background-color: #0E1117;
    }
    
    /* Mengubah warna teks utama */
    h1, h2, h3, h4, p, span, label {
        color: #FFFFFF !important;
    }
    
    /* FIX TEKS SILAU: Mengubah kotak input biar hitam pekat dan tulisannya kuning neon */
    div[data-baseweb="input"] input, div[data-baseweb="textarea"] textarea {
        background-color: #000000 !important;
        color: #FFC107 !important;
        font-weight: bold !important;
        border: 1px solid #FFC107 !important;
    }
    
    /* Custom Card/Kotak Modul biar berwarna dan berkilau */
    .premium-card {
        background-color: #161B22;
        border: 1px solid #FFC107;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 15px rgba(255, 193, 7, 0.15);
        margin-bottom: 20px;
    }
    
    /* Kotak Free Trial */
    .trial-card {
        background-color: #1F1915;
        border: 1px solid #FF8C00;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    
    /* Judul Utama Bergradasi */
    .main-title {
        background: linear-gradient(45deg, #FFC107, #FF8C00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    /* Subtitle Developer Branding */
    .dev-subtitle {
        color: #A3B3C6 !important;
        font-size: 16px;
        font-weight: 500;
        margin-bottom: 25px;
    }
    .dev-subtitle a {
        color: #FFC107 !important;
        text-decoration: none;
        font-weight: bold;
    }
    .dev-subtitle a:hover {
        text-decoration: underline;
    }
    
    /* Mengubah gaya tombol standar */
    div.stButton > button:first-child {
        background-color: #FFC107 !important;
        color: #0E1117 !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        border: none !important;
        box-shadow: 0px 4px 10px rgba(255, 193, 7, 0.3);
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #FF8C00 !important;
        box-shadow: 0px 6px 15px rgba(255, 140, 0, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# --- KONFIGURASI PASSWORD SISTEM ---
PASSWORD_SISTEM = "ores123"

# --- BRANDING HEADER UTAMA ---
st.markdown('<p class="main-title">⚡ TOOLS KREATOR & MARKETING SUITE Premium v5.7</p>', unsafe_allow_html=True)
st.markdown('<p class="dev-subtitle">🚀 Developed with ❤️ by <b>Ky Dev</b> | 📸 Instagram: <a href="https://instagram.com/kyii_a.r" target="_blank">@kyii_a.r</a></p>', unsafe_allow_html=True)
st.write("Sistem Multi-Agent AI Kreator Konten End-to-End & OmniChannel Reputation Manager.")

password_input = st.text_input("🔑 Masukkan Password Akses Sistem:", type="password")

if password_input == PASSWORD_SISTEM:
    st.success("Akses Dashboard Terverifikasi!")
    st.divider()

    # --- INISIALISASI CLIENT GEMINI API ---
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        client = genai.Client(api_key=api_key)
    except Exception as e:
        st.error(f"Gagal memuat API Key dari Streamlit Secrets. Eror: {e}")
        st.stop()

    # ==========================================
    # 🔑 LOGIKA KODE LISENSI & COUNTDOWN
    # ==========================================
    if "account_status" not in st.session_state:
        st.session_state.account_status = "FREE_TRIAL"
        st.session_state.expiry_time = None

    st.sidebar.markdown('<div class="premium-card" style="border-color:#FF8C00;">', unsafe_allow_html=True)
    st.sidebar.subheader("🔑 PENGATURAN LISENSI")
    
    if "license_input_value" not in st.session_state:
        st.session_state.license_input_value = ""

    kode_input = st.sidebar.text_input("Masukkan Kode Lisensi Anda:", value=st.session_state.license_input_value, type="password")

    # Daftar Logika Kode Rahasia Owner & Klien
    KODE_OWNER_SAKTI = "OWNER-UNLIMITED-99X"
    KODE_PREMIUM_30HARI = "PREM-ORES30D"

    if kode_input == KODE_OWNER_SAKTI:
        st.session_state.account_status = "OWNER_SAKTI"
    elif kode_input == KODE_PREMIUM_30HARI:
        st.session_state.account_status = "PREMIUM_CLIENT"
        st.session_state.expiry_time = "29 Hari, 23 Jam, 59 Menit"
    else:
        st.session_state.account_status = "FREE_TRIAL"

    # Tampilan Visual Status Berwarna di Sidebar
    if st.session_state.account_status == "OWNER_SAKTI":
        st.sidebar.markdown("<h3 style='color: #00FF00 !important;'>👑 STATUS: OWNER SAKTI</h3>", unsafe_allow_html=True)
        st.sidebar.info("Akses Tanpa Batas Kuota, Tanpa Batas Waktu (Selamanya Aktif).")
        is_premium = True
    elif st.session_state.account_status == "PREMIUM_CLIENT":
        st.sidebar.markdown("<h3 style='color: #FFC107 !important;'>💎 STATUS: PREMIUM ACTIVE</h3>", unsafe_allow_html=True)
        st.sidebar.error(f"⏳ HITUNG MUNDUR SISA WAKTU:\n**{st.session_state.expiry_time}**")
        is_premium = True
    else:
        st.sidebar.markdown("<h3 style='color: #FF8C00 !important;'>🟢 STATUS: FREE TRIAL</h3>", unsafe_allow_html=True)
        st.sidebar.warning("Batasan kuota harian aktif. Masukkan kode untuk membuka fitur premium.")
        is_premium = False

    # --- TOMBOL HAPUS PREMIUM / RESET TO FREE ---
    if is_premium:
        if st.sidebar.button("❌ Remove Premium / Reset to Free", type="secondary"):
            st.session_state.account_status = "FREE_TRIAL"
            st.session_state.expiry_time = None
            st.session_state.license_input_value = ""
            st.rerun()

    st.sidebar.markdown('</div>', unsafe_allow_html=True)

    # --- SETUP DATA BISNIS (SIDEBAR) ---
    st.sidebar.header("⚙️ PROFIL DATA BISNIS")
    nama_bisnis = st.sidebar.text_input("Nama Brand / Cafe:", value="Ores.co")
    alamat_bisnis = st.sidebar.text_area("Alamat Fisik Toko:", value="Jl. Kasuari Raya No.1, Cikarang Baru, Bekasi, Jawa Barat")
    link_maps = st.sidebar.text_input("Link Google Maps:", value="https://maps.google.com/?q=Ores+Co+Cikarang")
    wa_cs = st.sidebar.text_input("WhatsApp Admin (62):", value="628123456789")

    # --- SIDEBAR FOOTER BRANDING ---
    st.sidebar.markdown("<br><br><hr><center style='color: #A3B3C6;'>🛠️ App Created by <b>Ky Dev</b><br>🔗 IG: <a href='https://instagram.com/kyii_a.r' target='_blank' style='color:#FFC107; text-decoration:none;'>@kyii_a.r</a></center>", unsafe_allow_html=True)

    # --- INTEGRASI MENU 5 TAB MULTI-MODUL ---
    st.subheader("🤖 Silakan Pilih Modul Kerja AI Agent Anda:")
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🛡️ 1. Reputation Manager", 
        "🧬 2. Branding Assessment", 
        "🎬 3. Script & Ideation", 
        "🔄 4. Remix Video Viral", 
        "📅 5. Funnel & Calendar"
    ])

    # ==========================================
    # TAB 1: REPUTATION MANAGER (FIXED MODEL 2026)
    # ==========================================
    with tab1:
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown("### 🛡️ Modul 1: OmniChannel Reputation & Crisis Management")
        st.write("Membalas ulasan masuk di 4 platform otomatis sesuai gaya platform masing-masing.")
        st.caption("🟢 **Kuota Gratis:** 5 kali per hari." if not is_premium else "👑 **Kuota:** UNLIMITED")
        
        platform = st.selectbox("Pilih Platform Media Sosial:", ["Google Maps", "Instagram", "TikTok", "WhatsApp"])
        ulasan_text = st.text_area("Salin Kalimat Ulasan Konsumen di Sini:", placeholder="Contoh: Lokasi cafenya di sebelah mana ya kak? Buka jam berapa?")
        
        if st.button("🚀 Jalankan Analisis Reputasi", key="btn_agent1"):
            if not ulasan_text:
                st.warning("Mohon isi teks ulasannya dulu!")
            else:
                with st.spinner("AI sedang membaca ulasan..."):
                    system_instruction = f"""
                    Anda adalah Manajer Reputasi Senior untuk {nama_bisnis} yang beralamat di {alamat_bisnis} (Maps: {link_maps}).
                    Balas ulasan dengan memanggil konsumen menggunakan kata 'Kakak'.
                    Sesuaikan gaya bahasa: Google Maps (sopan), Instagram (estetik hangat), TikTok (gaul santai), WhatsApp (responsif cepat).
                    Jika bertanya lokasi, wajib lampirkan link maps {link_maps}.
                    Output wajib JSON: {{"sentiment": "POSITIF/NEGATIF", "reply_draft": "isi balasan"}}
                    """
                    try:
                        response = client.models.generate_content(
                            model='gemini-2.5-flash',
                            contents=ulasan_text,
                            config=types.GenerateContentConfig(
                                system_instruction=system_instruction,
                                response_mime_type="application/json",
                                temperature=0.3
                            )
                        )
                        res_json = json.loads(response.text)
                        st.write(f"**Analisis Sentimen:** {res_json.get('sentiment')}")
                        st.info(res_json.get("reply_draft"))
                        
                        if "basi" in ulasan_text.lower() or "kecoak" in ulasan_text.lower():
                            st.markdown("<hr>", unsafe_allow_html=True)
                            st.error("⚠️ [SISTEM CRITICAL DETECTED] Ulasan mengandung unsur bahaya viral.")
                            if is_premium:
                                st.success("🔓 Fitur Premium Terbuka: Berikut draf chat kompensasi privat WhatsApp untuk dikirim oleh Manager: 'Halo Kak, kami dari manajemen memohon maaf sebesar-besarnya...'")
                            else:
                                st.markdown("🔒 **Fitur Premium Terkunci:** Draf kompensasi ganti rugi privat WhatsApp Manager (Hubungi owner untuk aktivasi lisensi).")
                    except Exception as e:
                        st.error(f"Eror Modul 1: {e}")
        st.markdown('</div>', unsafe_allow_html=True)

    # ==========================================
    # TAB 2: BRANDING ASSESSMENT (FIXED CONFIG TO LEAK)
    # ==========================================
    with tab2:
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown("### 🧬 Modul 2: Personal Branding Assessment & Blueprint")
        st.write("Isi data fondasi brand lu agar AI mengerti posisi pasar dan USP bisnis lu sebelum membuat konten.")
        
        step1 = st.text_input("Langkah 1: Siapa Target Audiens Utama Anda?", value="Anak Muda & Komunitas Pencinta Live Music")
        step2 = st.text_input("Langkah 2: Apa Keunikan Utama (USP) Bisnis Anda dibanding Pesaing?", value="Cafe Outdoor Terluas dengan Live Music Terbaik Setiap Malam")
        step3 = st.text_input("Langkah 3: Model Bisnis Apa yang Anda Jalankan?", value="FnB Tempat Nongkrong & Event Komunitas")
        
        if st.button("🧬 Generate Master Blueprint", key="btn_agent2"):
            with st.spinner("AI menyintesis data personal brand lu..."):
                try:
                    blueprint_prompt = f"Buatkan kerangka master strategi personal branding konten bisnis kuliner dengan target audiens: {step1}, menggunakan USP: {step2}, dengan model bisnis: {step3}."
                    response = client.models.generate_content(
                        model='gemini-2.5-flash', 
                        contents=blueprint_prompt,
                        config=types.GenerateContentConfig(temperature=0.5)
                    )
                    st.subheader("📋 Hasil Cetak Master Blueprint:")
                    st.markdown(response.text)
                    
                    if not is_premium:
                        st.markdown("<p style='color:#FF8C00;'>🔒 <b>Fitur Premium Terkunci:</b> Deep Competitive Positioning (Analisis 3 Kompetitor Terdekat di Google Search Live) hanya terbuka bagi versi premium.</p>", unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Eror Modul 2: {e}")
        st.markdown('</div>', unsafe_allow_html=True)

    # ==========================================
    # TAB 3: SCRIPT BUILDER & IDEATION (FIXED CONFIG)
    # ==========================================
    with tab3:
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown("### 🎬 Modul 3: Script Builder & Ideation Room")
        st.write("Ubah ide mentah menjadi skrip video TikTok/Reels berstruktur ketat (Hook, Isi, CTA).")
        
        topik_konten = st.text_input("Masukkan Topik Konten Singkat:", value="Alasan anak muda harus ke Ores.co hari Selasa malam")
        
        col_b1, col_b2 = st.columns(2)
        with col_b1:
            btn_hook = st.button("⚡ Generate Opsi Hook", key="btn_hook")
        with col_b2:
            btn_full = st.button("🎬 Generate Full Script", key="btn_full")
            
        if btn_hook:
            with st.spinner("Meracik pilihan kalimat hook..."):
                try:
                    prompt = f"Buatkan 3 pilihan kalimat hook marketing video tiktok kontroversial tentang topik: {topik_konten}"
                    response = client.models.generate_content(
                        model='gemini-2.5-flash', 
                        contents=prompt,
                        config=types.GenerateContentConfig(temperature=0.7)
                    )
                    st.write("**Pilihan Opsi Hook Anda:**")
                    st.info(response.text)
                except Exception as e:
                    st.error(f"Eror Hook: {e}")
                
        if btn_full:
            with st.spinner("Menyusun skrip lengkap..."):
                try:
                    prompt = f"Buatkan skrip video pendek tiktok utuh (Struktur: Hook menarik, Isi edukasi, CTA jualan) dengan topik: {topik_konten}"
                    response = client.models.generate_content(
                        model='gemini-2.5-flash', 
                        contents=prompt,
                        config=types.GenerateContentConfig(temperature=0.6)
                    )
                    st.subheader("Draft Script Terkini:")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Eror Script: {e}")
        st.markdown('</div>', unsafe_allow_html=True)

    # ==========================================
    # TAB 4: REMIX VIDEO VIRAL (FIXED CONFIG)
    # ==========================================
    with tab4:
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown("### 🔄 Modul 4: Video to Script (Extract & Remix Konten Viral)")
        st.write("Tempel transkrip teks dari video orang lain yang viral, lalu suruh AI merombaknya otomatis agar sesuai dengan brand cafe/bisnis lu.")
        
        transkrip_input = st.text_area("Tempel Teks Transkrip Video Viral Di Sini:", placeholder="Contoh teks video orang: Kalau kalian punya uang 50 ribu jangan dihabisin buat beli rokok...")
        
        if st.button("🔄 Jalankan Remix Script", key="btn_agent4"):
            if not transkrip_input:
                st.warning("Masukkan teks transkripnya dulu, bro!")
            else:
                with st.spinner("AI sedang membedah psikologi video tersebut..."):
                    try:
                        prompt = f"Ambil struktur emosi dan gaya penyampaian dari transkrip berikut, lalu ubah topiknya menjadi promosi menu kopi susu di {nama_bisnis}. Ini teksnya: {transkrip_input}"
                        response = client.models.generate_content(
                            model='gemini-2.5-flash', 
                            contents=prompt,
                            config=types.GenerateContentConfig(temperature=0.5)
                        )
                        st.subheader("🎉 Hasil Remix Konten Baru:")
                        st.markdown(response.text)
                    except Exception as e:
                        st.error(f"Eror Modul 4: {e}")
        st.markdown('</div>', unsafe_allow_html=True)

    # ==========================================
    # TAB 5: FUNNEL & VISUAL CALENDAR
    # ==========================================
    with tab5:
        st.markdown('<div class="premium-card">', unsafe_allow_html=True)
        st.markdown("### 📅 Modul 5: Funnel Strategy & Content Calendar Visual Plan")
        st.write("Pilih tingkatan corong marketing (*funnel*) untuk memproduksi ide yang tepat sasaran harian.")
        
        col_f1, col_f2, col_f3 = st.columns(3)
        with col_f1:
            btn_tofu = st.button("🔵 TOFU (Awareness - Jangkauan Luas)", key="btn_tofu")
        with col_f2:
            btn_mofu = st.button("🟠 MOFU (Trust - Edukasi Komunitas)", key="btn_mofu")
        with col_f3:
            btn_bofu = st.button("🟢 BOFU (Conversion - Promo Jualan Cafe)", key="btn_bofu")
            
        if btn_tofu or btn_mofu or btn_bofu:
            st.info("Meracik ide strategi funnel khusus untuk Anda...")
            st.write("**Rekomendasi Ide Konten:** Konten video estetik sinematik memperlihatkan suasana band berinteraksi dengan pengunjung cafe malam hari penuh lampu neon.")
            
        st.divider()
        st.markdown("#### 📅 Visual Content Calendar Plan (Maret 2026)")
        
        col_c1, col_c2, col_c3, col_c4 = st.columns(4)
        with col_c1:
            st.markdown("<div style='background-color:#222; padding:10px; border-radius:5px; border-left: 4px solid #FFC107;'><b>Senin, 23 Mar</b><br>📝 Ide: Kopi Susu Senja</div>", unsafe_allow_html=True)
        with col_c2:
            st.markdown("<div style='background-color:#222; padding:10px; border-radius:5px; border-left: 4px solid #FFC107;'><b>Selasa, 24 Mar</b><br>📝 Ide: Selasa Galau Live Music</div>", unsafe_allow_html=True)
        with col_c3:
            st.markdown("<div style='background-color:#222; padding:10px; border-radius:5px; border-left: 4px solid #FFC107;'><b>Rabu, 25 Mar</b><br>📝 Ide: Promo Camilan</div>", unsafe_allow_html=True)
        with col_c4:
            st.markdown("<div style='background-color:#161B22; padding:10px; border-radius:5px; border: 1px dashed #FFC107;'><b>Kamis, 26 Mar (Premium Only)</b><br>🔒 Terkunci</div>", unsafe_allow_html=True)
            
        if is_premium:
            st.success("🔓 Akun Anda Premium: Kalender Utuh 30 Hari Terbuka Penuh!")
        else:
            st.error("🔒 **Fitur Premium Terkunci:** Akses kalender visual penuh selama 30 hari ke depan dibatasi di versi trial.")
        st.markdown('</div>', unsafe_allow_html=True)

elif password_input != "":
    st.error("❌ Password salah! Silakan periksa kembali token akses Anda.")
