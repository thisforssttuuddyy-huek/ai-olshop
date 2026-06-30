import streamlit as st
import json
from google import genai
from google.genai import types

# --- PENGATURAN HALAMAN DASHBOARD ---
st.set_page_config(
    page_title="AI Agent Marketing Suite",
    page_icon="☕",
    layout="centered"
)

APP_PASSWORD = "rahasia123" 

st.title("⚡ AI Agent Marketing Suite")
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
        
        # Input Form Dinamis dari User
        nama_cafe = st.text_input("Nama Cafe / Bisnis Anda:", placeholder="Contoh: Ores.co")
        ig_cafe = st.text_input("Username Instagram CS (Tanpa @):", placeholder="Contoh: ores.co")
        wa_cs = st.text_input("Nomor WhatsApp CS Bisnis:", placeholder="Contoh: 08123456789")
        
        customer_review = st.text_area("Salin Ulasan Pelanggan di Sini:", placeholder="Contoh: Kopinya enak sih, tapi pelayanannya lama banget...")
        rating = st.slider("Rating Bintang (1 - 5):", min_value=1, max_value=5, value=5)
        
        if st.button("🚀 Jalankan Analisis & Balas", type="primary", use_container_width=True):
            if not customer_review or not nama_cafe:
                st.warning("Masukkan ulasan pelanggan dan nama cafe terlebih dahulu, bro!")
            else:
                with st.spinner("Agent sedang membaca sentimen dan meracik balasan..."):
                    try:
                        system_instruction = f"""
                        Anda adalah AI Agent 'Review Responder' untuk bisnis kuliner bernama '{nama_cafe}'.
                        Analisis rating dan review, lalu berikan respons sesuai aturan:
                        - Bintang 4-5: Positif, terima kasih, sebutkan menu yang mereka puji jika ada, undang kembali. Gunakan gaya ramah dan kasual tapi tetap sopan.
                        - Bintang 1-3: Negatif, jangan defensif. Minta maaf dengan tulus atas ketidaknyamanan tersebut. Arahkan mereka ke DM IG @{ig_cafe} atau WA {wa_cs} agar manajemen bisa memberikan kompensasi (voucher/ganti rugi).
                        Output WAJIB berupa JSON dengan key 'sentiment' dan 'reply_draft'. Panggilan untuk pelanggan gunakan kata 'Kakak'.
                        """
                        prompt = f"Rating: {rating}/5\nReview Pelanggan: '{customer_review}'"
                        
                        response = client.models.generate_content(
                            model='gemini-1.5-flash',
                            contents=prompt,
                            config=types.GenerateContentConfig(
                                system_instruction=system_instruction,
                                response_mime_type="application/json",
                                temperature=0.3
                            ),
                        )
                        
                        hasil_json = json.loads(response.text)
                        
                        st.subheader("🎉 Hasil Kerja Agent:")
                        
                        if hasil_json.get("sentiment") == "POSITIF":
                            st.success(f"🟢 **Sentimen Terdeteksi:** {hasil_json.get('sentiment')}")
                        else:
                            st.error(f"🔴 **Sentimen Terdeteksi:** {hasil_json.get('sentiment')}")
                            
                        st.markdown("**Draf Balasan Teks:**")
                        st.info(hasil_json.get("reply_draft"))
                        
                        with st.expander("Lihat Raw Data Output JSON"):
                            st.json(hasil_json)
                            
                    except Exception as e:
                        st.error(f"Terjadi kesalahan teknis pada sistem: {e}")
                        
        st.info("💡 **Cara Kerja Sistem:** Masukkan ulasan dan rating bisnis. Sistem memaksa AI menghasilkan format JSON yang valid untuk membaca emosi pembeli tanpa bersikap defensif.")

    # ==========================================
    # LOGIKA AGENT 2: MENU & CONTENT COPYWRITER
    # ==========================================
    elif "Agent 2" in pilihan_agent:
        st.markdown("### ✍️ Agent 2: Menu & Content Copywriter")
        st.write("Agent kreatif senior yang dilengkapi fitur live internet (Google Search Grounding) untuk riset tren kuliner secara real-time.")
        
        # Input Form Dinamis dari User
        nama_cafe_2 = st.text_input("Nama Cafe / Bisnis Anda:", placeholder="Contoh: Ores.co")
        gaya_brand = st.text_input("Karakter / Vibes Cafe Anda:", placeholder="Contoh: Estetik, ramah anak muda, tempat asyik buat WFH, live music")
        
        tema_promosi_atau_menu = st.text_input("Masukkan Tema Promosi / Menu Baru:", placeholder="Contoh: Menu baru Iced Matcha Espresso Latte promo buy 1 get 1 hari Jumat")
        
        if st.button("✨ Racik Ide Konten Instagram", type="primary", use_container_width=True):
            if not tema_promosi_atau_menu or not nama_cafe_2:
                st.warning("Tulis nama cafe dan tema promosi atau menu barunya dulu, bro!")
            else:
                with st.spinner("Agent sedang browsing tren dan merancang draf visual kreatif..."):
                    try:
                        system_instruction = f"""
                        Anda adalah Senior Copywriter Instagram untuk bisnis kuliner bernama '{nama_cafe_2}'.
                        Karakter dan vibes brand: {gaya_brand}.
                        Buatkan 1 draf konten lengkap yang berisi: Hook (kalimat 3 detik pertama), Konsep Visual video/foto, Caption santai anak muda, dan Hashtag pilihan.
                        Gunakan data dari internet jika ada tren kopi/kuliner terbaru yang relevan dengan tema agar konten selalu kekinian.
                        """
                        
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
                        
                        st.subheader("🎬 Rekomendasi Konten Instagram:")
                        st.markdown(response.text)
                        
                    except Exception as e:
                        st.error(f"Terjadi kesalahan teknis saat browsing internet: {e}")
                        
        st.info("💡 **Cara Kerja Sistem:** Setiap ide konten yang diracik akan otomatis dicocokkan dengan apa yang sedang viral di Google secara real-time. Membuat strategi media sosial Anda selalu relevan.")

elif password_input != "":
    st.error("❌ Password salah! Silakan periksa kembali akses Anda.")
