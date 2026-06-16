# app.py
import streamlit as st
# Mengimpor basis pengetahuan dari berkas terpisah (Separation of Concerns)
from knowledge_base import GEJALA, ATURAN, SKALA_KEYAKINAN, SARAN

# ==========================================
# 1. KONFIGURASI HALAMAN & STYLE DESAIN (CSS)
# ==========================================
st.set_page_config(
    page_title="DiaBetic.AI - Premium Expert System", 
    page_icon="🩺", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    .hero-container {
        background: linear-gradient(rgba(30, 58, 138, 0.85), rgba(59, 130, 246, 0.85)), 
                    url('https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=1600&q=80');
        background-size: cover;
        background-position: center;
        padding: 80px 40px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 40px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
    }
    .hero-title {
        font-size: 3.2rem;
        font-weight: 800;
        margin-bottom: 12px;
        letter-spacing: -1px;
    }
    .hero-subtitle {
        font-size: 1.25rem;
        opacity: 0.95;
        max-width: 750px;
        margin: 0 auto 25px auto;
    }
    .feature-card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        text-align: center;
        height: 100%;
    }
    .test-box {
        background-color: #F9FAFB;
        padding: 40px;
        border-radius: 20px;
        border: 1px solid #E5E7EB;
        margin-top: 30px;
    }
    
    /* Menargetkan komponen grup radio */
    div[data-testid="stRadio"] {
        display: flex;
        justify-content: center !important;
        align-items: center !important;
        text-align: center !important;
        width: 100% !important;
    }
    /* Menargetkan kontainer baris di dalam objek radio horizontal */
    div[data-testid="stRadio"] > role-parameter, 
    div[data-testid="stRadio"] > div[role="radiogroup"] {
        display: flex !important;
        justify-content: center !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        gap: 20px !important;
        width: 100% !important;
    }
    /* Menargetkan elemen label teks di dalam masing-masing pilihan */
    div[data-testid="stRadio"] label {
        justify-content: center !important;
        text-align: center !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. HERO SECTION & FEATURE CARDS (LANDING PAGE)
# ==========================================
st.markdown("""
    <div class="hero-container">
        <div class="hero-title">🩺 DiaBetic.AI</div>
        <div class="hero-subtitle">Sistem Pakar Deteksi Dini Diabetes Tingkat Lanjut Menggunakan Metode Certainty Factor dengan Skala Likert Eksakta.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: #1F2937; margin-bottom: 25px;'>Keunggulan Arsitektur DiaBetic.AI</h3>", unsafe_allow_html=True)
col_f1, col_f2, col_f3 = st.columns(3)

with col_f1:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">⏱️</div>
            <div class="feature-title">Skala Likert Dinamis</div>
            <div class="feature-desc">Mengakomodasi tingkat keraguan gejala klinis pengguna untuk hasil kalkulasi yang jauh lebih personal dan realistis.</div>
        </div>
        """, unsafe_allow_html=True)

with col_f2:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🧮</div>
            <div class="feature-title">Multi-Rule Inference Engine</div>
            <div class="feature-desc">Menerapkan pencocokan multi-aturan secara simultan menggunakan rumus kombinasi kepastian linier.</div>
        </div>
        """, unsafe_allow_html=True)

with col_f3:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🗄️</div>
            <div class="feature-title">Modular Architecture</div>
            <div class="feature-desc">Pemisahan penuh antara data basis pengetahuan dengan mesin inferensi utama sesuai standar software engineer.</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><hr>", unsafe_allow_html=True)

# ==========================================
# 3. KUESIONER INTERAKTIF (SINGLE FORM APPROACH)
# ==========================================
st.markdown("<h3 style='text-align: center; color: #1F2937;'>Formulir Evaluasi Gejala Kesehatan</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6B7280; margin-bottom: 30px;'>Silakan tentukan tingkat keyakinan Anda terhadap kondisi klinis di bawah ini.</p>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="test-box">', unsafe_allow_html=True)
    
    with st.form("form_pemeriksaan"):
        user_responses = {}
        
        for kode, deskripsi in GEJALA.items():
            # Menampilkan deskripsi pertanyaan tepat di tengah halaman
            st.markdown(f"<p style='color: #1E3A8A; font-weight: 600; margin-bottom: 5px; text-align: center;'>{deskripsi}</p>", unsafe_allow_html=True)
            
            # Input berupa horizontal radio button yang otomatis bergeser ke tengah berkat selektor CSS kustom di atas
            pilihan = st.radio(
                label=f"Pilihan untuk {kode}",
                options=list(SKALA_KEYAKINAN.keys()),
                index=0,
                horizontal=True,
                label_visibility="collapsed",
                key=f"radio_{kode}"
            )
            user_responses[kode] = SKALA_KEYAKINAN[pilihan]
            st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        tombol_submit = st.form_submit_button("📊 Proses Analisis Diagnosis", type="primary", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # ==========================================
    # 4. ENGINE INFERENSI (CERTAINTY FACTOR KOMBINASI)
    # ==========================================
    if tombol_submit:
        st.markdown("<hr><h4 style='color: #1E3A8A; text-align: center; font-weight:700; margin-bottom: 25px;'>📊 Laporan Analisis Probabilitas Klinis</h4>", unsafe_allow_html=True)
        
        cf_aturan_aktif = {}
        
        for rule in ATURAN:
            cf_user_minimal = min([user_responses[g] for g in rule["gejala"]])
            
            if cf_user_minimal > 0:
                cf_hitung = rule["cf_pakar"] * cf_user_minimal
                nama_diagnosa = rule["diagnosa"]
                
                if nama_diagnosa not in cf_aturan_aktif:
                    cf_aturan_aktif[nama_diagnosa] = []
                cf_aturan_aktif[nama_diagnosa].append(cf_hitung)

        hasil_final_cf = {}
        
        for diagnosa, daftar_cf in cf_aturan_aktif.items():
            cf_kombinasi = daftar_cf[0]
            for cf_berikutnya in daftar_cf[1:]:
                cf_kombinasi = cf_kombinasi + cf_berikutnya * (1 - cf_kombinasi)
            hasil_final_cf[diagnosa] = cf_kombinasi

        # ==========================================
        # 5. OUTPUT DISPLAY & REKOMENDASI MEDIS
        # ==========================================
        if hasil_final_cf:
            hasil_urut = sorted(hasil_final_cf.items(), key=lambda x: x[1], reverse=True)
            diagnosa_utama, cf_tertinggi = hasil_urut[0]
            
            col_res1, col_res2 = st.columns([1, 1])
            with col_res1:
                st.toast("Kalkulasi inferensi berhasil!", icon='✨')
                st.metric(
                    label="Hasil Diagnosis Utama Terdeteksi", 
                    value=diagnosa_utama, 
                    delta=f"{cf_tertinggi * 100:.1f}% Tingkat Keyakinan Akumulatif"
                )
                
                st.write("**Daftar Diagnosis Diferensial (Urutan Probabilitas):**")
                for diagnosa, cf_nilai in hasil_urut:
                    st.caption(f"• {diagnosa}: Akumulasi Kepastian Aturan **{cf_nilai * 100:.1f}%**")
            
            with col_res2:
                st.markdown("<div style='background-color: #EFF6FF; padding: 25px; border-radius: 12px; border-left: 5px solid #3B82F6;'>", unsafe_allow_html=True)
                st.markdown(f"📋 **Rekomendasi Tindakan Klinis:**<br><span style='font-size: 0.95rem; color: #1E3A8A; line-height: 1.5;'>{SARAN[diagnosa_utama]}</span>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.info("💡 **Kesimpulan Akhir:** Berdasarkan parameter data input, tidak ada klaster konjungsi aturan gejala yang terpenuhi secara signifikan. Anda terindikasi berada pada kondisi sehat atau bebas dari risiko diabetes utama.")

    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 6. FOOTER LANDING PAGE
# ==========================================
st.markdown("""
    <br><br>
    <div style='text-align: center; color: #9CA3AF; font-size: 0.85rem;'>
        © 2026 DiaBetic.AI. Pengembangan Sistem Pakar Artificial Intelligence — Fakultas Dakwah dan Ilmu Komunikasi.<br>
        <span style='color: #EF4444;'>Peringatan Akademik:</span> Aplikasi ini bekerja berdasarkan penalaran kaidah matematika eksakta Certainty Factor untuk keperluan purwarupa akademis, pengujian laboratorium medis sungguhan tetap mutlak diperlukan.
    </div>
    """, unsafe_allow_html=True)