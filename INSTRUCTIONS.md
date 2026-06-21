#  SoundSync: Music Vibe & Genre Classifier - Panduan & Pembahasan Matematika

Dokumen ini berisi panduan menjalankan aplikasi dan penjelasan matematis lengkap untuk laporan Bab III dalam Bahasa Indonesia dengan studi kasus klasifikasi karakteristik dan genre musik.

---

##  1. Petunjuk Menjalankan Aplikasi

Ikuti langkah-langkah di bawah ini untuk menginstal dependensi dan menjalankan aplikasi dashboard **SoundSync**:

### Langkah 1: Persiapan Lingkungan (Environment Setup)
1. Buka terminal Anda (PowerShell, Command Prompt, atau Terminal VS Code).
2. Arahkan ke folder proyek ini:
   ```bash
   cd c:\Users\LENOVO\uas_jst
   ```
3. Aktifkan virtual environment:
   ```bash
   # Mengaktifkan venv di Windows (PowerShell)
   .\venv\Scripts\Activate.ps1
   # Atau jika menggunakan Command Prompt (cmd)
   .\venv\Scripts\activate.bat
   ```

### Langkah 2: Instalasi Library Pendukung
Pastikan library yang dibutuhkan terinstal dengan menjalankan:
```bash
pip install -r requirements.txt
```

### Langkah 3: Menjalankan Aplikasi Streamlit
Jalankan perintah berikut untuk membuka dashboard interaktif di browser Anda:
```bash
streamlit run app.py
```
Aplikasi secara otomatis akan terbuka di peramban web Anda pada alamat `http://localhost:8501`.

---

##  2. Konsep Aplikasi & Integrasi Model JST

Aplikasi **SoundSync** memadukan dua jenis algoritma JST yang dibangun secara manual (*from scratch*) menggunakan **NumPy**:
1. **Model 1: Adaline (Adaptive Linear Neuron)**
   - **Peran**: Memprediksi status karakteristik vibe lagu ke dalam kategori bipolar: *Energetic/Upbeat (+1)* atau *Calm/Relaxing (-1)*.
   - **Input**: Tempo / Danceability (0.1 - 1.0), Kenyaringan / Loudness (dB), Acousticness (0.0 - 1.0), dan Valence / Kegembiraan Lirik (0.0 - 1.0).
   - **Output**: Persentase energi musik representatif dan klasifikasi vibe akustik.
2. **Model 2: Learning Vector Quantization (LVQ)**
   - **Peran**: Mengklasifikasikan genre lagu menjadi salah satu dari 4 kategori utama: *Pop / Dance*, *Rock / Metal*, *Jazz / Lo-Fi*, dan *EDM / Electronic*.
   - **Input**: Kerapatan Ketukan / Beat Density (0.0 - 1.0), Distorsi Elektrik / Synth Distortions (0.0 - 1.0), dan Kemenonjolan Vokal / Vocal Prominence (0.0 - 1.0).
   - **Output**: Klasifikasi genre musik beserta pemetaan otomatis daftar lagu-lagu legendaris ke dalam kluster genre tersebut.

---

##  3. Pembahasan Matematika Bab III: Perhitungan Manual (Bahasa Indonesia)

Berikut adalah lampiran perhitungan manual satu langkah perambatan maju (*Forward Pass*) dan satu langkah pembaruan bobot (*Weight Update*) untuk kedua model:

### 3.1 Perhitungan Manual Adaline
* **Spesifikasi Awal:**
   - Input: $x = [0.8, 0.4, 0.2, 0.9]$ (Tempo/Danceability, Loudness, Acousticness, Valence)
   - Target: $y = 1$ (Energetic/Upbeat)
   - Bobot Awal: $W = [0.1, -0.2, 0.15, 0.3]^T$
   - Bias Awal: $b = 0.05$
   - Learning Rate ($\eta$): $0.1$

* **Forward Pass (Net Input):**
  $$net = \sum(x_i \cdot w_i) + b$$
  $$net = (0.8 \cdot 0.1) + (0.4 \cdot -0.2) + (0.2 \cdot 0.15) + (0.9 \cdot 0.3) + 0.05$$
  $$net = 0.08 - 0.08 + 0.03 + 0.27 + 0.05 = 0.35$$
  
  *Adaline menggunakan aktivasi linear saat training, sehingga output $= net = 0.35$.*

* **Backward Pass / Delta Rule (Update Bobot & Bias):**
  - Hitung Error:
    $$E = y - net = 1 - 0.35 = 0.65$$
  - Pembaruan Bobot ($\Delta w_i = \eta \cdot E \cdot x_i$):
    - $\Delta w_1 = 0.1 \cdot 0.65 \cdot 0.8 = 0.052 \rightarrow w_1^{(baru)} = 0.1 + 0.052 = 0.152$
    - $\Delta w_2 = 0.1 \cdot 0.65 \cdot 0.4 = 0.026 \rightarrow w_2^{(baru)} = -0.2 + 0.026 = -0.174$
    - $\Delta w_3 = 0.1 \cdot 0.65 \cdot 0.2 = 0.013 \rightarrow w_3^{(baru)} = 0.15 + 0.013 = 0.163$
    - $\Delta w_4 = 0.1 \cdot 0.65 \cdot 0.9 = 0.0585 \rightarrow w_4^{(baru)} = 0.3 + 0.0585 = 0.3585$
  - Pembaruan Bias ($\Delta b = \eta \cdot E$):
    - $\Delta b = 0.1 \cdot 0.65 = 0.065 \rightarrow b^{(baru)} = 0.05 + 0.065 = 0.115$

---

### 3.2 Perhitungan Manual LVQ
* **Spesifikasi Awal:**
  - Vektor Input: $x = [0.7, 0.3, 0.8]$ (Beat Density, Guitar Distortions, Vocal Prominence) dengan Label Kelas Sebenarnya $y = 0$ (Pop / Dance)
  - Vektor Prototipe Awal:
    - $W_0 = [0.6, 0.2, 0.7]$ (Kelas 0 - Pop / Dance)
    - $W_1 = [0.3, 0.8, 0.4]$ (Kelas 1 - Rock / Metal)
    - $W_2 = [0.5, 0.4, 0.9]$ (Kelas 2 - Jazz / Lo-Fi)
    - $W_3 = [0.1, 0.1, 0.2]$ (Kelas 3 - EDM)
  - Learning Rate ($\alpha$): $0.5$

* **Mencari Best Matching Unit (BMU) dengan Jarak Euclidean:**
  - Jarak ke $W_0$: $d(x, W_0) = \sqrt{(0.7-0.6)^2 + (0.3-0.2)^2 + (0.8-0.7)^2} = \sqrt{0.01 + 0.01 + 0.01} = \sqrt{0.03} \approx 0.1732$
  - Jarak ke $W_1$: $d(x, W_1) = \sqrt{(0.7-0.3)^2 + (0.3-0.8)^2 + (0.8-0.4)^2} = \sqrt{0.16 + 0.25 + 0.16} = \sqrt{0.57} \approx 0.7550$
  - Jarak ke $W_2$: $d(x, W_2) = \sqrt{(0.7-0.5)^2 + (0.3-0.4)^2 + (0.8-0.9)^2} = \sqrt{0.04 + 0.01 + 0.01} = \sqrt{0.06} \approx 0.2449$
  - Jarak ke $W_3$: $d(x, W_3) = \sqrt{(0.7-0.1)^2 + (0.3-0.1)^2 + (0.8-0.2)^2} = \sqrt{0.36 + 0.04 + 0.36} = \sqrt{0.76} \approx 0.8718$

  *Prototipe pemenang (BMU) adalah $W_0$ karena memiliki jarak Euclidean terkecil ($0.1732$).*

* **Pembaruan Bobot Prototipe BMU:**
  Karena Label BMU ($0$) sama dengan target kelas input ($y = 0$), maka bobot prototipe $W_0$ diperbarui agar bergeser **mendekati** input $x$:
  $$W_0^{(baru)} = W_0 + \alpha \cdot (x - W_0)$$
  $$W_0^{(baru)} = [0.6, 0.2, 0.7] + 0.5 \cdot ([0.7, 0.3, 0.8] - [0.6, 0.2, 0.7])$$
  $$W_0^{(baru)} = [0.6, 0.2, 0.7] + 0.5 \cdot [0.1, 0.1, 0.1]$$
  $$W_0^{(baru)} = [0.6, 0.2, 0.7] + [0.05, 0.05, 0.05] = [0.65, 0.25, 0.75]$$

  *Seluruh prototipe lainnya ($W_1$, $W_2$, $W_3$) tetap.*
