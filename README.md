# SIMUTEH — Sistem Pemeriksaan Mutu Daun Teh Berbasis Citra

Repositori praktikum berkelanjutan mata kuliah **Computer Vision** (Program Studi Teknik Informatika, Universitas Muhammadiyah Sukabumi).

- **NIM / SEED Dataset:** `2330511077` / `SEED = 1077`
- **Status Rilis:**
  - `v0.1-praproses`: Rangkaian praproses citra (`src/praproses.py`, `hasil/param_praproses.json`)
  - `v0.2-tepi`: Evaluasi deteksi tepi Sobel, Prewitt, LoG, dan Canny persentil (`notebook/P5_tepi.ipynb`, `src/utils_tepi.py`)
  - `v0.3-morfologi`: Operasi morfologi biner, analisis komponen terhubung, dan modul analisis bercak (`notebook/P6_morfologi.ipynb`, `src/bercak.py`, `hasil/param_bercak.json`)

## Ringkasan Hasil Pertemuan 5–6
1. **Deteksi Tepi (`v0.2-tepi`):** Kanal `R` menghasilkan `0,0` piksel tepi palsu tulang daun pada seluruh kondisi cahaya daun sehat (dibandingkan `846,5` piksel pada kanal `Gray` kondisi bayangan). Gradien morfologi dari mask daun menghasilkan batas daun yang lebih utuh pada citra kontras rendah.
2. **Morfologi & Analisis Bercak (`v0.3-morfologi`):**
   - Kombinasi terbaik: ambang `median + 4.0 * MAD` pada kanal `R`, diikuti *opening* dan *closing* dengan SE `elips 5x5`, serta penyaringan komponen terhubung (`luas >= 20 px`, `kebulatan >= 0.5`, `rasio_aspek <= 1.8`).
   - Evaluasi pada 60 citra menghasilkan **akurasi kelas `90,0%`**, **korelasi luas `0,955`**, dan **galat absolut rerata `0,450%`**.

## Cara Menggunakan Modul `src/bercak.py`
~~~python
import json, cv2
from src.praproses import praproses
from src.bercak import analisis_daun

param_pra = json.load(open("hasil/param_praproses.json"))
param_bercak = json.load(open("hasil/param_bercak.json"))

img = cv2.imread("data/sintetis/citra/teh_041.png")
img_bersih = praproses(img, param_pra)
hasil = analisis_daun(img_bersih, param_bercak)

print(hasil["kelas"], hasil["persen_bercak"], hasil["jumlah_bercak"])
~~~
