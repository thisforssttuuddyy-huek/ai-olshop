import streamlit as st
import google.generativeai as genai
from PIL import Image
from datetime import datetime
import pytz

# --- PENGATURAN HALAMAN ---
st.set_page_config(
    page_title="AI Marketing Suite Pro",
    page_icon="⚡",
    layout="centered"
)

APP_PASSWORD = "rahasia123" 

st.title("⚡ The Ultimate AI Marketing Suite v3.0")
st.write("Platform AI All-in-One 11-in-1 untuk Mendominasi FYP Sosmed & Optimasi Penjualan Kuliner.")

password_input = st.text_input("Masukkan Password Akses Premium:", type="password")

if password_input == APP_PASSWORD:
    st.success("Akses Premium Aktif! Mode Real-Time Trend Engine Menyala.")
    st.divider()
    
    # --- REAL-TIME TREND ENGINE INDONESIA (WIB) ---
    tz = pytz.timezone('Asia/Jakarta')
    waktu_sekarang = datetime.now(tz)
    jam_sekarang = waktu_sekarang.strftime("%H:%M")
    
    st.info(f"🔄 **Trend Engine Status:** Diperbarui otomatis untuk jam **{jam_sekarang} WIB**. Algoritma FYP & Jam Viral telah disesuaikan.")

    # --- MENU NAVIGASI 11 TOOLS UTAMA ---
    fitur = st.selectbox(
        "🚀 Pilih Senjata AI Anda:",
        [
            "1. AI Viral Hook & Jam Posting (Real-Time FYP)",
            "2. AI Menu Storyteller (Skrip Vlog/POV)",
            "3. AI Competitor Auditor (Intip Strategi Lawan)",
            "4. AI Food Aesthetic Visual Grader (Kritikus Foto)",
            "5. AI 7-Day Content Calendar Planner (Jadwal Seminggu)",
            "6. AI Food Promo & Discount Crafting (Peracik Diskon)",
            "7. AI Auto-Reply Comment & DM (Template Balas Chat)",
            "8. AI TikTok Trend Jacking Router (Pemanfaat Sound/Tren)",
            "9. AI Psychographic Customer Persona (Pembedah Otak Pembeli)",
            "10. AI Smart Instagram Grid & Color Palette Designer",
            "11. AI SEO & Copywriting untuk GrabFood/GoFood"
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
    # FITUR 1 SAMPAI 8 (DIPERTAHANKAN DAN DIBERI PANDUAN STEP-BY-STEP)
    # ==========================================
    if "1. AI Viral Hook" in fitur:
        st.markdown("### 🎯 Real-Time AI Viral Hook & Prime Time Router")
        uploaded_img = st.file_uploader("Upload Foto Produk/Menu:", type=["jpg", "jpeg", "png"], key="f1")
        if st.button("🚀 Ambil Hook & Jam Viral Terbaru", type="primary", use_container_width=True):
            if uploaded_img is None: st.warning("Upload foto dulu.")
            else:
                with st.spinner("Menghitung algoritma..."):
                    img = Image.open(uploaded_img)
                    prompt = f"Jam sekarang {jam_sekarang} WIB. Berikan rekomendasi jam posting terdekat hari ini beserta alasannya, dan buatkan 3 pilihan kalimat hook pendek gaya anak muda sosmed untuk foto produk ini."
                    response = model.generate_content([prompt, img])
                    st.markdown(response.text)
        
        st.info("💡 **Cara Penggunaan:**\n1. Upload foto menu/produk yang mau diposting.\n2. Klik tombol di atas.\n3. AI akan mendeteksi jam saat ini dan langsung meracik jam paling pas buat posting beserta teks pemancing FYP-nya.")

    elif "2. AI Menu Storyteller" in fitur:
        st.markdown("### ✍️ AI Menu-to-Promo Storyteller")
        uploaded_img = st.file_uploader("Upload Foto Menu/Cafe:", type=["jpg", "jpeg", "png"], key="f2")
        sudut_pandang = st.selectbox("Sudut Pandang Cerita (POV):", ["Nemenin pacar/temen lagi bete", "Hidden gem tersembunyi", "Self-reward setelah capek kerja/sekolah", "Nongkrong hemat tapi keliatan elit"])
        if st.button("🎬 Buat Skrip Cerita", type="primary", use_container_width=True):
            if uploaded_img is None: st.warning("Upload foto dulu.")
            else:
                with st.spinner("Meracik cerita..."):
                    img = Image.open(uploaded_img)
                    prompt = f"Buatkan skrip video pendek TikTok 20-30 detik soft selling yang mengalir dan emosional dari foto ini dengan POV: {sudut_pandang}. Berikan Konsep Cerita, Teks Voice Over kasual, dan rekomendasi musik."
                    response = model.generate_content([prompt, img])
                    st.markdown(response.text)
        
        st.info("💡 **Cara Penggunaan:**\n1. Upload foto menu atau suasana cafe.\n2. Pilih sudut pandang (POV) cerita yang diinginkan.\n3. Klik tombol dan salin skrip narasi video untuk diisi suara (Voice Over) saat editing.")

    elif "3. AI Competitor Auditor" in fitur:
        st.markdown("### 🕵️‍♂️ AI Social Media Competitor Auditor")
        uploaded_screenshot = st.file_uploader("Upload Screenshot Akun/Feed Kompetitor:", type=["jpg", "jpeg", "png"], key="f3")
        if st.button("⚡ Bedah Strategi Lawan", type="primary", use_container_width=True):
            if uploaded_screenshot is None: st.warning("Upload screenshot dulu.")
            else:
                with st.spinner("Membedah strategi visual..."):
                    img = Image.open(uploaded_screenshot)
                    prompt = "Analisis visual dari screenshot kompetitor ini. Berikan: 1. Faktor X yang membuat postingan mereka ramai, 2. Dua ide tiru & modifikasi (ATM) konkret yang bisa kita terapkan langsung ke sosmed kita."
                    response = model.generate_content([prompt, img])
                    st.markdown(response.text)
        
        st.info("💡 **Cara Penggunaan:**\n1. Tangkap layar (screenshot) profil atau postingan kompetitor terberat yang lagi ramai.\n2. Upload gambarnya di sini.\n3. AI akan membongkar rahasia visual mereka dan memberikan ide jiplak kreatif (ATM).")

    elif "4. AI Food Aesthetic Visual Grader" in fitur:
        st.markdown("### 🎨 AI Food Aesthetic Visual Grader")
        uploaded_food = st.file_uploader("Upload Foto Makanan/Minuman Anda:", type=["jpg", "jpeg", "png"], key="f4")
        if st.button("⭐ Nilai Foto Saya", type="primary", use_container_width=True):
            if uploaded_food is None: st.warning("Upload foto dulu.")
            else:
                with st.spinner("AI sedang menilai..."):
                    img = Image.open(uploaded_food)
                    prompt = "Bertindaklah sebagai fotografer makanan profesional. Berikan Rating Visual (0-10), bedah kekurangan visualnya (lighting, angle, background), dan kasih panduan edit atau cara take ulang agar fotonya terlihat premium."
                    response = model.generate_content([prompt, img])
                    st.markdown(response.text)
        
        st.info("💡 **Cara Penggunaan:**\n1. Upload foto makanan/minuman hasil jepretan Anda sebelum di-post.\n2. AI akan menilai kelayakannya secara profesional dan ngasih tips instan agar visualnya terlihat jauh lebih mahal.")

    elif "5. AI 7-Day Content Calendar Planner" in fitur:
        st.markdown("### 📅 AI 7-Day Content Calendar Planner")
        nama_bisnis = st.text_input("Nama Cafe / Olshop Anda:", placeholder="Contoh: Ores.co Coffee")
        goals = st.selectbox("Target Utama Bulan Ini:", ["Naikin Brand Awareness (Views)", "Fokus Jualan Menu Baru (Omset)", "Interaksi & Nambah Followers"])
        if st.button("🗓️ Susun Kalendar Konten", type="primary", use_container_width=True):
            if not nama_bisnis: st.warning("Masukkan nama bisnis dulu.")
            else:
                with st.spinner("Menyusun strategi..."):
                    prompt = f"Buatkan tabel strategi jadwal konten media sosial selama 7 hari untuk {nama_bisnis} dengan target: {goals}. Tiap hari harus berisi: Tipe Konten (Reels/Feeds/Story), Ide Konten harian, dan rekomendasi jam upload."
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
        
        st.info("💡 **Cara Penggunaan:**\n1. Masukkan nama bisnis Anda.\n2. Pilih fokus target utama konten bulan ini.\n3. Jalankan AI untuk mendapatkan rencana kerja (tabel konten) selama seminggu penuh agar konsisten.")

    elif "6. AI Food Promo & Discount Crafting" in fitur:
        st.markdown("### 💰 AI Food Promo & Discount Crafting")
        menu_promo = st.text_input("Nama Menu yang Mau Dipromokan:", placeholder="Contoh: Nasi Goreng Iga Bakar")
        harga = st.text_input("Harga Normal (K):", placeholder="Contoh: 58")
        if st.button("🔥 Racik Strategi Promo", type="primary", use_container_width=True):
            if not menu_promo: st.warning("Masukkan nama menu.")
            else:
                with st.spinner("Meracik skema diskon..."):
                    prompt = f"Buatkan 3 opsi ide promo kreatif anak muda untuk menu {menu_promo} dengan harga normal {harga}k agar tidak merugi tapi viral. Berikan nama promo yang unik dan draf copywriting penawarannya."
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
        
        st.info("💡 **Cara Penggunaan:**\n1. Isi nama menu yang stoknya melimpah atau mau dipromosikan.\n2. Tulis nominal harga normalnya.\n3. AI akan merancang 3 jenis skema diskon psikologis anak muda yang bikin mereka buru-buru beli tanpa merugikan bisnis.")

    elif "7. AI Auto-Reply Comment & DM" in fitur:
        st.markdown("### 💬 AI Auto-Reply Comment & DM")
        tanya = st.text_area("Ketik Pertanyaan Pembeli / Komentar Netizen yang Sering Muncul:", placeholder="Contoh: Kak ini lokasinya di mana? Bisa delivery gak?")
        if st.button("💬 Buat Template Balasan", type="primary", use_container_width=True):
            if not tanya: st.warning("Isi dulu pertanyaannya.")
            else:
                with st.spinner("Menyusun kalimat..."):
                    prompt = f"Buatkan 3 variasi template jawaban otomatis yang ramah, santai, banyak emoji untuk membalas chat/komentar pembeli ini: '{tanya}'. Di akhir kalimat harus mengarahkan pembeli untuk order via WA/Link Bio."
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
        
        st.info("💡 **Cara Penggunaan:**\n1. Copas pertanyaan pembeli yang paling sering masuk ke DM atau kolom komentar.\n2. AI akan membuatkan 3 variasi template balasan super ramah dan mengarahkan mereka langsung transaksi (konversi).")

    elif "8. AI TikTok Trend Jacking Router" in fitur:
        st.markdown("### 📈 AI TikTok Trend Jacking Router")
        tren_skrg = st.text_input("Apa tren sound / dance / gimmick yang lagi ramai di TikTok saat ini?", placeholder="Contoh: Sound Asmalibrasi / Trend Jedag Jedug CapCut")
        menu_kita = st.text_input("Menu/Produk Anda yang Ingin Dimasukkan ke Tren:", placeholder="Contoh: Kopi Susu Gula Aren Ores.co")
        if st.button("⚡ Satukan dengan Tren", type="primary", use_container_width=True):
            if not tren_skrg: st.warning("Isi tren dulu.")
            else:
                with st.spinner("Menghubungkan tren..."):
                    prompt = f"Bagaimana cara melakukan soft-selling menu {menu_kita} memanfaatkan tren viral '{tren_skrg}' di TikTok? Berikan konsep eksekusi visual video yang mulus dan natural agar tidak terlihat kaku jualan."
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
        
        st.info("💡 **Cara Penggunaan:**\n1. Tulis sound, musik, atau gimmick yang lagi viral di FYP hari ini.\n2. Masukkan nama menu Anda.\n3. AI akan memikirkan jembatan kreatif (cara menunggangi tren) agar menu Anda ikut viral secara alami.")

    # ==========================================
    # FITUR 9: AI PSYCHOGRAPHIC CUSTOMER PERSONA (BARU)
    # ==========================================
    elif "9. AI Psychographic" in fitur:
        st.markdown("### 🧠 AI Psychographic Customer Persona (Pembedah Otak Pembeli)")
        st.write("Bedah profil psikologis terdalam dari konsumen yang paling berpotensi memborong menu Anda.")
        menu_analisis = st.text_input("Masukkan Menu / Kategori Makanan:", placeholder="Contoh: Nasi Goreng Iga Bakar / Kopi Susu Aren / Camilan Pedas")
        
        if st.button("🧠 Bedah Otak Pembeli", type="primary", use_container_width=True):
            if not menu_analisis: st.warning("Masukkan nama menunya dulu bro.")
            else:
                with st.spinner("Menganalisis perilaku konsumen harian..."):
                    prompt = f"""
                    Kamu adalah ahli Perilaku Konsumen (Consumer Behavior) dan Psikologi Marketing. Bedah profil psikologis target pembeli untuk menu: {menu_analisis}.
                    Berikan output terstruktur tanpa basa-basi kaku:
                    1. **Profil Utama Konsumen:** (Rentang umur, status sosial, gaya hidup)
                    2. **Ketakutan Terbesar Mereka (Pain Points):** (Apa yang membuat mereka ragu membeli, misal takut zonk rasanya, takut mahal, dll)
                    3. **Kata Kunci Pemicu Instan (Trigger Words):** (Berikan 5 kata emosional yang kalau ditaruh di caption, bikin mereka langsung lapar dan beli)
                    """
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
        
        st.info("💡 **Cara Penggunaan:**\n1. Ketik nama menu andalan Anda.\n2. Klik tombol untuk membedah profil psikologis target pasar Anda.\n3. Gunakan data ketakutan (pain points) dan kata kunci pemicu tersebut sebagai bahan dasar pembuatan konten medsos selanjutnya.")

    # ==========================================
    # FITUR 10: AI SMART INSTAGRAM GRID & COLOR PALETTE DESIGNER (BARU)
    # ==========================================
    elif "10. AI Smart Instagram Grid" in fitur:
        st.markdown("### 🎨 AI Smart Instagram Grid & Color Palette Designer")
        st.write("Upload 2-3 foto produk Anda secara acak. AI akan merancang skema palette warna feed dan menyusun urutan postingan agar terlihat rapi dan premium.")
        
        uploaded_files = st.file_uploader("Upload 2 sampai 3 Foto Menu Sekaligus:", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="f10")
        
        if st.button("🎨 Desain Skema Feed Premium", type="primary", use_container_width=True):
            if not uploaded_files or len(uploaded_files) < 2:
                st.warning("Mohon upload minimal 2 atau 3 foto dulu bro agar AI bisa menganalisis kombinasi warnanya.")
            else:
                with st.spinner("AI sedang menghitung keselarasan warna estetika..."):
                    # Mengambil gambar pertama untuk analisis (Gemini Flash sanggup membaca list gambar)
                    images_list = [Image.open(f) for f in uploaded_files]
                    prompt = """
                    Kamu adalah seorang Feed Designer & Creative Director Instagram ternama. Analisis kumpulan foto menu yang diunggah ini.
                    Berikan output konkret:
                    1. **Analisis Palette Warna Utama:** (Sebutkan dominasi warna dari foto-foto tersebut dan berikan saran 3 Kode Warna Hex pendukung agar feed terlihat estetik dan konsisten)
                    2. **Rencana Urutan Postingan (Grid 3 Slot):** (Beri panduan urutan posting, mana foto yang harus di kiri, tengah, atau kanan, serta jenis latar belakang/pencahayaan yang harus dipertahankan)
                    """
                    response = model.generate_content([prompt] + images_list)
                    st.markdown(response.text)
        
        st.info("💡 **Cara Penggunaan:**\n1. Upload 2 sampai 3 foto menu makanan/cafe Anda secara bersamaan.\n2. Klik tombol untuk mendesain.\n3. AI akan membaca keselarasan warna visualnya, memberikan kode warna utama, serta menyusun urutan postingan biar feed Instagram cafe terlihat rapi mirip akun profesional.")

    # ==========================================
    # FITUR 11: AI SEO & COPYWRITING UNTUK GRABFOOD/GOFOOD (BARU)
    # ==========================================
    elif "11. AI SEO & Copywriting" in fitur:
        st.markdown("### ✍️ AI SEO & Copywriting Deskripsi Menu Aplikasi Ojol")
        st.write("Ubah deskripsi menu yang membosankan di GrabFood/GoFood menjadi kalimat lezat penuh kata kunci SEO agar mudah dicari pembeli.")
        
        nama_ojol_menu = st.text_input("Nama Menu di Aplikasi:", placeholder="Contoh: Nasi Goreng Iga Bakar Premium")
        bahan_spesial = st.text_input("Keunggulan / Bahan Spesial:", placeholder="Contoh: Daging iga sapi lokal pilihan, dimasak 4 jam, sambal buatan sendiri")
        
        if st.button("✍️ Buat Deskripsi Ojol yang Bikin Laper", type="primary", use_container_width=True):
            if not nama_ojol_menu: st.warning("Nama menu tidak boleh kosong.")
            else:
                with st.spinner("Menyusun teks deskripsi lezat..."):
                    prompt = f"""
                    Kamu adalah seorang Copywriter khusus industri Kuliner. Buatkan deskripsi menu untuk aplikasi GrabFood/GoFood yang sangat menggugah selera (bikin lapar seketika saat dibaca), informatif, dan dioptimasi dengan kata kunci pencarian populer (SEO Kuliner) berdasarkan data berikut:
                    - Nama Menu: {nama_ojol_menu}
                    - Keunggulan: {bahan_spesial}
                    
                    Format output:
                    *   **Deskripsi Menu Premium (Copywriting):** (Buat teks deskripsi sepanjang 2-3 kalimat yang lezat dan persuasif)
                    *   **Rekomendasi Kata Kunci Tagging Teks:** (Berikan 5 kata kunci tersembunyi untuk dimasukkan ke sistem agar gampang muncul saat dicari pengguna ojol)
                    """
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
        
        st.info("💡 **Cara Penggunaan:**\n1. Tulis nama menu beserta keunggulan atau cara pembuatannya yang unik.\n2. Jalankan AI.\n3. Salin hasilnya ke pengaturan menu merchant GrabFood/GoFood Anda agar peringkat pencarian menunya naik dan memancing orang langsung memesan karena deskripsinya bikin ngiler.")

elif password_input != "":
    st.error("❌ Password salah!")
