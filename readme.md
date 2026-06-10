# 📚 Tugas Akhir Jaringan Saraf Tiruan (JST)
## VibeSync: Social Battery & Mood Optimizer

Aplikasi asisten interaktif berbasis web untuk memantau kapasitas sosial (*Social Battery*) dan mengklasifikasikan suasana hati (*Mood Vibe*) harian menggunakan dua model Jaringan Saraf Tiruan (JST) yang dibangun dari nol (*from scratch*) menggunakan **NumPy**.

---

### 👤 Identitas Mahasiswa
* **Nama:** Muhammad Abday Abdul Hafidz
* **NIM:** 1123150093
* **Kelas:** TI-23-SE-1
* **Program Studi:** Rekayasa Perangkat Lunak / Teknik Informatika

---

## 📂 1. Deskripsi Proyek
Dalam ritme kehidupan akademis dan profesional yang padat, mahasiswa sering kali mengalami kelelahan sosial (*social burnout*) tanpa menyadari penurunan kapasitas mental mereka. **VibeSync** hadir sebagai asisten cerdas yang memecahkan masalah ini dengan mengombinasikan dua metode JST untuk analisis harian:

1. **Prediksi Kelelahan Sosial (Social Battery):** Menggunakan model **Adaline** untuk memprediksi apakah pengguna berada dalam kondisi prima (**Energized**) atau perlu istirahat (**Drained**) berdasarkan jam tidur, jam bersosialisasi, beban tugas, dan jam me-time.
2. **Klasifikasi Suasana Hati (Mood Vibe):** Menggunakan model **Learning Vector Quantization (LVQ)** untuk mengklasifikasikan kondisi emosional internal pengguna ke dalam 4 profil mood (*Focused, Calm, Stressed, atau Exhausted*) berdasarkan tingkat energi fisik, hasrat bersosialisasi, dan fokus kognitif.

Aplikasi ini dilengkapi dengan visualisasi kurva konvergensi latihan, perbandingan performa laju pembelajaran (*learning rate*), batas keputusan (*decision boundary*) 2D interaktif, serta visualisasi pemetaan koordinat 3D vektor prototipe mood secara real-time.

---

## 🛠️ 2. Arsitektur & Spesifikasi Model JST

### 2.1 Model 1: Adaline (Adaptive Linear Neuron)
Adaline adalah jaringan saraf lapis tunggal yang menggunakan fungsi aktivasi linear selama proses pelatihan dan memperbarui bobotnya menggunakan aturan kuadrat terkecil (*Least Mean Squares* / LMS atau aturan Delta).
* **Input Layer:** 4 neuron input ($x_1$: Kualitas Tidur, $x_2$: Jam Bersosialisasi, $x_3$: Jumlah Tugas Kerja, $x_4$: Jam Me-Time).
* **Output Layer:** 1 neuron output bipolar ($+1$ untuk *Energized* dan $-1$ untuk *Drained*).
* **Persamaan Forward Pass (Net Input):**
  $$net = \sum_{i=1}^{n} (x_i \cdot w_i) + b$$
* **Pembaruan Bobot & Bias (Aturan Delta):**
  $$w_i^{(baru)} = w_i^{(lama)} + \frac{\eta}{N} \cdot (y - net) \cdot x_i$$
  $$b^{(baru)} = b^{(lama)} + \frac{\eta}{N} \cdot \sum (y - net)$$
  *Dimana $\eta$ adalah learning rate dan $N$ adalah jumlah sampel data.*

### 2.2 Model 2: Learning Vector Quantization (LVQ)
LVQ adalah metode pembelajaran terawasi (*supervised competitive learning*) yang membagi ruang input ke dalam beberapa kelas menggunakan vektor prototipe (kodebook).
* **Input Layer:** 3 neuron input ($x_1$: Energi Fisik, $x_2$: Hasrat Bersosialisasi, $x_3$: Fokus Mental).
* **Output Layer (Prototipe):** 4 neuron kelas representatif:
  * **Kelas 0:** *Energetic & Focused* (Warna Kuning)
  * **Kelas 1:** *Calm & Chill* (Warna Sian)
  * **Kelas 2:** *Anxious & Stressed* (Warna Oranye)
  * **Kelas 3:** *Exhausted & Gloomy* (Warna Ungu)
* **Kriteria Pemenang (BMU - Best Matching Unit):** Memilih prototipe $W_c$ dengan jarak Euclidean terkecil ke input $x$:
  $$d(x, W_j) = \sqrt{\sum_{i=1}^{3} (x_i - w_{ji})^2}$$
* **Pembaruan Bobot Prototipe Pemenang ($W_c$):**
  * Jika kelas prototipe pemenang sesuai dengan kelas target ($T_c == y$):
    $$W_c^{(baru)} = W_c^{(lama)} + \alpha \cdot (x - W_c^{(lama)})$$
  * Jika kelas prototipe pemenang tidak sesuai dengan kelas target ($T_c \neq y$):
    $$W_c^{(baru)} = W_c^{(lama)} - \alpha \cdot (x - W_c^{(lama)})$$

---

## 🚀 3. Panduan Penggunaan & Cara Menjalankan

### Langkah 1: Persiapan Lingkungan (Environment Setup)
Buka terminal dan arahkan ke folder proyek:
```bash
cd C:\Users\LENOVO\uas_jst
```
Aktifkan virtual environment yang sudah tersedia di Windows:
* **PowerShell:**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
* **Command Prompt (CMD):**
  ```cmd
  .\venv\Scripts\activate.bat
  ```

### Langkah 2: Instalasi Dependensi
Pastikan semua library terinstal dengan benar:
```bash
pip install -r requirements.txt
```

### Langkah 3: Menjalankan Aplikasi
Jalankan dashboard Streamlit dengan perintah:
```bash
streamlit run app.py
```
Aplikasi akan otomatis terbuka di browser pada alamat: **`http://localhost:8501`**

---

## 📐 4. Pembahasan Matematika: Contoh Perhitungan Manual (UAS Bab III)

### 4.1 Perhitungan Manual Satu Iterasi Adaline
* **Parameter Awal:**
  - Input: $x = [0.8, 0.4, 0.2, 0.9]$
  - Target: $y = 1$ (Energized)
  - Bobot Awal: $W = [0.1, -0.2, 0.15, 0.3]^T$
  - Bias Awal: $b = 0.05$
  - Learning Rate ($\eta$): $0.1$

1. **Forward Pass (Net Input):**
   $$net = (0.8 \cdot 0.1) + (0.4 \cdot -0.2) + (0.2 \cdot 0.15) + (0.9 \cdot 0.3) + 0.05$$
   $$net = 0.08 - 0.08 + 0.03 + 0.27 + 0.05 = 0.35$$
2. **Kalkulasi Error:**
   $$E = y - net = 1 - 0.35 = 0.65$$
3. **Pembaruan Bobot & Bias ($\Delta w_i = \eta \cdot E \cdot x_i$):**
   - $w_1^{(baru)} = 0.1 + (0.1 \cdot 0.65 \cdot 0.8) = 0.1 + 0.052 = 0.152$
   - $w_2^{(baru)} = -0.2 + (0.1 \cdot 0.65 \cdot 0.4) = -0.2 + 0.026 = -0.174$
   - $w_3^{(baru)} = 0.15 + (0.1 \cdot 0.65 \cdot 0.2) = 0.15 + 0.013 = 0.163$
   - $w_4^{(baru)} = 0.3 + (0.1 \cdot 0.65 \cdot 0.9) = 0.3 + 0.0585 = 0.3585$
   - $b^{(baru)} = 0.05 + (0.1 \cdot 0.65) = 0.05 + 0.065 = 0.115$

---

### 4.2 Perhitungan Manual Satu Iterasi LVQ
* **Parameter Awal:**
  - Vektor Input: $x = [0.7, 0.3, 0.8]$ dengan Label Target $y = 0$
  - Prototipe Awal:
    - $W_0 = [0.6, 0.2, 0.7]$ (Kelas 0)
    - $W_1 = [0.3, 0.8, 0.4]$ (Kelas 1)
    - $W_2 = [0.5, 0.4, 0.9]$ (Kelas 2)
    - $W_3 = [0.1, 0.1, 0.2]$ (Kelas 3)
  - Learning Rate ($\alpha$): $0.5$

1. **Hitung Jarak Euclidean ke Seluruh Prototipe:**
   - $d(x, W_0) = \sqrt{(0.7-0.6)^2 + (0.3-0.2)^2 + (0.8-0.7)^2} = \sqrt{0.03} \approx 0.1732$
   - $d(x, W_1) = \sqrt{(0.7-0.3)^2 + (0.3-0.8)^2 + (0.8-0.4)^2} = \sqrt{0.57} \approx 0.7550$
   - $d(x, W_2) = \sqrt{(0.7-0.5)^2 + (0.3-0.4)^2 + (0.8-0.9)^2} = \sqrt{0.06} \approx 0.2449$
   - $d(x, W_3) = \sqrt{(0.7-0.1)^2 + (0.3-0.1)^2 + (0.8-0.2)^2} = \sqrt{0.76} \approx 0.8718$

   *BMU adalah $W_0$ karena memiliki jarak terkecil ($0.1732$) ke input.*

2. **Pembaruan Bobot BMU:**
   Karena label kelas $W_0$ (yaitu 0) sama dengan label target ($y = 0$), maka prototipe bergeser mendekati input:
   $$W_0^{(baru)} = W_0 + \alpha \cdot (x - W_0)$$
   $$W_0^{(baru)} = [0.6, 0.2, 0.7] + 0.5 \cdot ([0.7, 0.3, 0.8] - [0.6, 0.2, 0.7])$$
   $$W_0^{(baru)} = [0.6, 0.2, 0.7] + [0.05, 0.05, 0.05] = [0.65, 0.25, 0.75]$$

---

## 🔬 5. Hasil Analisis Pengaruh Parameter (UAS Bab IV)
Pelatihan model Adaline dengan variasi *learning rate* ($\eta$) memberikan wawasan penting tentang konvergensi bobot:
* **$\eta = 0.01$ (Terlalu Kecil):** Model stabil, namun laju penurunan MSE sangat lambat. Butuh epoch yang jauh lebih banyak untuk mencapai titik konvergensi minimum.
* **$\eta = 0.1$ (Optimal):** Model berkonvergensi dengan cepat menuju nilai minimum global tanpa osilasi yang berarti. Ini adalah parameter default yang digunakan.
* **$\eta = 0.5$ (Terlalu Besar):** Langkah pembaruan bobot melompati titik minimum global. Grafik MSE menunjukkan osilasi naik-turun yang ekstrem dan tidak pernah stabil.