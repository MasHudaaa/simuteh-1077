# SIMUTEH - Sistem Pemeriksaan Mutu Daun Teh
**Evaluasi Praktikum P1-P4 (Computer Vision)**

## 📌 Identitas Mahasiswa
- **Nama**: [Samsul Huda]
- **NIM**: [2330511077]
- **SEED Data**: `1077`
- **Git Tag**: `v0.1-praproses`
- **Repository**: [https://github.com/MasHudaaa/simuteh-1077](https://github.com/MasHudaaa/simuteh-1077)

---

## 🌿 Ringkasan Proyek
SIMUTEH (*Sistem Pemeriksaan Mutu Daun Teh*) adalah sistem berbasis Computer Vision konvensional untuk melakukan kualifikasi mutu daun teh dan deteksi bercak penyakit secara otomatis. Sistem ini dirancang untuk mengatasi masalah pencahayaan tidak merata, derau citra, dan pencahayaan latar belakang pada lingkungan perkebunan.

---

## ⚙️ Pipeline Praproses Citra
1. **Penyelarasan Ukuran**: Resizing citra input ke skala standar 640px.
2. **Perbaikan Kontras**: Penerapan CLAHE (*Contrast Limited Adaptive Histogram Equalization*) pada kanal V (Model Warna HSV).
3. **Penapisan Derau**: Filter Median 3x3 untuk mengeliminasi derau *salt-and-pepper* tanpa mengaburkan tepi bercak daun.

---

## 📊 Hasil Evaluasi Utama
- **Peningkatan Kontras Berkas (KB)**: Terjadi kenaikan rata-rata sebesar **+37.6%** setelah tahap praproses.
- **Visualisasi**: Seluruh grafik histogram, perbandingan kanal warna, dan pengujian bercak palsu tersimpan pada folder `hasil/`.

---

## 📁 Struktur Repositori
```text
simuteh-1077/
├── notebook/      # Notebook eksperimen B1 s.d. B5 (.ipynb)
├── src/           # Skrip utama Python (buat_dataset_sintetis.py, utils_cv.py, praproses.py)
├── hasil/         # Gambar visualisasi & file CSV hasil evaluasi
├── README.md      # Dokumentasi repositori
└── requirements.txt # Daftar pustaka Python
