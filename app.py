import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- PENGATURAN HALAMAN ---
st.set_page_config(
    page_title="AI Visual Content Director",
    page_icon="🎬",
    layout="centered"
)

APP_PASSWORD = "rahasia123" 

st.title("🎬 AI Visual Content Director")
st.write("Upload foto menu/cafe Anda, dan AI akan membuatkan panduan syuting video shot-by-shot yang instan & estetik!")

password_input = st.text_input("Masukkan Password Akses:", type="password")

if password_input == APP_PASSWORD:
    st.success("Akses diberikan!")
    st.divider()
    
    st.markdown("### 📸 Unggah Foto Menu / Cafe Anda")
    uploaded_file = st.file_uploader("Pilih foto (JPG/PNG):", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Foto yang berhasil di-upload", use_container_width=True)
        
        detail_tambahan = st.text_input("Detail tambahan (Opsional):", placeholder="Contoh: Menu ini lagi diskon 15% khusus weekend")
        
        if st.button("🎬 Racik Panduan Video Visual", type="primary", use_container_width=True):
            with st.spinner('AI sedang menganalisis foto dan menyusun panduan syuting... 🎥'):
                try:
                    api_key = st.secrets["GEMINI_API_KEY"]
                    genai.configure(api_key=api_key)
                    
                    # Menggunakan gemini-2.5-flash yang jago membaca gambar
                    model = genai.GenerativeModel('gemini-2.5-flash')
                    
                    prompt = f"""
                    Kamu adalah seorang Sutradara Konten TikTok/Reels profesional yang ahli dalam estetika kuliner dan cafe.
                    Analisis foto yang diunggah oleh pengguna ini. Buatkan panduan video singkat (durasi 15 detik) yang sangat visual, mudah dipahami, tidak kaku, dan tidak terasa seperti buatan AI biasa.
                    
                    Detail tambahan dari pengguna: {detail_tambahan}
                    
                    Berikan output dengan format terstruktur berikut:
                    
                    ### 🎯 Rencana Konten: [Tulis Judul Konsep Video]
                    **Saran Musik:** [Sebutkan jenis musik yang cocok, misal: lo-fi santai, tren jedag-jedug estetik, atau akustik]
                    
                    ---
                    
                    ### 🎥 PANDUAN SYUTING (SHOT-BY-SHOT)
                    
                    *   **DETIK 00-03 (The Hook):**
                        *   *Cara Ambil Video (Camera Angle):* [Jelaskan posisi kamera, misal: gerakkan HP dari bawah ke atas secara perlahan (tilt up) fokus ke produk]
                        *   *Apa yang Terjadi di Video:* [Jelaskan aksi visualnya]
                        *   *Teks di Layar (On-Screen Text):* [Tulis kalimat pendek yang bikin penasaran]
                        
                    *   **DETIK 03-10 (The Core):**
                        *   *Cara Ambil Video (Camera Angle):* [Misal: ambil jarak dekat (close up) saat makanan diaduk/dipotong]
                        *   *Apa yang Terjadi di Video:* [Jelaskan detail estetikanya]
                        *   *Teks di Layar (On-Screen Text):* [Tulis informasi keunggulan produk/menu]
                        
                    *   **DETIK 10-15 (The Outro / CTA):**
                        *   *Cara Ambil Video (Camera Angle):* [Misal: menjauh perlahan (pan out) memperlihatkan suasana meja cafe]
                        *   *Teks di Layar (On-Screen Text):* [Ajakan bertindak, misal: 'Gass ke Ores.co akhir pekan ini!']
                        
                    ---
                    
                    ### ✍️ CAPTION & HASHTAG SANTAI
                    [Buat 1 baris caption Instagram yang sangat santai gaya anak muda sekarang, diikuti 5-8 hashtag paling relevan]
                    """
                    
                    # Memanggil API dengan menyertakan gambar dan prompt teks
                    response = model.generate_content([prompt, image])
                    
                    st.divider()
                    st.markdown("### 🎉 Panduan Syuting Video Anda Sudah Siap:")
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"❌ Terjadi kesalahan saat menghubungi AI: {e}")

elif password_input != "":
    st.error("❌ Password salah! Silakan coba lagi.")
