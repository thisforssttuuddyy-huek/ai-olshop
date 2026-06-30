import streamlit as st
import json
import random
from google import genai
from google.genai import types

# --- CONFIGURASI HALAMAN STREAMLIT ---
st.set_page_config(
    page_title="OmniChannel AI Marketing Suite",
    page_icon="⚡",
    layout="wide"
)

# --- SISTEM KEAMANAN & PASSWORD ---
PASSWORD_SISTEM = "ores123"

st.title("⚡ OmniChannel AI Marketing Suite v5.0")
st.write("Sistem Multi-Agent AI Terintegrasi untuk Digital Marketing, Reputasi Multi-Platform, dan Desain Kreatif.")

password_input = st.text_input("🔑 Masukkan Password Akses Sistem:", type="password")

if password_input == PASSWORD_SISTEM:
    st.success("Akses Sistem Multi-Agent Aktif!")
    st.divider()

    # --- INISIALISASI CLIENT GEMINI API ---
    try:
        # Mengambil API KEY dari Streamlit Secrets
        api_key = st.secrets["GEMINI_API_KEY"]
        client = genai.Client(api_key=api_key)
    except Exception as e:
        st.error(f"Gagal memuat API Key dari Streamlit Secrets. Pastikan 'GEMINI_API_KEY' sudah dikonfigurasi. Eror: {e}")
        st.stop()

    # --- KONFIGURASI PROFIL BISNIS (SIDEBAR) ---
    st.sidebar.header("⚙️ Profil Bisnis & CS")
    nama_bisnis = st.sidebar.text_input("Nama Bisnis/Cafe:", value="Ores.co")
    wa_cs = st.sidebar.text_input("Nomor WA CS (Format 62):", value="628123456789")
    ig_bisnis = st.sidebar.text_input("Username Instagram Bisnis:", value="ores.co")
    tiktok_bisnis = st.sidebar.text_input("Username TikTok Bisnis:", value="ores.co")
    
    st.sidebar.divider()
    st.sidebar.subheader("📊 Status Kuota Pengguna (Trial 1 Minggu)")
    st.sidebar.info("💡 Akun Anda berada dalam masa peninjauan trial. Beberapa fitur taktis harian terbuka dengan batasan kuota.")

    # --- NAVIGASI ANTARA 7 AGENT ---
    pilihan_agent = st.selectbox(
        "🤖 Pilih Agen AI yang Ingin Anda Pekerjakan Hari Ini:",
        [
            "Agent 1: OmniChannel Reputation Manager (Balas Ulasan 4 Platform)",
            "Agent 2: Executive Analytics & Operational Auditor (Analisis Data Masalah)",
            "Agent 3: Creative Campaign & Event Director (Strategi Promo & Live Music)",
            "Agent 4: High-Converting Copywriter (Skrip Video & Caption AIDA)",
            "Agent 5: Automated Graphic Designer (Panduan Visual & Cetak Poster)",
            "Agent 6: Automation & Workflow Copilot (Arsitektur Admin Otomatis)",
            "Agent 7: Market Intelligence & Competitor Spy (Mata-Mata Tren Live Internet)"
        ]
    )
    st.divider()

    # ==========================================
    # AGENT 1: OMNICHANNEL REPUTATION MANAGER
    # ==========================================
    if "Agent 1" in pilihan_agent:
        st.markdown("### 🛡️ Agent 1: OmniChannel Reputation & PR Crisis Manager")
        st.write("**Fungsi:** Membalas ulasan masuk secara otomatis di 4 platform dengan karakter bahasa unik (Google Maps = Sopan/Solutif, IG = Estetik/Hangat, TikTok = Gaul/Santai, WA = Personal/Responsif).")
        
        # Indikator Kuota Trial
        st.caption("🟢 **Kuota Free Trial:** 5 penggunaan per hari.")
        
        platform = st.selectbox("Pilih Platform Ulasan/Komentar:", ["Google Maps", "Instagram", "TikTok", "WhatsApp"])
        ulasan_input = st.text_area("Salin Teks Ulasan / Komentar Konsumen di Sini:", placeholder="Contoh: Makanannya lumayan, tapi pelayanannya lambat banget tolong diperbaiki.")
        
        rating = 5
        if platform == "Google Maps":
            rating = st.slider("Rating Bintang Pelanggan:", min_value=1, max_value=5, value=5)

        if st.button("🚀 Jalankan Agen 1", type="primary"):
            if not ulasan_input:
                st.warning("Harap masukkan teks ulasan terlebih dahulu!")
            else:
                with st.spinner("Agen sedang membaca platform dan meracik draf kalimat..."):
                    try:
                        system_instruction = f"""
                        Anda adalah Agen AI Senior spesialis Manajemen Reputasi untuk bisnis bernama '{nama_bisnis}'.
                        Tugas Anda adalah meracik balasan ulasan/komentar pelanggan sesuai dengan karakteristik platform {platform}.
                        Panggilan untuk konsumen di semua platform wajib menggunakan kata 'Kakak'.
                        
                        Aturan Karakter Bahasa Platform:
                        - Google Maps: Bahasa sopan, formal-profesional, fokus pada terima kasih atau penyelesaian masalah.
                        - Instagram: Bahasa estetik, ramah, hangat, interaktif, dan gunakan beberapa emoji yang relevan.
                        - TikTok: Bahasa sangat kasual, gaul ala anak muda, singkat, santai, dan ekspresif.
                        - WhatsApp: Bahasa personal, responsif, berorientasi pada pelayanan langsung (Customer Service).
                        
                        Logika Kasus:
                        - Jika review POSITIF: Ucapkan terima kasih, sebutkan menu yang dipuji (jika ada), undang kembali secara halus.
                        - Jika review NEGATIF (atau Rating 1-3): Jangan defensif. Minta maaf dengan tulus atas nama manajemen. Arahkan untuk penyelesaian masalah via WA {wa_cs} atau IG @{ig_bisnis}.
                        
                        Output WAJIB berupa JSON dengan key:
                        {{
                          "sentiment": "POSITIF" atau "NEGATIF",
                          "reply_draft": "Isi teks balasan Anda di sini"
                        }}
                        """
                        
                        prompt = f"Platform: {platform}\nRating: {rating}/5\nTeks Masukan: '{ulasan_input}'"
                        
                        response = client.models.generate_content(
                            model='gemini-1.5-flash',
                            contents=prompt,
                            config=types.GenerateContentConfig(
                                system_instruction=system_instruction,
                                response_mime_type="application/json",
                                temperature=0.4
                            ),
                        )
                        
                        hasil_json = json.loads(response.text)
                        
                        st.subheader("🎉 Hasil Kerja Agen 1:")
                        if hasil_json.get("sentiment") == "POSITIF":
                            st.success(f"🟢 **Sentimen Terdeteksi:** {hasil_json.get('sentiment')}")
                        else:
                            st.error(f"🔴 **Sentimen Terdeteksi:** {hasil_json.get('sentiment')}")
                        
                        st.markdown("**Draf Kalimat Balasan:**")
                        st.info(hasil_json.get("reply_draft"))
                        
                        # FITUR PREMIUM TRIGGERS (ANTI-VIRAL REDIRECTION)
                        kata_fatal = ["basi", "kecoak", "kasar", "rambut", "ulat", "racun", "kecewa berat", "menyesal"]
                        if any(kata in ulasan_input.lower() for kata in kata_fatal) or rating <= 2:
                            st.divider()
                            st.markdown("### 💎 Paket Proteksi Premium Terdeteksi (Terkunci)")
                            st.warning("⚠️ **SISTEM ANTI-VIRAL DETECTED:** Ulasan ini mengandung isu operasional sensitif yang berpotensi memicu blunder publik.")
                            st.markdown(f"""
                            **Fitur Premium Terkunci:**
                            - **Draf Chat WhatsApp Jalur Privat:** Teks penawaran ganti rugi/kompensasi intern khusus dari Manager agar konsumen melunakkan amarahnya dan bersedia menghapus ulasan buruk secara damai.
                            - **Direct Link WA Routing:** Tombol otomatis untuk langsung membuka aplikasi WhatsApp dan mengirim draf kompensasi ke konsumen.
                            """)
                            st.button("🔓 Buka Fitur Premium (Langganan)", key="lock_a1_premium")
                            
                    except Exception as e:
                        st.error(f"Terjadi kesalahan teknis: {e}")

    # ==========================================
    # AGENT 2: EXECUTIVE ANALYTICS
    # ==========================================
    elif "Agent 2" in pilihan_agent:
        st.markdown("### 📊 Agent 2: Executive Analytics & Operational Auditor")
        st.write("**Fungsi:** Membedah kumpulan keluhan atau ulasan berkala untuk mengekstrak masalah operasional terbesar di dapur atau pelayanan sebagai bahan evaluasi manajemen.")
        st.caption("🟢 **Kuota Free Trial:** 2 kali analisis data teks per minggu.")
        
        data_ulasan_manual = st.text_area("Masukkan Kumpulan Ulasan/Komplain Konsumen Seminggu Terakhir (Pisahkan dengan baris baru):", placeholder="Ulasan 1: Pelayanannya lama banget kasirnya cemberut\nUlasan 2: AC lantai 2 bocor dan panas...")
        
        if st.button("🚀 Jalankan Agen 2", type="primary"):
            if not data_ulasan_manual:
                st.warning("Harap isi kumpulan teks ulasan terlebih dahulu!")
            else:
                with st.spinner("Agen sedang mengaudit masalah operasional..."):
                    try:
                        system_instruction = f"Anda adalah Auditor Bisnis internal untuk '{nama_bisnis}'. Bedah data keluhan yang diberikan, petakan masalah utamanya, dan berikan poin ringkas rekomendasi perbaikan untuk manajemen dapur/staf lapangan."
                        
                        response = client.models.generate_content(
                            model='gemini-1.5-flash',
                            contents=data_ulasan_manual,
                            config=types.GenerateContentConfig(system_instruction=system_instruction, temperature=0.2)
                        )
                        st.subheader("📋 Laporan Audit Masalah Operasional:")
                        st.markdown(response.text)
                        
                        # Kunci Premium Bulk Upload
                        st.divider()
                        st.error("🔒 FITUR BULK UPLOAD EXCEL / GRAPHIC REPORT TERKUNCI")
                        st.write("Di paket premium, Anda cukup mengunggah file .XLSX / .CSV hasil ekspor data ulasan Google Maps selama sebulan. AI akan langsung memproses ribuan data secara instan dan menampilkan grafik diagram batang otomatis untuk bahan rapat direksi.")
                        st.file_uploader("Upload Data Excel Bulanan (.xlsx / .csv):", disabled=True)
                        st.button("🔓 Upgrade untuk Buka Bulk Upload & Grafik PDF", key="lock_a2")
                    except Exception as e:
                        st.error(f"Terjadi kesalahan: {e}")

    # ==========================================
    # AGENT 3: CREATIVE CAMPAIGN & EVENT DIRECTOR
    # ==========================================
    elif "Agent 3" in pilihan_agent:
        st.markdown("### 🎸 Agent 3: The Creative Campaign & Event Director")
        st.write("**Fungsi:** Merancang konsep event kreatif, taktik promosi, dan *gimmick* khusus untuk meramaikan cafe pada hari kerja (*weekdays*) seperti event *live music* harian.")
        st.caption("🟢 **Kuota Free Trial:** 3 kali pembuatan konsep per minggu.")
        
        target_event = st.text_input("Apa Target Promosi / Event Anda?", placeholder="Contoh: Ngeramein hari Selasa malam pas jadwal Live Music akustik")
        
        if st.button("🚀 Jalankan Agen 3", type="primary"):
            if not target_event:
                st.warning("Masukkan target event promosi terlebih dahulu!")
            else:
                with st.spinner("Agen sedang menyusun konsep gimmick kreatif..."):
                    try:
                        system_instruction = f"Anda adalah Creative Director untuk '{nama_bisnis}'. Buatkan 1 ide konsep acara komplit beserta gimmick marketing interaktif anak muda agar target event tersebut ramai pengunjung."
                        response = client.models.generate_content(
                            model='gemini-1.5-flash',
                            contents=target_event,
                            config=types.GenerateContentConfig(system_instruction=system_instruction, temperature=0.6)
                        )
                        st.subheader("💡 Rekomendasi Konsep & Gimmick Event:")
                        st.markdown(response.text)
                        
                        st.divider()
                        st.error("🔒 FITUR LISENSI PREMIUM: FULL 30-DAYS CONTENT CALENDAR TERKUNCI")
                        st.write("Paket premium membuka akses pembuatan kalender konten media sosial utuh selama 30 hari penuh, lengkap dengan matriks target audiens (*Customer Persona*) dan strategi promo psikologis anti-boncos.")
                        st.button("🔓 Aktifkan Kalender Konten 30 Hari", key="lock_a3")
                    except Exception as e:
                        st.error(f"Terjadi kesalahan: {e}")

    # ==========================================
    # AGENT 4: HIGH-CONVERTING COPYWRITER
    # ==========================================
    elif "Agent 4" in pilihan_agent:
        st.markdown("### ✍️ Agent 4: The High-Converting Copywriter")
        st.write("**Fungsi:** Membuat teks tulisan iklan, skrip video Reels/TikTok, atau caption media sosial terstruktur menggunakan formula psikologi pemasaran.")
        st.caption("🟢 **Kuota Free Trial:** 5 kali pembuatan teks per hari.")
        
        jenis_copy = st.selectbox("Pilih Jenis Teks Copywriting:", ["Skrip Video TikTok/Reels (Storytelling)", "Caption Instagram Estetik", "Template Jawaban Otomatis (FAQ CS)"])
        bahan_promo = st.text_input("Menu / Promo Apa yang Ingin Diangkat?", placeholder="Contoh: Menu baru Matcha Espresso Latte, promo Buy 1 Get 1 khusus hari Jumat")
        
        if st.button("🚀 Jalankan Agen 4", type="primary"):
            if not bahan_promo:
                st.warning("Masukkan bahan menu/promo terlebih dahulu!")
            else:
                with st.spinner("Agen sedang merangkai kata promosi..."):
                    try:
                        system_instruction = f"Anda adalah Senior Copywriter untuk '{nama_bisnis}'. Buatkan teks {jenis_copy} terstruktur menggunakan formula AIDA (Attention, Interest, Desire, Action), penuh emoji menarik, dan gaya bahasa kasual anak muda."
                        response = client.models.generate_content(
                            model='gemini-1.5-flash',
                            contents=bahan_promo,
                            config=types.GenerateContentConfig(system_instruction=system_instruction, temperature=0.7)
                        )
                        st.subheader("📝 Hasil Teks Copywriting:")
                        st.markdown(response.text)
                        
                        st.divider()
                        st.error("🔒 FITUR PREMIUM: SEO COMPETITOR KEYWORD STEALER TERKUNCI")
                        st.write("Fitur premium membedah algoritma kata kunci tersembunyi yang digunakan oleh kompetitor Anda di Google Maps, GrabFood, atau GoFood agar posisi toko Anda melesat ke urutan paling atas pencarian.")
                        st.button("🔓 Buka Fitur Mata-Mata SEO Premium", key="lock_a4")
                    except Exception as e:
                        st.error(f"Terjadi kesalahan: {e}")

    # ==========================================
    # AGENT 5: AUTOMATED GRAPHIC DESIGNER
    # ==========================================
    elif "Agent 5" in pilihan_agent:
        st.markdown("### 🎨 Agent 5: The Automated Graphic Designer")
        st.write("**Fungsi:** Menyusun panduan estetika visual, tata letak objek, rekomendasi warna, dan teks instruksi (*Master Prompt*) untuk membuat poster promosi atau banner menu.")
        st.caption("🟢 **Kuota Free Trial:** 2 kali pakai per minggu.")
        
        tema_desain = st.text_input("Judul / Tema Poster Promosi yang Ingin Dibuat:", placeholder="Contoh: Poster Promo Jumat Berkah Diskon 20% Semua Varian Kopi")
        
        if st.button("🚀 Jalankan Agen 5", type="primary"):
            if not tema_desain:
                st.warning("Masukkan tema desain poster terlebih dahulu!")
            else:
                with st.spinner("Agen sedang merancang brief arsitektur visual..."):
                    try:
                        system_instruction = "Anda adalah Art Director senior. Buatkan brief desain poster promosi yang sangat detail meliputi: rekomendasi palet warna (hex code), jenis font yang cocok, tata letak komposisi objek gambar, dan ditutup dengan teks 'Master Prompt' berbahasa Inggris untuk dimasukkan ke AI generator gambar."
                        response = client.models.generate_content(
                            model='gemini-1.5-flash',
                            contents=tema_desain,
                            config=types.GenerateContentConfig(system_instruction=system_instruction, temperature=0.5)
                        )
                        st.subheader("📋 Brief & Panduan Produksi Visual:")
                        st.markdown(response.text)
                        
                        st.divider()
                        st.error("🔒 FITUR PREMIUM: INSTANT PYTHON GRAPHIC ENGINE TERKUNCI")
                        st.write("Di paket premium, Agen tidak hanya memberikan teks panduan, melainkan sistem akan langsung otomatis mencetak gambar poster berformat PNG/JPG jadi menggunakan library grafis Python secara instan sekali klik tanpa software tambahan.")
                        st.button("🔓 Aktifkan Engine Cetak Gambar Otomatis", key="lock_a5")
                    except Exception as e:
                        st.error(f"Terjadi kesalahan: {e}")

    # ==========================================
    # AGENT 6: AUTOMATION & WORKFLOW COPILOT
    # ==========================================
    elif "Agent 6" in pilihan_agent:
        st.markdown("### ⚙️ Agent 6: The Automation & Workflow Copilot")
        st.write("**Fungsi:** Merancang bagan logika alur kerja otomatisasi data antar aplikasi (seperti ManyChat, Zapier, Google Sheets) untuk menghilangkan kerja manual admin toko.")
        st.caption("🟢 **Kuota Free Trial:** 3 kali rancang per minggu.")
        
        alur_manual = st.text_area("Deskripsikan Alur Kerja Manual yang Ingin Diotomatisasikan:", placeholder="Contoh: Kalau ada konsumen isi form pendaftaran di iklan Instagram, datanya harus otomatis masuk ke Google Sheets dan kirim pesan WA ke HP saya.")
        
        if st.button("🚀 Jalankan Agen 6", type="primary"):
            if not alur_manual:
                st.warning("Deskripsikan dulu alur kerjanya, bro!")
            else:
                with st.spinner("Agen sedang merancang logika otomatisasi..."):
                    try:
                        system_instruction = "Anda adalah Automation Engineer. Buatkan panduan arsitektur logika alur kerja (flowchart langkah demi langkah) untuk menyambungkan aplikasi yang diminta oleh user menggunakan tools otomatisasi seperti Zapier/Make agar berjalan tanpa eror."
                        response = client.models.generate_content(
                            model='gemini-1.5-flash',
                            contents=alur_manual,
                            config=types.GenerateContentConfig(system_instruction=system_instruction, temperature=0.3)
                        )
                        st.subheader("🔗 Rekomendasi Logika Alur Otomatisasi (Workflow):")
                        st.markdown(response.text)
                        
                        st.divider()
                        st.error("🔒 FITUR PREMIUM: CUSTOM WEBHOOK & API SCRIPT INJECTION TERKUNCI")
                        st.write("Fitur premium menyediakan kode skrip Webhook dan API kustom siap pakai yang bisa langsung di-inject ke sistem internal bisnis Anda untuk otomatisasi tanpa biaya langganan aplikasi pihak ketiga.")
                        st.button("🔓 Buka Akses Skrip API Kustom", key="lock_a6")
                    except Exception as e:
                        st.error(f"Terjadi kesalahan: {e}")

    # ==========================================
    # AGENT 7: MARKET INTELLIGENCE & COMPETITOR SPY
    # ==========================================
    elif "Agent 7" in pilihan_agent:
        st.markdown("### 🕵️‍♂️ Agent 7: The Market Intelligence & Competitor Spy")
        st.write("**Fungsi:** Menembus live internet secara real-time menggunakan Google Search Grounding untuk meriset tren kopi/kuliner terkini atau membedah taktik promosi kompetitor.")
        st.caption("🟢 **Kuota Free Trial:** 3 kali riset live internet per minggu.")
        
        kueri_tren = st.text_input("Tulis Tren / Nama Kompetitor yang Ingin Diriset secara Live:", placeholder="Contoh: Tren menu kopi susu viral di Indonesia saat ini")
        
        if st.button("🚀 Jalankan Agen 7", type="primary"):
            if not kueri_tren:
                st.warning("Masukkan topik riset live terlebih dahulu!")
            else:
                with st.spinner("Agen sedang melakukan browsing internet secara real-time..."):
                    try:
                        # Mengaktifkan Google Search Grounding bawaan Gemini terbaru
                        config = types.GenerateContentConfig(
                            system_instruction=f"Anda adalah Agen Riset Pasar Senior untuk industri F&B. Lakukan analisis mendalam berdasarkan data terbaru dari internet terkait kueri yang dicari user untuk bisnis '{nama_bisnis}'.",
                            temperature=0.4,
                            tools=[types.Tool(google_search=types.GoogleSearch())]
                        )
                        
                        response = client.models.generate_content(
                            model='gemini-1.5-flash',
                            contents=kueri_tren,
                            config=config
                        )
                        
                        st.subheader("🌐 Hasil Riset Tren & Intelijen Pasar Terkini:")
                        st.markdown(response.text)
                        
                        st.divider()
                        st.error("🔒 FITUR PREMIUM: COMPETITOR WEAKNESS COUNTER-MARKETING TERKUNCI")
                        st.write("Fitur premium akan otomatis melacak ulasan buruk terbesar dari seluruh kompetitor terdekat Anda di internet, memetakan kelemahan operasional mereka, dan meracik draf materi iklan serang untuk merebut konsumen mereka.")
                        st.button("🔓 Buka Akses Counter-Marketing Premium", key="lock_a7")
                    except Exception as e:
                        st.error(f"Terjadi kesalahan riset internet: {e}")

elif password_input != "":
    st.error("❌ Password salah! Silakan periksa kembali token akses Anda.")
