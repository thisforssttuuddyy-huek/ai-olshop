import streamlit as st
import json
from google import genai
from google.genai import types

# --- PENGATURAN HALAMAN DASHBOARD ---
st.set_page_config(
    page_title="AI Agent Suite",
    page_icon="☕",
    layout="centered"
)

APP_PASSWORD = "rahasia123" 

st.title("⚡ Kopi Senja - AI Agent Suite")
st.write("Sistem otomatisasi Multi-Agent berbasis Gemini API untuk manajemen ulasan dan tim kreatif konten.")

password_input = st.text_input("Masukkan Password Akses Premium:", type="password")

if password_input == APP_PASSWORD:
    st.success("Akses Sistem Multi-Agent Aktif!")
    st.divider()
    
    # --- INISIALISASI GEMINI CLIENT DARI SECRETS ---
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        client = genai.Client(api_key=api_key)
    except Exception as e:
        st.error(f"Gagal memuat API Key dari Streamlit Secrets: {e}")
        st.stop()

    # --- NAVIGASI PILIHAN AGENT ---
    pilihan_agent = st.selectbox(
        "🤖 Pilih Agent AI yang Ingin Dijalankan:",
        [
            "Agent 1: Review Responder (Analisis Sentimen & Balasan Otomatis)",
            "Agent 2: Menu & Content Copywriter (Riset Tren & Pembuat Konten Live)"
        ]
    )
    st.divider()

    # ==========================================
    # LOGIKA AGENT 1: REVIEW RESPONDER
    # ==========================================
    if "Agent 1" in pilihan_agent:
        st.markdown("### 🤖 Agent 1: Review Responder")
        st.write("Agent ini bertugas menganalisis ulasan pelanggan secara objektif dan meracik draf balasan profesional format JSON.")
        
        # Input Form dari User
        customer_review = st.text_area("Salin Ulasan Pelanggan di Sini:", placeholder="Contoh: Kopinya enak sih, tapi pelayanannya lama banget...")
        rating = st.slider("Rating Bintang (1 - 5):", min_value=1, max_value=5, value=5)
        
        if st.button("🚀 Jalankan Analisis & Balas", type="primary", use_container_width=True):
            if not customer_review:
                st.warning("Masukkan ulasan pelanggan terlebih dahulu, bro!")
            else:
                with st.spinner("Agent sedang membaca sentimen dan meracik balasan..."):
                    try:
                        system_instruction = """
                        Anda adalah AI Agent 'Review Responder' untuk 'Kopi Senja'.
                        Analisis rating dan review, lalu berikan respons sesuai aturan:
                        - Bintang 4-5: Positif, terima kasih, undang kembali.
                        - Bintang 1-3: Negatif, minta maaf, arahkan ke DM IG @kopisenja.id atau WA 08123456789 untuk kompensasi.
                        Output WAJIB berupa JSON dengan key 'sentiment' dan 'reply_draft'.
                        """
                        prompt = f"Rating: {rating}/5\nReview Pelanggan: '{customer_review}'"
                        
                        # Memanggil Gemini API dengan format JSON terstruktur
                        response = client.models.generate_content(
                            model='gemini-1.5-flash',
                            contents=prompt,
                            config=types.GenerateContentConfig(
                                system_instruction=system_instruction,
                                response_mime_type="application/json",
                                temperature=0.3
                            ),
                        )
                        
                        # Parsing hasil JSON teks menjadi objek dictionary Python
                        hasil_json = json.loads(response.text)
                        
                        # Menampilkan Output ke Dashboard Web
                        st.subheader("🎉 Hasil Kerja Agent:")
                        
                        # Indikator Visual Sentimen
                        if hasil_json.get("sentiment") == "POSITIF":
                            st.success(f"🟢 **Sentimen Terdeteksi:** {hasil_json.get('sentiment')}")
                        else:
                            st.error(f"🔴 **Sentimen Terdeteksi:** {hasil_json.get('sentiment')}")
                            
                        st.markdown("**Draf Balasan Teks:**")
                        st.info(hasil_json.get("reply_draft"))
                        
                        # Tampilkan raw JSON data jika developer ingin melihat kodenya
                        with st.expander("Lihat Raw Data Output JSON"):
                            st.json(hasil_json)
                            
                    except Exception as e:
                        st.error(f"Terjadi kesalahan teknis pada sistem: {e}")
                        
        st.info("💡 **Cara Kerja Sistem:** Masukkan ulasan dan rating. Sistem memaksa AI menghasilkan format JSON yang valid untuk membaca emosi pembeli tanpa bersikap defensif.")

    # ==========================================
    # LOGIKA AGENT 2: MENU & CONTENT COPYWRITER
    # ==========================================
    elif "Agent 2" in pilihan_agent:
        st.markdown("### ✍️ Agent 2: Menu & Content Copywriter")
        st.write("Agent kreatif senior yang dilengkapi fitur live internet (Google Search Grounding) untuk riset tren kopi secara real-time.")
        
        # Input Form dari User
        tema_promosi_atau_menu = st.text_input("Masukkan Tema Promosi / Menu Baru:", placeholder="Contoh: Menu baru Iced Matcha Espresso Latte promo buy 1 get 1 hari Jumat")
        
        if st.button("✨ Racik Ide Konten Instagram", type="primary", use_container_width=True):
            if not tema_promosi_atau_menu:
                st.warning("Tulis tema promosi atau menu barunya dulu, bro!")
            else:
                with st.spinner("Agent sedang browsing tren dan merancang draf visual kreatif..."):
                    try:
                        system_instruction = """
                        Anda adalah Senior Copywriter Instagram untuk 'Kopi Senja' (Café estetik, ramah anak muda/WFH).
                        Buatkan 1 draf konten lengkap (Hook, Konsep Visual, Caption santai/anak muda, Hashtag).
                        Gunakan data dari internet jika ada tren kopi/kuliner terbaru yang relevan dengan tema.
                        """
                        
                        # Mengaktifkan fitur Google Search Grounding bawaan Gemini terbaru
                        config = types.GenerateContentConfig(
                            system_instruction=system_instruction,
                            temperature=0.7,
                            tools=[types.Tool(google_search=types.GoogleSearch())]
                        )
                        
                        prompt = f"Buatkan konten Instagram menarik dengan tema/menu baru: {tema_promosi_atau_menu}"
                        
                        response = client.models.generate_content(
                            model='gemini-1.5-flash',
                            contents=prompt,
                            config=config
                        )
                        
                        # Menampilkan Output Teks Kreatif
                        st.subheader("🎬 Rekomendasi Konten Instagram:")
                        st.markdown(response.text)
                        
                    except Exception as e:
                        st.error(f"Terjadi kesalahan teknis saat browsing internet: {e}")
                        
        st.info("💡 **Cara Kerja Sistem:** Setiap ide konten yang diracik akan otomatis dicocokkan dengan apa yang sedang viral di Google hari ini. Membuat tim marketing lu selalu terdepan!")

elif password_input != "":
    st.error("❌ Password salah! Silakan periksa kembali akses Anda.")
