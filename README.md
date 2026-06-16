# DiaBetic.AI: Premium Expert System for Early Diabetes Detection

[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/framework-Streamlit-FF4B4B)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

DiaBetic.AI adalah sebuah purwarupa sistem pakar (*expert system*) berbasis kecerdasan buatan konvensional yang dirancang untuk melakukan deteksi dini komparatif terhadap empat klasifikasi diabetes: Diabetes Melitus Tipe 1, Diabetes Melitus Tipe 2, Diabetes Gestasional, dan Prediabetes[cite: 2]. Sistem ini mengimplementasikan metode **Certainty Factor (CF)** dengan mengadopsi variabel input berbasis **Skala Likert Eksakta** untuk mengakomodasi ambiguitas atau batasan keyakinan (*uncertainty*) diagnosis klinis dari sisi pengguna[cite: 1, 2].

## 1. Landasan Teoretis & Metodologi

Sistem ini menyelesaikan konflik ketidakpastian medis dengan menggunakan kalkulasi kepastian linier. Proses penalaran (*inference engine*) mengeksekusi dua tahapan matematis secara simultan:

### A. Aturan Tunggal (Inference Rule)
Menghitung nilai kepastian dari kombinasi gejala tunggal berdasarkan bobot kepastian pakar ($CF_{\text{pakar}}$) dan bobot keyakinan pengguna ($CF_{\text{user}}$):

$$CF_{\text{hitung}}(H,E) = CF_{\text{pakar}}(H) \times \min(CF_{\text{user}}(E_1), CF_{\text{user}}(E_2), \dots, CF_{\text{user}}(E_n))$$

### B. Rumus Kombinasi (Combining Certainty Factors)
Jika sebuah klaster diagnosis dipicu oleh lebih dari satu aturan (*multi-rule*), nilai akumulasi akhir dihitung menggunakan fungsi kombinasi sekansial[cite: 1, 2]:

$$CF_{\text{combine}}(CF_1, CF_2) = CF_1 + CF_2 \times (1 - CF_1)$$

Proses ini diulang secara iteratif untuk seluruh bobot $CF$ aktif guna menghasilkan urutan diagnosis diferensial berbasis probabilitas klinis tertinggi[cite: 1].

---

## 2. Arsitektur Perangkat Lunak

Aplikasi ini dirancang dengan prinsip **Separation of Concerns (SoC)** untuk memisahkan antara data pengetahuan statis dengan mesin inferensi eksekusi[cite: 1]:

*   `knowledge_base.py`: Bertindak sebagai *Knowledge Base* yang menyimpan representasi data berupa daftar gejala, aturan implikasi (*rule-base*), skala parameter Likert, dan rekomendasi medis[cite: 1, 2].
*   `app.py`: Bertindak sebagai *Inference Engine* sekaligus *User Interface* (UI) berbasis Streamlit yang mengelola visualisasi grafis dan kalkulasi kombinasi matematika[cite: 1].

---

## 3. Instalasi dan Deployment Lokal

### Prasyarat System
*   Python 3.9 ke atas
*   Pip (Python Package Installer)

### Langkah-Langkah Instalasi

1.  **Kloning Repositori:**
```bash
    git clone [https://github.com/USERNAME/NAMA-REPOSITORI.git](https://github.com/USERNAME/NAMA-REPOSITORI.git)
    cd NAMA-REPOSITORI
    ```

2.  **Isolasi Environment (Rekomendasi):**
```bash
    python -m venv .venv
    source .venv/bin/activate  # Untuk Linux/macOS
    .venv\Scripts\activate     # Untuk Windows
    ```

3.  **Instalasi Dependensi:**
```bash
    pip install -r requirements.txt
    ```

4.  **Eksekusi Aplikasi:**
```bash
    streamlit run app.py
    ```

---

## 4. Sumber Daya & Referensi Teknik

*   **UI/UX Framework:** Streamlit UI Components & Embedded Tailwind CSS Custom Blocks[cite: 1].
*   **Inference Method:** Shortliffe-Buchanan Certainty Factor Theory (1975).
*   **Dataset/Knowledge Source:** Representasi pengetahuan berbasis klasifikasi klinis diabetes umum[cite: 2].

---

## Disclaimer / Peringatan Akademik
Aplikasi ini dikembangkan murni sebagai purwarupa akademis untuk pengujian komputasi logika matematika sistem pakar[cite: 1]. Hasil keluaran kalkulasi tidak dapat dijadikan sebagai acuan final diagnosis medis mutlak tanpa adanya validasi laboratorium klinis atau konfirmasi formal dari tenaga medis/dokter spesialis terkait[cite: 1].
