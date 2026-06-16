# knowledge_base.py

# 1. Daftar Gejala Klinis
GEJALA = {
    "G1": "Sering merasa haus yang berlebihan (Polidipsia)",
    "G2": "Sering buang air kecil, terutama di malam hari (Poliuria)",
    "G3": "Sering merasa lapar yang ekstrem (Polifagia)",
    "G4": "Penurunan berat badan drastis tanpa sebab yang jelas",
    "G5": "Luka yang lambat sembuh atau sering terjadi infeksi",
    "G6": "Pandangan kabur atau buram secara mendadak",
    "G7": "Kesemutan, mati rasa, atau nyeri pada tangan/kaki",
    "G8": "Sedang dalam kondisi kehamilan",
    "G9": "Memiliki riwayat keluarga kandung yang mengidap diabetes"
}

# 2. Multi-Rule Base (Dipecah agar rumus CF Kombinasi aktif secara valid)
ATURAN = [
    # Aturan untuk Diabetes Melitus Tipe 1
    {"id": "R1", "gejala": ["G1", "G2"], "diagnosa": "Diabetes Melitus Tipe 1", "cf_pakar": 0.70},
    {"id": "R2", "gejala": ["G3", "G4"], "diagnosa": "Diabetes Melitus Tipe 1", "cf_pakar": 0.65},
    
    # Aturan untuk Diabetes Melitus Tipe 2
    {"id": "R3", "gejala": ["G1", "G2"], "diagnosa": "Diabetes Melitus Tipe 2", "cf_pakar": 0.60},
    {"id": "R4", "gejala": ["G5", "G7"], "diagnosa": "Diabetes Melitus Tipe 2", "cf_pakar": 0.75},
    
    # Aturan untuk Diabetes Gestasional
    {"id": "R5", "gejala": ["G1", "G2"], "diagnosa": "Diabetes Gestasional", "cf_pakar": 0.55},
    {"id": "R6", "gejala": ["G8"],       "diagnosa": "Diabetes Gestasional", "cf_pakar": 0.85},
    
    # Aturan untuk Prediabetes
    {"id": "R7", "gejala": ["G3", "G6"], "diagnosa": "Prediabetes", "cf_pakar": 0.50},
    {"id": "R8", "gejala": ["G9"],       "diagnosa": "Prediabetes", "cf_pakar": 0.60}
]

# 3. Opsi Jawaban Skala Likert (Menggantikan Ya/Tidak yang kaku)
SKALA_KEYAKINAN = {
    "Tidak Mengalami / Tidak Tahu": 0.0,
    "Sedikit Yakin": 0.4,
    "Cukup Yakin": 0.6,
    "Yakin": 0.8,
    "Sangat Yakin": 1.0
}

# 4. Rekomendasi/Saran Medis Terintegrasi
SARAN = {
    "Diabetes Melitus Tipe 1": "Segera konsultasikan dengan dokter spesialis endokrin. Kondisi ini memerlukan terapi insulin intensif dan pemantauan kadar gula darah secara berkala.",
    "Diabetes Melitus Tipe 2": "Terapkan pola makan rendah karbohidrat, rutin berolahraga minimal 150 menit seminggu, dan konsultasikan ke dokter untuk peresepan obat metformin atau terapi edukasi mandiri.",
    "Diabetes Gestasional": "Lakukan pemantauan ketat dengan dokter kandungan dan ahli gizi. Jaga pola makan untuk melindungi kesehatan ibu dan janin.",
    "Prediabetes": "Ubah gaya hidup segera. Batasi konsumsi gula, turunkan berat badan jika berlebih, dan lakukan cek gula darah puasa minimal 6 bulan sekali untuk mencegah progresi menjadi diabetes."
}