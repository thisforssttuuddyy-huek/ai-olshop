import streamlit as st
import google.generativeai as genai

# --- PENGATURAN HALAMAN ---
st.set_page_config(
    page_title="AI Asisten Konten Bisnis",
    page_icon="🚀",
    layout="centered"
)

# --- PASSWORD APLIKASI ---
APP_PASSWORD = "rahasia123ya" 

st.title("🚀 AI Asisten Konten Bisnis & Olshop")
st.write("Buat ide video TikTok, caption Instagram, dan hashtag otomatis untuk segala jenis bisnis dalam hitungan detik!")

# --- SISTEM LOGIN SEDERHANA ---
password_input = st.text_input("Masukkan Password Akses:", type="password")

if password_input == APP_PASSWORD:
    st.success("Akses diberikan! Selamat datang.")
    st.divider()
    
    # --- FORM INPUT KONTEN ---
    st.markdown("### 📝 Detail Bisnis & Produk")
    
    # Fitur Baru: Pilih Kategori Bisnis biar fleksibel!
    kategori_bisnis = st.selectbox(
        "Pilih Kategori Bisnis:",
        ["Online Shop (Baju, Skincare, Jualan Produk)", "Cafe / Resto / Kuliner", "Jasa / Lainnya"]
    )
    
    nama_produk = st.text_input("Nama Produk / Menu / Event:", placeholder="Contoh: Nasi Goreng Iga Bakar / Sepatu Sneakers")
    promo = st.text_area("Promo / Suasana / Detail Tambahan:", placeholder="Contoh: Diskon 15% khusus weekend, ada live music, tempatnya estetik.")
    
    # --- TOMBOL GENERATE ---
    if st.button("✨ Buat Konten", type="primary", use_container_width=True):
        if not nama_produk:
            st.warning("⚠️ Mohon masukkan Nama Produk atau Menu.")
        else:
            with st.spinner('Sedang meracik konten ajaib dengan AI... ⏳'):
                try:
                    # Mengambil API Key secara aman dari Secrets Streamlit
                    api_key = st.secrets["GEMINI_API_KEY"]
                    genai.configure(api_key=api_key)
                    
                    # Menggunakan model terbaru tahun 2026 yang super cepat
                    model = genai.GenerativeModel('gemini-2.5-flash')
                    
                    prompt = f"""
                    Kamu adalah seorang social media manager ahli, digital marketer, dan copywriter handal.
                    Tolong buatkan materi promosi yang sangat menarik, kreatif, kekinian (sesuai tren anak muda sekarang), dan persuasif berdasarkan informasi berikut:
                    - Kategori Bisnis: {kategori_bisnis}
                    - Nama Produk/Menu/Event: {nama_produk}
                    - Detail/Promo/Suasana: {promo}
                    
                    Harap berikan hasil dengan format berikut (pastikan terstruktur, estetik, dan mudah dibaca):
                    
                    ## 🎬 1. Ide Konten Video TikTok / Reels (Visual & Kreatif)
                    - **Kalimat Hook Pembuka (3 detik pertama yang memancing perhatian):** [Tulis kalimat hook yang kuat]
                    - **Konsep Visual & Angle Kamera:** [Jelaskan adegan per adegan atau sudut kamera yang harus diambil agar estetik]
                    - **Skrip Voice Over (VO):** [Tulis teks dialog/narasi yang santai, gaul, dan persuasif]
                    
                    ## 📸 2. Caption Instagram / Sosial Media
                    (Buat caption yang persuasif, gunakan spasi/paragraf yang enak dibaca, sertakan emoji yang relevan, info harga/promo, dan ajakan bertindak/Call to Action)
                    
                    ## #️⃣ 3. Hashtag Optimasi
                    (Berikan 15-20 hashtag campuran yang relevan, sedang tren, dan spesifik sesuai kategori bisnis tersebut)
                    """
                    
                    response = model.generate_content(prompt)
                    
                    st.divider()
                    st.markdown("### 🎉 Yeay! Konten Anda Sudah Siap:")
                    st.info("Anda bisa langsung menyalin (copy) teks di bawah ini.")
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"❌ Terjadi kesalahan saat menghubungi AI: {e}")

elif password_input != "":
    st.error("❌ Password salah! Silakan coba lagi.")
