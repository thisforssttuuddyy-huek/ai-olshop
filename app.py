import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- PENGATURAN HALAMAN ---
st.set_page_config(
    page_title="AI Marketing Suite v4.0",
    page_icon="🚀",
    layout="centered"
)

APP_PASSWORD = "rahasia123" 

st.title("🚀 AI Marketing Suite v4.0")
st.write("Satu aplikasi dengan 10 modul simulator AI terbaik berdasarkan riset industri marketing terkini.")

password_input = st.text_input("Masukkan Password Akses Premium:", type="password")

if password_input == APP_PASSWORD:
    st.success("Akses Premium Aktif! Semua modul simulator siap digunakan.")
    st.divider()
    
    # --- NAVIGASI 10 TOOLS BARU ---
    fitur = st.selectbox(
        "🔥 Pilih Modul AI Hasil Riset:",
        [
            "1. Opus Clip / CapCut AI (Video Shortener)",
            "2. Photoroom AI (Studio Photo Background)",
            "3. Gamma App (Proposal & Deck Builder)",
            "4. Jasper AI / Copy.ai (High-Converting Copy)",
            "5. Surfer SEO (Content Ranking Optimizer)",
            "6. ManyChat AI (Automated Chat & FAQ Bot)",
            "7. Zapier AI Copilot (Workflow Automation)",
            "8. Perplexity AI (Market & Trend Research)",
            "9. Claude AI (Sales Data Insight Analyzer)",
            "10. Brand24 (Social Listening & Crisis Control)"
        ]
    )
    st.divider()

    # --- KONFIGURASI MODEL GEMINI ---
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')
    except Exception as e:
        st.error(f"Gagal konfigurasi AI: {e}")
        st.stop()

    # ==========================================
    # 1. OPUS CLIP / CAPCUT AI
    # ==========================================
    if "1. Opus Clip" in fitur:
        st.markdown("### 🎬 Modul Opus Clip / CapCut AI")
        st.write("Simulasikan pemotongan video panjang menjadi draf konten pendek yang siap viral.")
        konsep_video = st.text_input("Ketik Konsep / Topik Video Panjang Anda:", placeholder="Contoh: Review Nasi Goreng Iga Bakar Ores.co durasi 5 menit")
        
        if st.button("✂️ Potong Menjadi Konten Pendek", type="primary", use_container_width=True):
            if not konsep_video: st.warning("Isi konsep videonya dulu, bro.")
            else:
                with st.spinner("Memotong video..."):
                    prompt = f"Bertindaklah sebagai Opus Clip AI. Dari konsep video panjang '{konsep_video}', potong dan pecah menjadi 3 draf ide video pendek (TikTok/Reels) berdurasi 15 detik. Untuk setiap draf, berikan: 1. Estimasi Viral Score (90-99%), 2. Kalimat Hook on-screen, 3. Draf Subtitle otomatis yang menarik."
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
        
        st.info("💡 **Cara Penggunaan:** Masukkan tema video panjang Anda, lalu AI akan langsung memotongnya menjadi 3 ide video pendek lengkap dengan teks subtitle siap pakai.")

    # ==========================================
    # 2. PHOTOROOM AI
    # ==========================================
    elif "2. Photoroom AI" in fitur:
        st.markdown("### 📸 Modul Photoroom AI")
        st.write("Analisis foto produk Anda dan dapatkan rekomendasi penggantian background studio yang estetik.")
        uploaded_img = st.file_uploader("Upload Foto Produk / Menu Anda:", type=["jpg", "jpeg", "png"], key="f2")
        
        if st.button("🖼️ Rancang Latar Belakang Studio", type="primary", use_container_width=True):
            if uploaded_img is None: st.warning("Upload foto produkmu dulu, bro.")
            else:
                with st.spinner("Merancang background studio premium..."):
                    img = Image.open(uploaded_img)
                    prompt = "Bertindaklah sebagai Photoroom AI. Analisis objek utama pada foto ini. Berikan 3 rekomendasi konsep latar belakang (background) studio pengganti yang estetik dan cocok dengan produk tersebut (misal: tema kayu gelap rustic, marmer mewah, atau neon cyberpunk) lengkap dengan saran pencahayaannya."
                    response = model.generate_content([prompt, img])
                    st.markdown(response.text)
        
        st.info("💡 **Cara Penggunaan:** Upload foto produk dengan latar belakang biasa. AI akan memberikan rekomendasi setup background studio kelas atas untuk foto katalog Anda.")

    # ==========================================
    # 3. GAMMA APP
    # ==========================================
    elif "3. Gamma App" in fitur:
        st.markdown("### 📊 Modul Gamma App")
        st.write("Buat kerangka slide presentasi atau proposal bisnis instan hanya dari satu baris perintah.")
        topik_deck = st.text_input("Masukkan Topik Proposal / Presentasi Anda:", placeholder="Contoh: Proposal Kerja Sama Marketing AI dengan Cafe Ores.co")
        
        if st.button("✨ Susun Outline Presentasi", type="primary", use_container_width=True):
            if not topik_deck: st.warning("Tulis topik proposalnya dulu, bro.")
            else:
                with st.spinner("Menyusun kerangka slide..."):
                    prompt = f"Bertindaklah sebagai Gamma App. Buatkan outline atau kerangka slide presentasi profesional sebanyak 5 slide berdasarkan topik '{topik_deck}'. Tuliskan judul slide beserta poin-poin singkat isinya yang persuasif."
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
        
        st.info("💡 **Cara Penggunaan:** Masukkan topik proposal, klik tombol, dan salin struktur tulisan yang keluar untuk langsung dijadikan bahan slide presentasi Anda.")

    # ==========================================
    # 4. JASPER AI / COPY.AI
    # ==========================================
    elif "4. Jasper AI" in fitur:
        st.markdown("### ✍️ Modul Jasper AI / Copy.ai")
        st.write("Racik draf copywriting iklan atau caption media sosial yang fokus pada peningkatan konversi penjualan.")
        detail_jualan = st.text_area("Detail Produk & Promo:", placeholder="Contoh: Es Pisang Ijo Ores.co, harga 25k, segar, manis, diskon khusus weekend")
        
        if st.button("🔥 Buat High-Converting Copy", type="primary", use_container_width=True):
            if not detail_jualan: st.warning("Isi detail produk yang mau dijual, bro.")
            else:
                with st.spinner("Menulis teks iklan..."):
                    prompt = f"Bertindaklah sebagai Jasper AI. Buatkan 2 variasi teks iklan/caption media sosial menggunakan formula copywriting AIDA (Attention, Interest, Desire, Action) yang sangat persuasif berdasarkan detail produk ini: '{detail_jualan}'."
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
        
        st.info("💡 **Cara Penggunaan:** Isi detail produk dan promo. AI akan meracik teks iklan psikologis yang memicu pembaca untuk langsung melakukan pembelian.")

    # ==========================================
    # 5. SURFER SEO
    # ==========================================
    elif "5. Surfer SEO" in fitur:
        st.markdown("### 🌐 Modul Surfer SEO")
        st.write("Dapatkan rekomendasi kata kunci (keywords) penting agar konten web Anda nangkring di halaman pertama Google.")
        topik_seo = st.text_input("Ketik Topik Artikel / Keyword Utama Target Anda:", placeholder="Contoh: Cafe live music terdekat di Cikarang")
        
        if st.button("📈 Ambil Strategi Keyword SEO", type="primary", use_container_width=True):
            if not topik_seo: st.warning("Tulis topik keyword utamanya dulu, bro.")
            else:
                with st.spinner("Menganalisis algoritma Google..."):
                    prompt = f"Bertindaklah sebagai Surfer SEO. Untuk keyword utama '{topik_seo}', berikan: 1. 10 Kata kunci pendukung (LSI keywords) yang wajib dimasukkan ke dalam artikel, 2. Rekomendasi jumlah kata ideal, 3. Saran judul artikel yang menarik klik (Click-through rate tinggi)."
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
        
        st.info("💡 **Cara Penggunaan:** Tulis kata kunci utama bisnis Anda. AI akan memberikan daftar kata kunci rahasia agar website Anda gampang ditemukan di Google secara organik.")

    # ==========================================
    # 6. MANYCHAT (AI INTEGRATED)
    # ==========================================
    elif "6. ManyChat" in fitur:
        st.markdown("### 🤖 Modul ManyChat AI")
        st.write("Rancang alur pesan otomatis (Chatbot Automation) untuk membalas DM konsumen 24 jam nonstop.")
        pemicu = st.text_input("Ketik Kata Kunci Pemicu (Trigger Keyword):", placeholder="Contoh: Pembeli ketik 'MAU' atau 'INFO HARGA'")
        
        if st.button("🤖 Rancang Alur Chatbot", type="primary", use_container_width=True):
            if not pemicu: st.warning("Tulis kata kunci pemicunya dulu, bro.")
            else:
                with st.spinner("Menyusun logika chatbot otomatis..."):
                    prompt = f"Bertindaklah sebagai ManyChat AI. Buatkan draf alur chat otomatis (Flow Chart teks) ketika konsumen mengetik kata '{pemicu}'. Berikan draf balasan pesan pertama, pilihan menu interaktif, dan cara mengarahkan mereka hingga transaksi selesai via WhatsApp."
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
        
        st.info("💡 **Cara Penggunaan:** Isi kata kunci yang sering diketik netizen. AI akan membuatkan skema balasan otomatis agar konsumen terlayani instan meskipun admin sedang tidur.")

    # ==========================================
    # 7. ZAPIER (AI COPILOT)
    # ==========================================
    elif "7. Zapier" in fitur:
        st.markdown("### ⚙️ Modul Zapier AI Copilot")
        st.write("Otomatisasikan pekerjaan antar aplikasi tanpa perlu input data manual satu per satu.")
        kerja_manual = st.text_input("Tulis Alur Kerja yang Mau Diotomatisasi:", placeholder="Contoh: Kalau ada orang isi form di Instagram Ads, tolong kirim data ke WhatsApp admin")
        
        if st.button("⚙️ Buat Skema Otomatisasi (Zap)", type="primary", use_container_width=True):
            if not kerja_manual: st.warning("Tulis dulu alur kerja manualnya, bro.")
            else:
                with st.spinner("Merancang integrasi sistem..."):
                    prompt = f"Bertindaklah sebagai Zapier AI Copilot. Terjemahkan perintah ini: '{kerja_manual}' menjadi skema 'Zap' yang konkret. Sebutkan Aplikasi Pemicu (Trigger), Aplikasi Aksi (Action), dan data apa saja yang akan dipindahkan secara otomatis tanpa eror."
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
        
        st.info("💡 **Cara Penggunaan:** Ketik tugas berulang yang bikin admin capek. AI akan merancang skema penghubung antar aplikasi agar semua data berjalan otomatis.")

    # ==========================================
    # 8. PERPLEXITY AI
    # ==========================================
    elif "8. Perplexity" in fitur:
        st.markdown("### 🔍 Modul Perplexity AI")
        st.write("Riset tren pasar dan taktik promo kompetitor secara tajam, akurat, dan berbasis data nyata.")
        kueri_riset = st.text_input("Apa yang Ingin Anda Riset Hari Ini?:", placeholder="Contoh: Tren menu minuman anak muda di Bekasi tahun 2026")
        
        if st.button("🔍 Jalankan Riset Pasar", type="primary", use_container_width=True):
            if not kueri_riset: st.warning("Masukkan kueri riset pasar Anda, bro.")
            else:
                with st.spinner("Memindai data tren pasar industri..."):
                    prompt = f"Bertindaklah sebagai Perplexity AI. Lakukan analisis mendalam mengenai topik '{kueri_riset}'. Berikan kesimpulan tren terkini, taktik kompetitor yang sukses pada bidang tersebut, dan 2 saran promo konkret yang pasti laku."
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
        
        st.info("💡 **Cara Penggunaan:** Ketik hal atau tren yang mau Anda pelajari. AI akan memberikan ringkasan data riset valid untuk meminimalisir risiko kegagalan promosi.")

    # ==========================================
    # 9. CLAUDE AI
    # ==========================================
    elif "9. Claude" in fitur:
        st.markdown("### 📊 Modul Claude AI")
        st.write("Masukkan ringkasan data laporan atau omset penjualan Anda untuk dicari kelemahan dan peluang promonya.")
        data_penjualan = st.text_area("Ketik atau Tempel Ringkasan Data Penjualan Anda:", placeholder="Contoh: Minggu 1 Spaghetti laku 50 porsi, Minggu 2 drop jadi 20 porsi. Menu Rahang Tuna stabil di 40 porsi.")
        
        if st.button("📊 Analisis Data Penjualan", type="primary", use_container_width=True):
            if not data_penjualan: st.warning("Masukkan ringkasan data penjualan Anda dulu, bro.")
            else:
                with st.spinner("Membaca pola data dan insight tersembunyi..."):
                    prompt = f"Bertindaklah sebagai Claude AI yang ahli dalam analisis data bisnis. Analisis data penjualan berikut: '{data_penjualan}'. Berikan kesimpulan produk mana yang performanya paling buruk, mengapa itu bisa terjadi, dan racik 1 strategi promo jitu untuk mendongkrak penjualannya bulan depan."
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
        
        st.info("💡 **Cara Penggunaan:** Masukkan data angka/catatan penjualan berkala toko Anda. AI akan menemukan masalah bisnis Anda dan memberikan solusi promosi yang pas.")

    # ==========================================
    # 10. BRAND24
    # ==========================================
    elif "10. Brand24" in fitur:
        st.markdown("### 📢 Modul Brand24")
        st.write("Simulasikan pelacakan opini netizen (Social Listening) untuk mengontrol krisis reputasi brand Anda.")
        nama_brand = st.text_input("Masukkan Nama Brand Anda:", placeholder="Contoh: Cafe Ores.co Cikarang")
        
        if st.button("📢 Lacak Sentimen Netizen", type="primary", use_container_width=True):
            if not nama_brand: st.warning("Masukkan nama brand Anda dulu, bro.")
            else:
                with st.spinner("Memindai pembicaraan di internet..."):
                    prompt = f"Bertindaklah sebagai Brand24 AI Simulator. Simulasikan laporan social listening untuk brand '{nama_brand}'. Berikan analisis perbandingan sentimen positif vs negatif di internet, sebutkan 1 contoh skenario komplain konsumen yang paling mungkin terjadi, dan tuliskan langkah penanganan krisis (PR Crisis Control) instan sebelum viral."
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
        
        st.info("💡 **Cara Penggunaan:** Masukkan nama bisnis Anda. AI akan mensimulasikan isu atau komplain apa yang berpotensi muncul dari netizen beserta cara meredamnya sebelum viral.")

elif password_input != "":
    st.error("❌ Password salah!")
