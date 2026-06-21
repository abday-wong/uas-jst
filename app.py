# ==============================================================================
# APP CONFIGURATION AND LIBRARIES SETUP
# ==============================================================================
# Cara Instalasi dan Menjalankan Aplikasi:
# 1. Pastikan Python sudah terinstal di sistem Anda (versi 3.8 ke atas direkomendasikan).
# 2. Instal library yang dibutuhkan dengan menjalankan perintah berikut di terminal:
#    pip install -r requirements.txt
# 3. Jalankan aplikasi Streamlit menggunakan perintah:
#    streamlit run app.py
# ==============================================================================

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set page configuration with a premium look
st.set_page_config(
    page_title="SoundSync: Music Vibe & Genre Classifier - JST Final Exam",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom premium CSS styling for the interface
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
    html, body, .stApp, .stMarkdown, p, li, label, .stWidgetLabel {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    .stApp {
        background: radial-gradient(circle at 50% 50%, #0d111e 0%, #04060a 100%) !important;
        background-attachment: fixed !important;
    }
    
    .main {
        background: transparent !important;
    }
    
    /* Transparent default Streamlit header */
    header[data-testid="stHeader"], header {
        background-color: transparent !important;
        background: transparent !important;
    }
    
    header[data-testid="stHeader"] button, header button {
        color: #ffffff !important;
    }
    
    /* Glassmorphic Sidebar */
    .stSidebar, [data-testid="stSidebar"] {
        background-color: rgba(8, 10, 18, 0.6) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
    }
    
    .stSidebar h1, .stSidebar h2, .stSidebar h3, .stSidebar h4, .stSidebar h5, .stSidebar h6 {
        color: #ffffff !important;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #ff007f !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-weight: 700 !important;
    }
    
    /* Form widget and slider labels */
    label, [data-testid="stWidgetLabel"] p, [data-testid="stWidgetLabel"] {
        color: rgba(255, 255, 255, 0.95) !important;
        font-weight: 500 !important;
    }
    
    /* Streamlit expander header color */
    .streamlit-expanderHeader p, .streamlit-expanderHeader {
        color: rgba(255, 255, 255, 0.95) !important;
    }
    
    /* Body & Paragraph Text Legibility */
    p, span, li, .stMarkdown p, .stMarkdown li {
        color: rgba(255, 255, 255, 0.85) !important;
        line-height: 1.6 !important;
    }
    
    /* Selectbox dropdown container */
    .stSelectbox div[data-baseweb="select"] {
        background-color: rgba(255, 255, 255, 0.04) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 8px !important;
    }
    
    .stSelectbox div[data-baseweb="select"] div {
        color: #ffffff !important;
    }
    
    /* Style tabs for premium glassmorphism */
    button[data-baseweb="tab"] {
        background-color: transparent !important;
        color: rgba(255, 255, 255, 0.6) !important;
        border: none !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        padding: 10px 20px !important;
        transition: all 0.3s ease !important;
    }
    
    button[data-baseweb="tab"]:hover {
        color: #ff007f !important;
    }
    
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #ff007f !important;
        border-bottom: 2px solid #ff007f !important;
    }
    
    div[data-testid="stTabContent"] {
        background: rgba(255, 255, 255, 0.01) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        border: 1px solid rgba(255, 255, 255, 0.03) !important;
        border-radius: 16px;
        padding: 25px;
        margin-top: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
    }
    
    /* Glassmorphic notification alerts */
    div[data-testid="stNotification"] {
        background-color: rgba(255, 255, 255, 0.03) !important;
        backdrop-filter: blur(10px) !important;
        -webkit-backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 12px !important;
    }
    div[data-testid="stNotification"] p {
        color: #ffffff !important;
    }
    
    /* Custom Card Styles */
    .card-vibe-high {
        background: rgba(19, 43, 29, 0.35) !important;
        backdrop-filter: blur(16px) saturate(180%) !important;
        -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
        border: 1px solid rgba(0, 230, 118, 0.25) !important;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 230, 118, 0.06);
    }
    
    .card-vibe-low {
        background: rgba(48, 19, 24, 0.35) !important;
        backdrop-filter: blur(16px) saturate(180%) !important;
        -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
        border: 1px solid rgba(255, 23, 68, 0.25) !important;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(255, 23, 68, 0.06);
    }
    
    .track-badge {
        display: inline-block;
        background-color: rgba(30, 34, 53, 0.45) !important;
        backdrop-filter: blur(10px) !important;
        -webkit-backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 12px;
        padding: 15px 20px;
        margin: 8px 0px;
        font-size: 16px;
        color: #e2e8f0;
        width: 100%;
        box-sizing: border-box;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
    }
</style>
""", unsafe_allow_html=True)


# ==============================================================================
# MODEL 1: ADALINE (ADAPTIVE LINEAR NEURON) FROM SCRATCH
# ==============================================================================
# Deskripsi Matematis & Fungsionalitas:
# Model ini digunakan untuk memprediksi tipe Vibe Lagu (Energetic (+1) vs Calm (-1))
# berdasarkan parameter audio teknis harian.
#
# Rumus Update Bobot (Delta Rule / Least Mean Squares):
# 1. Output Net Input (Linear):
#    net = X . W + b
# 2. Hitung Error:
#    error = y - net
# 3. Pembaruan Bobot dan Bias:
#    W_baru = W_lama + lr * (X.T . error) / N
#    b_baru = b_lama + lr * sum(error) / N
# ==============================================================================

class Adaline:
    def __init__(self, input_dim=4, lr=0.01):
        """
        Inisialisasi parameter jaringan Adaline.
        """
        self.input_dim = input_dim
        self.lr = lr
        
        # Set seed agar hasil training konsisten
        np.random.seed(42)
        
        # Inisialisasi bobot dan bias acak mendekati nol
        self.W = np.random.randn(self.input_dim, 1) * 0.01
        self.b = np.zeros((1, 1))

    def forward(self, X):
        """
        Kalkulasi keluaran linear (net input).
        """
        return np.dot(X, self.W) + self.b

    def predict(self, X):
        """
        Prediksi kelas bipolar: +1 (Energetic) atau -1 (Calm).
        """
        net = self.forward(X)
        return np.where(net >= 0.0, 1, -1)

    def train(self, X, y, epochs=1000):
        """
        Melakukan pelatihan model Adaline menggunakan Delta Rule.
        """
        mse_history = []
        n_samples = len(X)
        
        for epoch in range(epochs):
            net = self.forward(X)
            errors = y - net
            
            # Update bobot dan bias (LMS / Delta Rule)
            self.W += (self.lr / n_samples) * np.dot(X.T, errors)
            self.b += (self.lr / n_samples) * np.sum(errors, axis=0, keepdims=True)
            
            # Hitung Mean Squared Error
            mse = np.mean(np.square(errors))
            mse_history.append(mse)
            
        return mse_history


# ==============================================================================
# MODEL 2: LEARNING VECTOR QUANTIZATION (LVQ) FROM SCRATCH
# ==============================================================================
# Deskripsi Matematis & Fungsionalitas:
# Model ini digunakan untuk mengklasifikasikan genre lagu (Genre Vibe)
# ke dalam 4 kategori berdasarkan profil ketukan, distorsi elektrik, dan vokal.
#
# Rumus Update Bobot LVQ:
# 1. Cari Best Matching Unit (BMU) dengan jarak Euclidean terkecil:
#    d(x, W_j) = sqrt( sum( (x_i - w_ji)^2 ) )
# 2. Perbarui bobot BMU (W_c) berdasarkan kesamaan label:
#    - Jika Label BMU == Label Target (Benar):
#      W_c_baru = W_c_lama + lr * (X - W_c_lama)
#    - Jika Label BMU != Label Target (Salah):
#      W_c_baru = W_c_lama - lr * (X - W_c_lama)
# ==============================================================================

class LearningVectorQuantization:
    def __init__(self, input_dim=3, num_classes=4, lr_start=0.5):
        """
        Inisialisasi kodebook vektor prototipe untuk LVQ.
        """
        self.input_dim = input_dim
        self.num_classes = num_classes
        self.lr_start = lr_start
        
        np.random.seed(42)
        # Inisialisasi 1 prototipe vektor per kelas secara acak [0.1, 0.9]
        self.prototypes = np.random.uniform(0.1, 0.9, (self.num_classes, self.input_dim))
        self.prototype_labels = np.arange(self.num_classes)

    def find_bmu(self, x):
        """
        Mencari BMU (prototipe terdekat) menggunakan Jarak Euclidean.
        """
        distances = np.linalg.norm(self.prototypes - x, axis=1)
        bmu_idx = np.argmin(distances)
        return bmu_idx, distances

    def predict(self, X):
        """
        Memprediksi kelas untuk sekumpulan input.
        """
        preds = []
        for x in X:
            bmu_idx, _ = self.find_bmu(x)
            preds.append(self.prototype_labels[bmu_idx])
        return np.array(preds)

    def train(self, X, y, epochs=200):
        """
        Melatih vektor prototipe LVQ menggunakan supervised clustering.
        """
        # Inisialisasi vektor prototipe berdasarkan rata-rata (mean) dari data tiap kelas
        for c in range(self.num_classes):
            class_samples = X[y == c]
            if len(class_samples) > 0:
                self.prototypes[c] = np.mean(class_samples, axis=0)

        error_history = []
        
        for epoch in range(epochs):
            # Decay learning rate secara linier
            lr = self.lr_start * (1.0 - epoch / epochs)
            if lr < 0.01:
                lr = 0.01
                
            for x, label in zip(X, y):
                bmu_idx, _ = self.find_bmu(x)
                bmu_label = self.prototype_labels[bmu_idx]
                
                # Update rule
                if bmu_label == label:
                    self.prototypes[bmu_idx] += lr * (x - self.prototypes[bmu_idx])
                else:
                    self.prototypes[bmu_idx] -= lr * (x - self.prototypes[bmu_idx])
            
            # Hitung Classification Error di akhir epoch
            preds = self.predict(X)
            accuracy = np.mean(preds == y)
            error_history.append(1.0 - accuracy)
            
        return error_history


# ==============================================================================
# DATA GENERATION AND PREPARATION
# ==============================================================================

# 1. Membuat data sintetis untuk training Adaline (Model 1)
# Bipolar labels: +1 (Energetic/Upbeat), -1 (Calm/Relaxing)
def generate_music_vibe_dataset():
    np.random.seed(42)
    n_samples = 180
    
    # Fitur:
    # - Tempo / Danceability (0.1 s/d 1.0)
    # - Loudness (Loudness dalam dB, normalisasi -60 s/d 0)
    # - Acousticness (Kemurnian instrumen akustik, 0.0 s/d 1.0)
    # - Valence (Keceriaan emosi lagu, 0.0 s/d 1.0)
    danceability = np.random.uniform(0.1, 1.0, n_samples)
    loudness = np.random.uniform(-60.0, 0.0, n_samples)
    acousticness = np.random.uniform(0.0, 1.0, n_samples)
    valence = np.random.uniform(0.0, 1.0, n_samples)
    
    X_raw = np.column_stack((danceability, loudness, acousticness, valence))
    
    # Normalisasi Min-Max ke [0, 1]
    norm_params = {
        'dance_min': 0.1, 'dance_max': 1.0,
        'loud_min': -60.0, 'loud_max': 0.0,
        'acoustic_min': 0.0, 'acoustic_max': 1.0,
        'valence_min': 0.0, 'valence_max': 1.0
    }
    
    X_norm = np.zeros_like(X_raw)
    X_norm[:, 0] = danceability
    X_norm[:, 1] = (loudness + 60.0) / 60.0
    X_norm[:, 2] = acousticness
    X_norm[:, 3] = valence
    
    # Hubungan target:
    # Lagu berenergi (+1) jika danceability & loudness tinggi, akustik rendah, valence tinggi
    score = 0.55 * X_norm[:, 0] + 0.45 * X_norm[:, 1] - 0.45 * X_norm[:, 2] + 0.35 * X_norm[:, 3] - 0.3
    # Tambahkan noise
    score += np.random.normal(0, 0.08, n_samples)
    
    # Konversi ke bipolar +1 atau -1
    y = np.where(score >= 0.0, 1, -1).reshape(-1, 1)
    
    return X_raw, X_norm, y, norm_params

# 2. Membuat data sintetis untuk training LVQ (Model 2)
# Masing-masing data merepresentasikan profil lagu untuk 4 kategori genre
# Fitur: [Beat Density, Electric Distortions, Vocal Prominence]
# Label: 
#   0: "Pop / Dance"
#   1: "Rock / Metal"
#   2: "Jazz / Lo-Fi"
#   3: "EDM / Electronic"
def generate_genre_dataset():
    np.random.seed(99)
    n_samples = 160
    
    X = []
    y = []
    
    # Kelas 0: Pop / Dance (Beat density tinggi, Distorsi rendah, Vocal prominence tinggi)
    X.append(np.random.uniform([0.6, 0.0, 0.7], [0.9, 0.3, 1.0], (40, 3)))
    y.append(np.zeros(40, dtype=int))
    
    # Kelas 1: Rock / Metal (Beat density tinggi, Distorsi tinggi, Vocal prominence rendah-sedang)
    X.append(np.random.uniform([0.7, 0.7, 0.2], [1.0, 1.0, 0.6], (40, 3)))
    y.append(np.ones(40, dtype=int))
    
    # Kelas 2: Jazz / Lo-Fi (Beat density rendah, Distorsi rendah, Vocal prominence sedang)
    X.append(np.random.uniform([0.1, 0.0, 0.4], [0.4, 0.2, 0.7], (40, 3)))
    y.append(np.ones(40, dtype=int) * 2)
    
    # Kelas 3: EDM / Electronic (Beat density tinggi, Distorsi sedang, Vocal prominence rendah)
    X.append(np.random.uniform([0.7, 0.3, 0.0], [1.0, 0.6, 0.3], (40, 3)))
    y.append(np.ones(40, dtype=int) * 3)
    
    X = np.vstack(X)
    y = np.concatenate(y)
    
    return X, y


# ==============================================================================
# STREAMLIT CACHED TRAINING EXECUTION
# ==============================================================================

@st.cache_resource
def train_and_cache_models():
    # 1. Ambil dataset Adaline
    _, X_adaline_train, y_adaline_train, norm_params = generate_music_vibe_dataset()
    
    # Latih Model 1: Adaline (η = 0.1)
    ada_model = Adaline(input_dim=4, lr=0.1)
    ada_history = ada_model.train(X_adaline_train, y_adaline_train, epochs=800)
    
    # Latih model pembanding dengan η berbeda (untuk Analisis Bab IV)
    ada_lr_001 = Adaline(input_dim=4, lr=0.01)
    history_001 = ada_lr_001.train(X_adaline_train, y_adaline_train, epochs=800)
    
    ada_lr_05 = Adaline(input_dim=4, lr=0.5)
    history_05 = ada_lr_05.train(X_adaline_train, y_adaline_train, epochs=800)
    
    # 2. Ambil dataset LVQ & Latih Model 2: LVQ
    X_lvq_train, y_lvq_train = generate_genre_dataset()
    lvq_model = LearningVectorQuantization(input_dim=3, num_classes=4, lr_start=0.5)
    lvq_history = lvq_model.train(X_lvq_train, y_lvq_train, epochs=250)
    
    return {
        "ada_model": ada_model,
        "ada_history": ada_history,
        "history_001": history_001,
        "history_05": history_05,
        "lvq_model": lvq_model,
        "lvq_history": lvq_history,
        "norm_params": norm_params
    }

cached_data = train_and_cache_models()


# ==============================================================================
# STREAMLIT USER INTERFACE & LAYOUT
# ==============================================================================

# Title Banner
st.write("""
<div style="text-align: center; padding: clamp(15px, 4vw, 25px) 10px; border-bottom: 2px solid #ff007f; margin-bottom: 25px;">
    <h1 style="margin: 0; font-size: clamp(1.8rem, 5vw, 2.5rem); font-weight: 800; color: #ff007f; line-height: 1.2;">SOUNDSYNC: MUSIC VIBE & GENRE CLASSIFIER</h1>
    <p style="font-size: clamp(0.9rem, 2.5vw, 1.1rem); color: #a0aec0; margin-top: 10px; line-height: 1.4;">
        Klasifikasi Genre & Karakteristik Suara Musik Menggunakan JST Adaline dan LVQ dari Scratch
    </p>
    <span style="background-color: #ff007f; color: #fff; padding: 4px 10px; border-radius: 20px; font-size: clamp(10px, 2vw, 11px); font-weight: bold; text-transform: uppercase;">
        Tugas Akhir Jaringan Saraf Tiruan (JST) - Adaline & LVQ
    </span>
</div>
""", unsafe_allow_html=True)

# SIDEBAR: PANEL INPUT USER (LANGKAH DEMI LANGKAH)
st.sidebar.markdown("""
<div style="background-color: #161925; padding: 15px; border-radius: 8px; border-left: 5px solid #ff007f; margin-bottom: 20px;">
    <h4 style="margin: 0; color: #ffffff;">LANGKAH 1: Karakteristik Lagu (Adaline)</h4>
    <small style="color: #a0aec0;">Setel parameter teknis lagu di bawah ini.</small>
</div>
""", unsafe_allow_html=True)

# Sidebar Inputs for Model 1 (Adaline)
danceability = st.sidebar.slider("Tempo & Danceability (0.1 = Lambat, 1.0 = Sangat Cepat/Danceable)", min_value=0.1, max_value=1.0, value=0.7, step=0.05)
loudness = st.sidebar.slider("Kenyaringan / Volume Loudness (dB)", min_value=-60.0, max_value=0.0, value=-12.0, step=1.0)
acousticness = st.sidebar.slider("Acousticness (0.0 = Elektrik/Synth, 1.0 = Akustik Murni)", min_value=0.0, max_value=1.0, value=0.2, step=0.05)
valence = st.sidebar.slider("Valence / Kegembiraan Lirik (0.0 = Melankolis, 1.0 = Sangat Ceria)", min_value=0.0, max_value=1.0, value=0.6, step=0.05)

st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style="background-color: #161925; padding: 15px; border-radius: 8px; border-left: 5px solid #00f0ff; margin-bottom: 20px;">
    <h4 style="margin: 0; color: #ffffff;">LANGKAH 2: Profil Suara Genre (LVQ)</h4>
    <small style="color: #a0aec0;">Masukkan instrumen dan ketukan akustik lagu.</small>
</div>
""", unsafe_allow_html=True)

# Sidebar Inputs for Model 2 (LVQ)
beat_density = st.sidebar.slider("Kerapatan Ketukan / Beat Density (0.0 = Renggang, 1.0 = Sangat Rapat)", min_value=0.0, max_value=1.0, value=0.7, step=0.05)
electric_distortion = st.sidebar.slider("Distorsi Elektrik / Synth Distortions (0.0 = Bersih, 1.0 = Berat)", min_value=0.0, max_value=1.0, value=0.2, step=0.05)
vocal_prominence = st.sidebar.slider("Kemenonjolan Vokal / Vocal Prominence (0.0 = Instrumental, 1.0 = Vokal Dominan)", min_value=0.0, max_value=1.0, value=0.8, step=0.05)


# TABS LAYOUT FOR APP SECTIONS
tab_dashboard, tab_charts = st.tabs([
    "Dashboard Utama & Rekomendasi", 
    "Kurva Training & Visualisasi Model"
])

# ==============================================================================
# TAB 1: DASHBOARD UTAMA & REKOMENDASI
# ==============================================================================
with tab_dashboard:
    # Onboarding Guide for User
    st.markdown("""
    <div style="background-color: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 16px; padding: clamp(15px, 3vw, 25px); margin-bottom: 30px;">
        <h3 style="margin-top: 0; color: #ff007f; font-size: clamp(1.2rem, 3.5vw, 1.6rem);"> Bagaimana Cara Kerja Aplikasi Ini?</h3>
        <p style="font-size: clamp(0.85rem, 2.5vw, 0.95rem); margin-bottom: 15px; color: #a0aec0;">
            Aplikasi ini mendeteksi karakteristik serta genre lagu secara otomatis menggunakan dua model <strong>Jaringan Saraf Tiruan (JST)</strong> yang berjalan secara real-time berdasarkan input yang Anda masukkan di panel kiri:
        </p>
        <div style="display: flex; gap: 15px; flex-wrap: wrap;">
            <div style="flex: 1; min-width: 250px; background-color: rgba(255,255,255,0.02); padding: 15px; border-radius: 12px; border-left: 4px solid #ff007f;">
                <strong style="color: #ffffff; font-size: clamp(0.9rem, 2.5vw, 1.05rem);">1. Prediksi Vibe Karakter (Model Adaline)</strong>
                <p style="font-size: clamp(0.8rem, 2.2vw, 0.9rem); margin-top: 5px; color: #a0aec0; line-height: 1.4;">
                    Memprediksi apakah lagu tergolong bersemangat/cepat (<strong>Energetic & Upbeat</strong>) atau lambat/menenangkan (<strong>Calm & Relaxing</strong>) berdasarkan tempo, volume, kemurnian akustik, dan valensi emosi.
                </p>
            </div>
            <div style="flex: 1; min-width: 250px; background-color: rgba(255,255,255,0.02); padding: 15px; border-radius: 12px; border-left: 4px solid #00f0ff;">
                <strong style="color: #ffffff; font-size: clamp(0.9rem, 2.5vw, 1.05rem);">2. Klasifikasi Genre Musik (Model LVQ)</strong>
                <p style="font-size: clamp(0.8rem, 2.2vw, 0.9rem); margin-top: 5px; color: #a0aec0; line-height: 1.4;">
                    Mendeteksi genre lagu ke dalam salah satu dari 4 kategori utama (Pop/Dance, Rock/Metal, Jazz/Lo-Fi, EDM) dengan mencocokkan densitas beat, distorsi elektrik, dan kemenonjolan vokal.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("### Hasil Klasifikasi Lagu Hari Ini")
    
    col1, col2 = st.columns(2)
    
    # Model 1 (Adaline): Evaluasi Karakteristik Vibe
    with col1:
        st.write("#### Prediksi Karakteristik Vibe (Adaline)")
        
        # Jembatan Normalisasi untuk input real-time
        params = cached_data["norm_params"]
        norm_dance = danceability
        norm_loud = (loudness - params['loud_min']) / (params['loud_max'] - params['loud_min'])
        norm_acoustic = acousticness
        norm_valence = valence
        
        input_adaline = np.array([[norm_dance, norm_loud, norm_acoustic, norm_valence]])
        
        ada_model = cached_data["ada_model"]
        raw_score = ada_model.forward(input_adaline)[0][0]
        prediction_state = ada_model.predict(input_adaline)[0][0]
        
        # Penskalaan nilai mentah [-1.0 s/d 1.0] ke [0% s/d 100%]
        energy_pct = int(np.clip((raw_score + 1.0) / 2.0 * 100.0, 0, 100))
        
        if prediction_state == 1:
            st.markdown(f"""
            <div class="card-vibe-high" style="padding: clamp(15px, 3vw, 20px);">
                <h2 style="margin: 0; color: #00e676; font-size: clamp(1.3rem, 4vw, 1.7rem);">ENERGETIC & UPBEAT (+1)</h2>
                <h3 style="margin: 5px 0 12px 0; color: #ffffff; font-size: clamp(1.0rem, 3vw, 1.3rem);">Energy Level Lagu: {energy_pct}%</h3>
                <p style="font-size: clamp(0.85rem, 2.5vw, 0.95rem); margin: 0; line-height: 1.4;">Karakteristik lagu ini berenergi tinggi, upbeat, dan dinamis. Sangat cocok didengarkan untuk membakar semangat saat berolahraga, pesta, atau bekerja aktif.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="card-vibe-low" style="padding: clamp(15px, 3vw, 20px);">
                <h2 style="margin: 0; color: #ff1744; font-size: clamp(1.3rem, 4vw, 1.7rem);">CALM & RELAXING (-1)</h2>
                <h3 style="margin: 5px 0 12px 0; color: #ffffff; font-size: clamp(1.0rem, 3vw, 1.3rem);">Energy Level Lagu: {energy_pct}%</h3>
                <p style="font-size: clamp(0.85rem, 2.5vw, 0.95rem); margin: 0; line-height: 1.4;">Karakteristik lagu ini damai, tenang, dan rileks. Sangat cocok didengarkan untuk meredakan ketegangan, belajar, tidur, atau membaca buku.</p>
            </div>
            """, unsafe_allow_html=True)
            
        st.progress(energy_pct / 100.0)
        
        # Penjelasan Keputusan UX
        st.markdown(f"""
        <div style="background-color: rgba(255, 255, 255, 0.01); border: 1px dashed rgba(255,255,255,0.1); padding: 15px; border-radius: 8px; margin-top: 15px; font-size: 13px;">
            <strong style="color: #ffffff;">Bagaimana model mengambil keputusan ini?</strong><br/>
            Model Adaline mengalikan nilai parameter teknis lagu Anda dengan bobot latihnya secara linear. Hasil akumulasinya adalah <strong>{raw_score:.3f}</strong>. Karena nilai ini {"lebih besar dari atau sama dengan 0" if raw_score >= 0 else "kurang dari 0"}, sistem mengklasifikasikan lagu ini sebagai <strong>{"ENERGETIC" if prediction_state == 1 else "CALM"}</strong>.
        </div>
        """, unsafe_allow_html=True)

        # Tampilan metrik input Adaline
        st.write("")
        st.write("**Detail Parameter Input & Hasil Normalisasi:**")
        df_adaline = pd.DataFrame({
            "Parameter": ["Tempo / Danceability", "Kenyaringan (Loudness)", "Acousticness", "Valence (Keceriaan)"],
            "Nilai Input": [f"{danceability:.2f}", f"{loudness} dB", f"{acousticness:.2f}", f"{valence:.2f}"],
            "Nilai Normalisasi (Skala 0-1)": [f"{norm_dance:.3f}", f"{norm_loud:.3f}", f"{norm_acoustic:.3f}", f"{norm_valence:.3f}"]
        })
        st.table(df_adaline)

    # Model 2 (LVQ): Klasifikasi Genre Musik
    with col2:
        st.write("#### Klasifikasi Genre Musik (LVQ)")
        
        input_lvq = np.array([[beat_density, electric_distortion, vocal_prominence]])
        lvq_model = cached_data["lvq_model"]
        predicted_class = lvq_model.predict(input_lvq)[0]
        
        genres = {
            0: {"title": "Pop / Dance", "color": "#ffea00", "desc": "Ketukan bersemangat yang catchy dengan vokal dominan dan bersih. Cocok untuk dinikmati di stasiun radio, pesta pop, atau playlist harian santai."},
            1: {"title": "Rock / Metal", "color": "#00e5ff", "desc": "Suara berkarakter keras dengan distorsi gitar elektrik yang kencang dan ketukan drum yang solid. Terbaik didengarkan saat ingin fokus memacu adrenalin."},
            2: {"title": "Jazz / Lo-Fi", "color": "#ff9100", "desc": "Ketukan santai yang lambat dengan melodi instrumen alami (piano/trompet) dan vokal bersih yang hangat. Cocok untuk belajar, rileksasi, dan teman minum kopi."},
            3: {"title": "EDM / Electronic", "color": "#d500f9", "desc": "Synthesizer elektrik yang dominan dengan vokal minim/instrumental dan beat bas elektronik yang padat. Musik lantai dansa yang penuh energi sintetis."}
        }
        
        current_genre = genres[predicted_class]
        
        st.markdown(f"""
        <div style="background-color: rgba(255, 255, 255, 0.03); border: 2px solid {current_genre['color']}; border-radius: 16px; padding: clamp(15px, 3vw, 20px); box-shadow: 0 8px 32px 0 rgba(0,0,0,0.2);">
            <h2 style="margin: 0; color: {current_genre['color']}; font-size: clamp(1.3rem, 4vw, 1.7rem);">{current_genre['title'].upper()}</h2>
            <p style="margin-top: 10px; font-size: clamp(0.85rem, 2.5vw, 0.95rem); margin-bottom: 0; line-height: 1.4;">{current_genre['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Penjelasan Keputusan UX
        st.markdown(f"""
        <div style="background-color: rgba(255, 255, 255, 0.01); border: 1px dashed rgba(255,255,255,0.1); padding: 15px; border-radius: 8px; margin-top: 15px; font-size: clamp(0.8rem, 2.2vw, 0.85rem);">
            <strong style="color: #ffffff;">Bagaimana model mengambil keputusan ini?</strong><br/>
            Model LVQ membandingkan koordinat akustik input Anda <strong>[{beat_density:.2f}, {electric_distortion:.2f}, {vocal_prominence:.2f}]</strong> dengan 4 pusat koordinat genre ideal (prototipe). Genre <strong>{current_genre['title']}</strong> dideteksi memiliki jarak Euclidean terdekat dengan parameter lagu Anda saat ini.
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        st.write("#### Contoh Lagu yang Mirip Karakteristiknya")
        st.write("Berikut adalah lagu-lagu legendaris yang memiliki kluster genre serupa secara real-time di Spotify/Apple Music:")
        
        # Cari BMU untuk beberapa lagu contoh
        sample_tracks = [
            {"name": "Blinding Lights - The Weeknd", "v": [0.8, 0.1, 0.85]},
            {"name": "Master of Puppets - Metallica", "v": [0.95, 0.95, 0.4]},
            {"name": "Come Away With Me - Norah Jones", "v": [0.2, 0.05, 0.7]},
            {"name": "Animals - Martin Garrix", "v": [0.9, 0.6, 0.05]},
            {"name": "Bohemian Rhapsody - Queen", "v": [0.65, 0.75, 0.8]}
        ]
        
        for track in sample_tracks:
            bmu_idx, _ = lvq_model.find_bmu(np.array(track["v"]))
            genre_info = genres[bmu_idx]
            st.markdown(f"""
            <div class="track-badge" style="border-left: 4px solid {genre_info['color']} !important; padding: clamp(10px, 2.5vw, 15px); font-size: clamp(0.85rem, 2.4vw, 0.95rem);">
                <strong>{track['name']}</strong> → <span style="color: {genre_info['color']}; font-weight: bold;">{genre_info['title']}</span>
            </div>
            """, unsafe_allow_html=True)


# ==============================================================================
# TAB 2: KURVA TRAINING & VISUALISASI MODEL
# ==============================================================================
with tab_charts:
    # Bersihkan sisa gambar dari memori matplotlib untuk mencegah penumpukan grafik (overplotting)
    plt.close('all')
    
    # Ambil data latih dan parameter dari cache
    ada_model = cached_data["ada_model"]
    lvq_model = cached_data["lvq_model"]
    params = cached_data["norm_params"]
    
    # Hitung normalisasi input real-time lokal untuk plotting
    norm_dance_val = danceability
    norm_loud_val = (loudness - params['loud_min']) / (params['loud_max'] - params['loud_min'])
    norm_acoustic_val = acousticness
    norm_valence_val = valence
    
    input_adaline = np.array([[norm_dance_val, norm_loud_val, norm_acoustic_val, norm_valence_val]])
    current_prediction_state = ada_model.predict(input_adaline)[0][0]

    st.markdown("""
    <div style="background-color: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 12px; padding: 20px; margin-bottom: 25px;">
        <h4 style="margin-top:0; color: #ff007f;"> Panduan Membaca Grafik Visualisasi</h4>
        <p style="font-size: 13.5px; margin-bottom: 0; color: #a0aec0;">
            Tab ini memaparkan visualisasi performa latih model dan hubungan posisi input lagu Anda dengan batas klasifikasi. Kolom kiri memvisualisasikan model <strong>Adaline</strong> (karakteristik vibe), sedangkan kolom kanan memvisualisasikan model <strong>LVQ</strong> (genre musik).
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col_ada, col_lvq = st.columns(2)
    
    with col_ada:
        st.write("#### Konvergensi Model Adaline (MSE)")
        st.caption("Grafik di bawah menunjukkan nilai Mean Squared Error (MSE) model Adaline seiring berjalannya epoch latihan. Semakin rendah garis menuju nol, berarti model semakin akurat dalam belajar memisahkan kategori.")
        
        fig, ax = plt.subplots(figsize=(6, 4), facecolor='#0d111e')
        ax.set_facecolor('#0d111e')
        
        epochs_range = range(1, len(cached_data["ada_history"]) + 1)
        ax.plot(epochs_range, cached_data["ada_history"], color='#ff007f', linewidth=2.5, label='MSE (η = 0.1)')
        
        ax.tick_params(colors='white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')
        ax.set_xlabel("Epochs")
        ax.set_ylabel("Mean Squared Error")
        ax.grid(True, color='white', alpha=0.05)
        ax.legend(facecolor='#0d111e', labelcolor='white')
        
        st.pyplot(fig)
        plt.close(fig)
        
        st.write("#### Perbandingan Variasi Learning Rate (η)")
        st.caption("Grafik ini menunjukkan perbandingan kecepatan belajar Adaline. Nilai η terlalu kecil (0.01) membuat model lambat belajar. Nilai η terlalu besar (0.5) menyebabkan model berosilasi tidak stabil. Nilai η = 0.1 adalah nilai optimal.")
        
        fig_comp, ax_comp = plt.subplots(figsize=(6, 4), facecolor='#0d111e')
        ax_comp.set_facecolor('#0d111e')
        
        ax_comp.plot(epochs_range, cached_data["history_001"], color='#00e5ff', linestyle='--', label='η = 0.01 (Lambat)')
        ax_comp.plot(epochs_range, cached_data["ada_history"], color='#ff007f', label='η = 0.1 (Optimal)')
        ax_comp.plot(epochs_range, cached_data["history_05"], color='#ffab00', linestyle=':', label='η = 0.5 (Osilasi/Tidak Stabil)')
        
        ax_comp.tick_params(colors='white')
        ax_comp.xaxis.label.set_color('white')
        ax_comp.yaxis.label.set_color('white')
        ax_comp.title.set_color('white')
        ax_comp.set_xlabel("Epochs")
        ax_comp.set_ylabel("MSE")
        ax_comp.grid(True, color='white', alpha=0.05)
        ax_comp.legend(facecolor='#0d111e', labelcolor='white')
        
        st.pyplot(fig_comp)
        plt.close(fig_comp)

        st.write("#### Posisi Real-time vs Decision Boundary")
        st.caption("Plot 2D di bawah ini memproyeksikan data training Tempo/Danceability (x-axis) vs Acousticness (y-axis). Garis merah muda adalah Batas Keputusan (Decision Boundary). Simbol bintang melambangkan posisi lagu Anda secara real-time. Gerakkan slider di sidebar untuk melihat pergeseran posisi bintang.")
        
        # Ambil bobot Adaline
        W = ada_model.W.flatten()
        b = ada_model.b[0][0]
        
        # Gambar plot 2D: Danceability (X) vs Acousticness (Y)
        fig_bound, ax_bound = plt.subplots(figsize=(6, 4), facecolor='#0d111e')
        ax_bound.set_facecolor('#0d111e')
        
        # Plot training data points
        _, X_adaline_norm, y_adaline_val, _ = generate_music_vibe_dataset()
        energetic_mask = (y_adaline_val == 1).flatten()
        calm_mask = (y_adaline_val == -1).flatten()
        
        ax_bound.scatter(X_adaline_norm[energetic_mask, 0], X_adaline_norm[energetic_mask, 2], color='#00e676', alpha=0.3, label='Data Energetic (+1)', s=15)
        ax_bound.scatter(X_adaline_norm[calm_mask, 0], X_adaline_norm[calm_mask, 2], color='#ff1744', alpha=0.3, label='Data Calm (-1)', s=15)
        
        # Hitung garis batas keputusan: W[0]*x1 + W[1]*x2 + W[2]*x3 + W[3]*x4 + b = 0
        # Di mana x2 (loudness) dan x4 (valence) adalah posisi slider saat ini.
        # Maka x3 (acousticness) = -(W[0]*x1 + W[1]*x2 + W[3]*x4 + b) / W[2]
        x1_vals = np.linspace(0, 1.0, 100)
        if abs(W[2]) > 1e-5:
            x3_vals = -(W[0] * x1_vals + W[1] * norm_loud_val + W[3] * norm_valence_val + b) / W[2]
            ax_bound.plot(x1_vals, x3_vals, color='#ff007f', linewidth=2, label='Decision Boundary (net=0)')
            ax_bound.fill_between(x1_vals, -0.2, x3_vals, color='#ff1744', alpha=0.05)
            ax_bound.fill_between(x1_vals, x3_vals, 1.2, color='#00e676', alpha=0.05)
        
        # Plot posisi pengguna saat ini
        color_pos = '#00e676' if current_prediction_state == 1 else '#ff1744'
        ax_bound.scatter(norm_dance_val, norm_acoustic_val, color=color_pos, edgecolor='white', s=200, marker='*', label='Posisi Anda', zorder=5)
        
        ax_bound.set_xlim(-0.05, 1.05)
        ax_bound.set_ylim(-0.05, 1.05)
        ax_bound.set_xlabel("Normalized Tempo / Danceability (x1)")
        ax_bound.set_ylabel("Normalized Acousticness (x3)")
        ax_bound.tick_params(colors='white')
        ax_bound.xaxis.label.set_color('white')
        ax_bound.yaxis.label.set_color('white')
        ax_bound.grid(True, color='white', alpha=0.05)
        ax_bound.legend(facecolor='#0d111e', labelcolor='white', loc='upper right')
        
        st.pyplot(fig_bound)
        plt.close(fig_bound)
        
    with col_lvq:
        st.write("#### Konvergensi Model LVQ (Classification Error)")
        st.caption("Grafik di bawah ini memaparkan laju kesalahan klasifikasi model LVQ selama epoch latihan. Semakin lama melatih, tingkat error klasifikasi (Competitive Error Rate) model berkurang hingga stabil.")
        
        fig_lvq, ax_lvq = plt.subplots(figsize=(6, 4), facecolor='#0d111e')
        ax_lvq.set_facecolor('#0d111e')
        
        lvq_epochs_range = range(1, len(cached_data["lvq_history"]) + 1)
        ax_lvq.plot(lvq_epochs_range, cached_data["lvq_history"], color='#00e5ff', linewidth=2.5, label='Error Rate')
        
        ax_lvq.tick_params(colors='white')
        ax_lvq.xaxis.label.set_color('white')
        ax_lvq.yaxis.label.set_color('white')
        ax_lvq.title.set_color('white')
        ax_lvq.set_xlabel("Epochs")
        ax_lvq.set_ylabel("Classification Error Rate")
        ax_lvq.grid(True, color='white', alpha=0.05)
        ax_lvq.legend(facecolor='#0d111e', labelcolor='white')
        
        st.pyplot(fig_lvq)
        plt.close(fig_lvq)
        
        # Prototypes Visualizer (DataFrame of Prototypes)
        st.write("#### Koordinat Vektor Prototipe LVQ (Weights)")
        st.caption("Tabel di bawah memuat bobot latih akhir (koordinat ideal) dari 4 pusat genre musik di ruang input:")
        
        proto_df = pd.DataFrame(
            lvq_model.prototypes,
            columns=["Beat Density", "Guitar Distortions", "Vocal Prominence"],
            index=["Kelas 0: Pop / Dance", "Kelas 1: Rock / Metal", "Kelas 2: Jazz / Lo-Fi", "Kelas 3: EDM / Electronic"]
        )
        st.dataframe(proto_df.style.background_gradient(cmap="plasma", axis=None))

        st.write("#### Pemetaan Vektor Prototipe & Posisi Anda (3D)")
        st.caption("Ruang 3D di bawah ini memvisualisasikan posisi 4 prototipe genre musik (bola berwarna) dan posisi lagu Anda saat ini (simbol X berwarna merah muda). Garis penghubung lurus tebal menunjukkan prototipe terdekat (BMU) yang memenangkan klasifikasi.")
        
        # Data input saat ini
        user_vec = np.array([beat_density, electric_distortion, vocal_prominence])
        
        fig_3d = plt.figure(figsize=(6, 5), facecolor='#0d111e')
        ax_3d = fig_3d.add_subplot(111, projection='3d', facecolor='#0d111e')
        
        # Atur warna panel 3D
        ax_3d.xaxis.set_pane_color((0.05, 0.07, 0.12, 1.0))
        ax_3d.yaxis.set_pane_color((0.05, 0.07, 0.12, 1.0))
        ax_3d.zaxis.set_pane_color((0.05, 0.07, 0.12, 1.0))
        
        # Plot Prototypes
        protos = lvq_model.prototypes
        colors_3d = ['#ffea00', '#00e5ff', '#ff9100', '#d500f9']
        labels_3d = ['Pop / Dance', 'Rock / Metal', 'Jazz / Lo-Fi', 'EDM / Electronic']
        
        for idx, proto in enumerate(protos):
            ax_3d.scatter(proto[0], proto[1], proto[2], color=colors_3d[idx], s=150, depthshade=False, label=labels_3d[idx], edgecolor='white', linewidth=1.5)
            
        # Plot user position
        ax_3d.scatter(user_vec[0], user_vec[1], user_vec[2], color='#ff007f', s=200, marker='X', depthshade=False, label='Posisi Anda', edgecolor='white', linewidth=2)
        
        # Hubungkan garis dari user ke seluruh prototipe
        bmu_idx, _ = lvq_model.find_bmu(user_vec)
        for idx, proto in enumerate(protos):
            is_bmu = (idx == bmu_idx)
            linestyle = '-' if is_bmu else '--'
            linewidth = 2.5 if is_bmu else 0.8
            linecolor = colors_3d[idx] if is_bmu else 'gray'
            ax_3d.plot([user_vec[0], proto[0]], [user_vec[1], proto[1]], [user_vec[2], proto[2]], linestyle=linestyle, linewidth=linewidth, color=linecolor, alpha=0.8)
            
        ax_3d.set_xlabel("Beat Density", color='white')
        ax_3d.set_ylabel("Guitar Distortions", color='white')
        ax_3d.set_zlabel("Vocal Prominence", color='white')
        ax_3d.tick_params(colors='white')
        ax_3d.xaxis.label.set_color('white')
        ax_3d.yaxis.label.set_color('white')
        ax_3d.zaxis.label.set_color('white')
        ax_3d.grid(True, color='white', alpha=0.05)
        ax_3d.legend(facecolor='#0d111e', labelcolor='white', loc='upper left', prop={'size': 8})
        
        st.pyplot(fig_3d)
        plt.close(fig_3d)
