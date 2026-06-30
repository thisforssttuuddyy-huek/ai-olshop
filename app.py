import streamlit as st
import google.generativeai as genai

# --- PENGATURAN HALAMAN ---
st.set_page_config(
    page_title="AI Asisten Konten Olshop",
    page_icon="🛍️",
    layout="centered"
)

# --- PASSWORD APLIKASI ---
# Ubah password ini sesuai keinginan Anda
APP_PASSWORD = "Rahasia123ya" 

st.title("🛍️ AI Asisten Konten Olshop")
st.write("Buat ide video TikTok, caption Instagram, dan hashtag otomatis dalam hitungan detik!")

# --- SISTEM LOGIN SEDERHANA ---
password_input = st.text_input("Masukkan Password untuk mengakses aplikasi:", type="password")

if password_input == APP_PASSWORD:
    st.success("Akses diberikan! Selamat datang.")
    st.divider()
    
    # --- PENGATURAN API KEY ---
    st.markdown("### 🔑 Kredensial API")
    api_key = st.text_input("Masukkan Google Gemini API Key Anda:", type="password", help="Dapatkan API Key di Google AI Studio.")
    
    # --- FORM INPUT KONTEN ---
    st.markdown("### 📝 Detail Produk")
    nama_produk = st.text_input("Nama Produk:", placeholder="Contoh: Sepatu Sneakers Pria Anti Slip")
    promo = st.text_area("Promo / Detail Tambahan:", placeholder="Contoh: Diskon 50% khusus hari ini, gratis ongkir seluruh Indonesia.")
    
    # --- TOMBOL GENERATE ---
    if st.button("✨ Buat Konten", type="primary", use_container_width=True):
        if not api_key:
            st.warning("⚠️ Mohon masukkan Gemini API Key Anda terlebih dahulu.")
        elif not nama_produk:
            st.warning("⚠️ Mohon masukkan Nama Produk.")
        else:
            with st.spinner('Sedang meracik konten ajaib untuk olshop Anda... ⏳'):
                try:
                    # Konfigurasi Gemini API
                    genai.configure(api_key=api_key)
                    # Menggunakan model gemini-1.5-flash untuk respon yang cepat dan akurat
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    
                    # Prompt / Perintah untuk Gemini
                    prompt = f"""
                    Kamu adalah seorang social media manager ahli dan copywriter handal untuk online shop.
                    Tolong buatkan materi promosi yang menarik, gaul, dan persuasif (bikin orang ingin beli) berdasarkan informasi berikut:
                    - Nama Produk: {nama_produk}
                    - Promo/Detail: {promo}
                    
                    Harap berikan hasil dengan format berikut (pastikan terstruktur dan mudah dibaca):
                    
                    ## 🎬 1. Ide Konten Video TikTok
                    (Jelaskan konsep videonya. Apa Hook/kalimat pertama yang menarik perhatian, bagaimana isi/visual videonya, dan apa Call to Action (CTA) di akhir video)
                    
                    ## 📸 2. Caption Instagram
                    (Buat caption yang estetik, persuasif, gunakan spasi/paragraf yang enak dibaca, dan sertakan emoji yang relevan. Jangan lupa masukkan info promo dan ajakan membeli)
                    
                    ## #️⃣ 3. Hashtag
                    (Berikan 15-20 hashtag campuran yang relevan, sedang tren, dan spesifik untuk produk tersebut)
                    """
                    
                    # Memanggil API untuk membuat konten
                    response = model.generate_content(prompt)
                    
                    # Menampilkan hasil
                    st.divider()
                    st.markdown("### 🎉 Yeay! Konten Anda Sudah Siap:")
                    st.info("Anda bisa langsung menyalin (copy) teks di bawah ini.")
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"❌ Terjadi kesalahan saat menghubungi API: {e}")

elif password_input != "":
    st.error("❌ Password salah! Silakan coba lagi.")
