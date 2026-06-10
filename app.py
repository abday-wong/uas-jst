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
    page_title="VibeSync: Social Battery & Mood Optimizer - JST Final Exam",
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
    .card-battery-high {
        background: rgba(19, 43, 29, 0.35) !important;
        backdrop-filter: blur(16px) saturate(180%) !important;
        -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
        border: 1px solid rgba(0, 230, 118, 0.25) !important;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 230, 118, 0.06);
    }
    
    .card-battery-low {
        background: rgba(48, 19, 24, 0.35) !important;
        backdrop-filter: blur(16px) saturate(180%) !important;
        -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
        border: 1px solid rgba(255, 23, 68, 0.25) !important;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(255, 23, 68, 0.06);
    }
    
    .vibe-badge {
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
# Model ini digunakan untuk memprediksi status Social Battery pengguna
# (Energized (+1) vs Drained (-1)) berdasarkan parameter input harian.
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
        Prediksi kelas bipolar: +1 (Energized) atau -1 (Drained).
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
# Model ini digunakan untuk mengklasifikasikan suasana hati (Mood Vibe)
# ke dalam 4 kategori berdasarkan profil energi, tingkat sosial, dan fokus mental.
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
# Bipolar labels: +1 (Energized), -1 (Drained)
def generate_social_battery_dataset():
    np.random.seed(42)
    n_samples = 180
    
    # Fitur:
    # - Sleep Quality (0.0 s/d 1.0)
    # - Social Hours (Jam, normalisasi 0 s/d 10)
    # - Tasks Workload (Skala normalisasi 1 s/d 12)
    # - Me-time / Quiet Hours (Jam, normalisasi 0 s/d 8)
    sleep = np.random.uniform(0.1, 1.0, n_samples)
    social_h = np.random.uniform(0.0, 10.0, n_samples)
    workload = np.random.uniform(1.0, 12.0, n_samples)
    quiet_h = np.random.uniform(0.0, 8.0, n_samples)
    
    X_raw = np.column_stack((sleep, social_h, workload, quiet_h))
    
    # Normalisasi Min-Max ke [0, 1]
    norm_params = {
        'sleep_min': 0.1, 'sleep_max': 1.0,
        'social_min': 0.0, 'social_max': 10.0,
        'workload_min': 1.0, 'workload_max': 12.0,
        'quiet_min': 0.0, 'quiet_max': 8.0
    }
    
    X_norm = np.zeros_like(X_raw)
    X_norm[:, 0] = sleep
    X_norm[:, 1] = social_h / 10.0
    X_norm[:, 2] = (workload - 1.0) / 11.0
    X_norm[:, 3] = quiet_h / 8.0
    
    # Hubungan target:
    # Social battery positif jika sleep & quiet tinggi, negatif jika social & workload tinggi
    score = 0.55 * X_norm[:, 0] - 0.45 * X_norm[:, 1] - 0.35 * X_norm[:, 2] + 0.45 * X_norm[:, 3]
    # Tambahkan noise
    score += np.random.normal(0, 0.08, n_samples)
    
    # Konversi ke bipolar +1 atau -1
    y = np.where(score >= 0.0, 1, -1).reshape(-1, 1)
    
    return X_raw, X_norm, y, norm_params

# 2. Membuat data sintetis untuk training LVQ (Model 2)
# Masing-masing data merepresentasikan profil harian untuk 4 kategori mood/vibe
# Fitur: [Physical Energy, Social Desire, Cognitive Focus]
# Label: 
#   0: "Energetic & Focused"
#   1: "Calm & Chill"
#   2: "Anxious & Stressed"
#   3: "Exhausted & Gloomy"
def generate_mood_dataset():
    np.random.seed(99)
    n_samples = 160
    
    X = []
    y = []
    
    # Kelas 0: Energetic & Focused (Energi tinggi, Sosial sedang, Fokus tinggi)
    X.append(np.random.uniform([0.7, 0.2, 0.7], [1.0, 0.6, 1.0], (40, 3)))
    y.append(np.zeros(40, dtype=int))
    
    # Kelas 1: Calm & Chill (Energi sedang-rendah, Sosial sedang, Fokus sedang-rendah)
    X.append(np.random.uniform([0.3, 0.4, 0.1], [0.6, 0.8, 0.5], (40, 3)))
    y.append(np.ones(40, dtype=int))
    
    # Kelas 2: Anxious & Stressed (Energi tinggi, Sosial tinggi, Fokus rendah-sedang)
    X.append(np.random.uniform([0.6, 0.6, 0.2], [0.9, 1.0, 0.6], (40, 3)))
    y.append(np.ones(40, dtype=int) * 2)
    
    # Kelas 3: Exhausted & Gloomy (Energi rendah, Sosial rendah, Fokus rendah)
    X.append(np.random.uniform([0.0, 0.0, 0.0], [0.3, 0.3, 0.3], (40, 3)))
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
    _, X_adaline_train, y_adaline_train, norm_params = generate_social_battery_dataset()
    
    # Latih Model 1: Adaline (η = 0.1)
    ada_model = Adaline(input_dim=4, lr=0.1)
    ada_history = ada_model.train(X_adaline_train, y_adaline_train, epochs=800)
    
    # Latih model pembanding dengan η berbeda (untuk Analisis Bab IV)
    ada_lr_001 = Adaline(input_dim=4, lr=0.01)
    history_001 = ada_lr_001.train(X_adaline_train, y_adaline_train, epochs=800)
    
    ada_lr_05 = Adaline(input_dim=4, lr=0.5)
    history_05 = ada_lr_05.train(X_adaline_train, y_adaline_train, epochs=800)
    
    # 2. Ambil dataset LVQ & Latih Model 2: LVQ
    X_lvq_train, y_lvq_train = generate_mood_dataset()
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
    <h1 style="margin: 0; font-size: clamp(1.8rem, 5vw, 2.5rem); font-weight: 800; color: #ff007f; line-height: 1.2;">VIBESYNC: SOCIAL BATTERY & MOOD OPTIMIZER</h1>
    <p style="font-size: clamp(0.9rem, 2.5vw, 1.1rem); color: #a0aec0; margin-top: 10px; line-height: 1.4;">
        Asisten Klasifikasi Suasana Hati & Prediksi Kelelahan Sosial Berbasis JST (Adaline & LVQ)
    </p>
    <span style="background-color: #ff007f; color: #fff; padding: 4px 10px; border-radius: 20px; font-size: clamp(10px, 2vw, 11px); font-weight: bold; text-transform: uppercase;">
        Tugas Akhir Jaringan Saraf Tiruan (JST) - Adaline & LVQ
    </span>
</div>
""", unsafe_allow_html=True)

# SIDEBAR: PANEL INPUT USER (LANGKAH DEMI LANGKAH)
st.sidebar.markdown("""
<div style="background-color: #161925; padding: 15px; border-radius: 8px; border-left: 5px solid #ff007f; margin-bottom: 20px;">
    <h4 style="margin: 0; color: #ffffff;">LANGKAH 1: Aktivitas Sosial & Kerja</h4>
    <small style="color: #a0aec0;">Geser parameter di bawah untuk menggambarkan aktivitas Anda hari ini.</small>
</div>
""", unsafe_allow_html=True)

# Sidebar Inputs for Model 1 (Adaline)
sleep_quality = st.sidebar.slider("Kualitas Tidur (0.1 = Buruk, 1.0 = Sangat Nyenyak)", min_value=0.1, max_value=1.0, value=0.7, step=0.05)
social_hours = st.sidebar.slider("Durasi Bersosialisasi (Jam)", min_value=0.0, max_value=10.0, value=3.0, step=0.5)
workload_tasks = st.sidebar.slider("Jumlah Tugas / Beban Kerja", min_value=1, max_value=12, value=4)
quiet_hours = st.sidebar.slider("Durasi Me-Time / Waktu Tenang (Jam)", min_value=0.0, max_value=8.0, value=2.0, step=0.5)

st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style="background-color: #161925; padding: 15px; border-radius: 8px; border-left: 5px solid #00f0ff; margin-bottom: 20px;">
    <h4 style="margin: 0; color: #ffffff;">LANGKAH 2: Kondisi Energi & Fokus</h4>
    <small style="color: #a0aec0;">Masukkan indikator internal fisik dan mental Anda saat ini.</small>
</div>
""", unsafe_allow_html=True)

# Sidebar Inputs for Model 2 (LVQ)
physical_energy = st.sidebar.slider("Energi Fisik Saat Ini (0.0 = Habis, 1.0 = Bugar)", min_value=0.0, max_value=1.0, value=0.6, step=0.05)
social_desire = st.sidebar.slider("Hasrat Bersosialisasi (0.0 = Malas, 1.0 = Ingin)", min_value=0.0, max_value=1.0, value=0.5, step=0.05)
cognitive_focus = st.sidebar.slider("Tingkat Fokus Mental (0.0 = Kabur, 1.0 = Tajam)", min_value=0.0, max_value=1.0, value=0.7, step=0.05)


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
        <h3 style="margin-top: 0; color: #ff007f; font-size: clamp(1.2rem, 3.5vw, 1.6rem);">💡 Bagaimana Cara Kerja Aplikasi Ini?</h3>
        <p style="font-size: clamp(0.85rem, 2.5vw, 0.95rem); margin-bottom: 15px; color: #a0aec0;">
            Aplikasi ini memantau tingkat kesiapan mental dan suasana hati Anda menggunakan dua model <strong>Jaringan Saraf Tiruan (JST)</strong> yang berjalan secara real-time berdasarkan input yang Anda masukkan di panel kiri:
        </p>
        <div style="display: flex; gap: 15px; flex-wrap: wrap;">
            <div style="flex: 1; min-width: 250px; background-color: rgba(255,255,255,0.02); padding: 15px; border-radius: 12px; border-left: 4px solid #ff007f;">
                <strong style="color: #ffffff; font-size: clamp(0.9rem, 2.5vw, 1.05rem);">1. Prediksi Social Battery (Model Adaline)</strong>
                <p style="font-size: clamp(0.8rem, 2.2vw, 0.9rem); margin-top: 5px; color: #a0aec0; line-height: 1.4;">
                    Memprediksi apakah kapasitas bersosialisasi Anda dalam kondisi <strong>Energized</strong> atau sudah <strong>Drained</strong>. Model ini belajar memisahkan kedua kondisi tersebut berdasarkan data aktivitas harian Anda.
                </p>
            </div>
            <div style="flex: 1; min-width: 250px; background-color: rgba(255,255,255,0.02); padding: 15px; border-radius: 12px; border-left: 4px solid #00f0ff;">
                <strong style="color: #ffffff; font-size: clamp(0.9rem, 2.5vw, 1.05rem);">2. Klasifikasi Mood Vibe (Model LVQ)</strong>
                <p style="font-size: clamp(0.8rem, 2.2vw, 0.9rem); margin-top: 5px; color: #a0aec0; line-height: 1.4;">
                    Mendeteksi suasana hati Anda ke dalam salah satu dari 4 kategori mood utama. Model ini mencocokkan kondisi energi fisik, hasrat sosial, dan tingkat fokus Anda dengan profil suasana hati ideal.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("### Hasil Prediksi Hari Ini")
    
    col1, col2 = st.columns(2)
    
    # Model 1 (Adaline): Evaluasi Social Battery
    with col1:
        st.write("#### Prediksi Status Social Battery (Adaline)")
        
        # Jembatan Normalisasi untuk input real-time
        params = cached_data["norm_params"]
        norm_sleep = sleep_quality
        norm_social = social_hours / 10.0
        norm_workload = (workload_tasks - params['workload_min']) / (params['workload_max'] - params['workload_min'])
        norm_quiet = quiet_hours / 8.0
        
        input_adaline = np.array([[norm_sleep, norm_social, norm_workload, norm_quiet]])
        
        ada_model = cached_data["ada_model"]
        raw_score = ada_model.forward(input_adaline)[0][0]
        prediction_state = ada_model.predict(input_adaline)[0][0]
        
        # Penskalaan nilai mentah [-1.0 s/d 1.0] ke [0% s/d 100%]
        battery_pct = int(np.clip((raw_score + 1.0) / 2.0 * 100.0, 0, 100))
        
        if prediction_state == 1:
            st.markdown(f"""
            <div class="card-battery-high" style="padding: clamp(15px, 3vw, 20px);">
                <h2 style="margin: 0; color: #00e676; font-size: clamp(1.3rem, 4vw, 1.7rem);">ENERGIZED (+1)</h2>
                <h3 style="margin: 5px 0 12px 0; color: #ffffff; font-size: clamp(1.0rem, 3vw, 1.3rem);">Social Battery Anda: {battery_pct}%</h3>
                <p style="font-size: clamp(0.85rem, 2.5vw, 0.95rem); margin: 0; line-height: 1.4;">Status baterai sosial Anda saat ini aman. Anda memiliki energi yang cukup untuk menghadiri pertemuan sosial, berkolaborasi, atau melanjutkan pekerjaan yang padat.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="card-battery-low" style="padding: clamp(15px, 3vw, 20px);">
                <h2 style="margin: 0; color: #ff1744; font-size: clamp(1.3rem, 4vw, 1.7rem);">DRAINED (-1)</h2>
                <h3 style="margin: 5px 0 12px 0; color: #ffffff; font-size: clamp(1.0rem, 3vw, 1.3rem);">Social Battery Anda: {battery_pct}%</h3>
                <p style="font-size: clamp(0.85rem, 2.5vw, 0.95rem); margin: 0; line-height: 1.4;">Status baterai sosial Anda terkuras. Disarankan untuk membatasi interaksi sosial luar, luangkan waktu untuk me-time, dan lakukan pemulihan mental malam ini.</p>
            </div>
            """, unsafe_allow_html=True)
            
        st.progress(battery_pct / 100.0)
        
        # Penjelasan Keputusan UX
        st.markdown(f"""
        <div style="background-color: rgba(255, 255, 255, 0.01); border: 1px dashed rgba(255,255,255,0.1); padding: 15px; border-radius: 8px; margin-top: 15px; font-size: 13px;">
            <strong style="color: #ffffff;">Bagaimana model mengambil keputusan ini?</strong><br/>
            Model Adaline mengalikan nilai input harian Anda dengan bobot latihnya secara linear. Hasil akumulasinya adalah <strong>{raw_score:.3f}</strong>. Karena nilai ini {"lebih besar dari atau sama dengan 0" if raw_score >= 0 else "kurang dari 0"}, sistem mengklasifikasikan Anda sebagai <strong>{"ENERGIZED" if prediction_state == 1 else "DRAINED"}</strong>.
        </div>
        """, unsafe_allow_html=True)

        # Tampilan metrik input Adaline
        st.write("")
        st.write("**Detail Parameter Input & Hasil Normalisasi:**")
        df_adaline = pd.DataFrame({
            "Parameter": ["Kualitas Tidur", "Jam Sosial", "Tugas Kerja", "Jam Me-time"],
            "Nilai Input": [f"{sleep_quality:.2f}", f"{social_hours} jam", f"{workload_tasks} tugas", f"{quiet_hours} jam"],
            "Nilai Normalisasi (Skala 0-1)": [f"{norm_sleep:.3f}", f"{norm_social:.3f}", f"{norm_workload:.3f}", f"{norm_quiet:.3f}"]
        })
        st.table(df_adaline)

    # Model 2 (LVQ): Klasifikasi Mood Vibe
    with col2:
        st.write("#### Klasifikasi Mood Vibe (LVQ)")
        
        input_lvq = np.array([[physical_energy, social_desire, cognitive_focus]])
        lvq_model = cached_data["lvq_model"]
        predicted_class = lvq_model.predict(input_lvq)[0]
        
        moods = {
            0: {"title": "Energetic & Focused", "color": "#ffea00", "desc": "Tingkat energi dan konsentrasi Anda optimal. Waktu terbaik untuk menyelesaikan tugas sulit, coding, atau belajar materi baru."},
            1: {"title": "Calm & Chill", "color": "#00e5ff", "desc": "Kondisi emosi santai dan damai. Cocok untuk membaca buku, mendengarkan musik lambat, atau berdiskusi santai."},
            2: {"title": "Anxious & Stressed", "color": "#ff9100", "desc": "Ada ketegangan internal yang tinggi. Cobalah untuk mengambil napas dalam-dalam, kurangi asupan kafein, dan hindari konflik sosial sementara waktu."},
            3: {"title": "Exhausted & Gloomy", "color": "#d500f9", "desc": "Kelelahan fisik dan mental yang menumpuk. Rekomendasi terbaik adalah menghentikan aktivitas berat dan segera tidur siang atau istirahat total."}
        }
        
        current_mood = moods[predicted_class]
        
        st.markdown(f"""
        <div style="background-color: rgba(255, 255, 255, 0.03); border: 2px solid {current_mood['color']}; border-radius: 16px; padding: clamp(15px, 3vw, 20px); box-shadow: 0 8px 32px 0 rgba(0,0,0,0.2);">
            <h2 style="margin: 0; color: {current_mood['color']}; font-size: clamp(1.3rem, 4vw, 1.7rem);">{current_mood['title'].upper()}</h2>
            <p style="margin-top: 10px; font-size: clamp(0.85rem, 2.5vw, 0.95rem); margin-bottom: 0; line-height: 1.4;">{current_mood['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Penjelasan Keputusan UX
        st.markdown(f"""
        <div style="background-color: rgba(255, 255, 255, 0.01); border: 1px dashed rgba(255,255,255,0.1); padding: 15px; border-radius: 8px; margin-top: 15px; font-size: clamp(0.8rem, 2.2vw, 0.85rem);">
            <strong style="color: #ffffff;">Bagaimana model mengambil keputusan ini?</strong><br/>
            Model LVQ membandingkan koordinat input Anda <strong>[{physical_energy:.2f}, {social_desire:.2f}, {cognitive_focus:.2f}]</strong> dengan 4 pusat profil mood (prototipe). Profil mood <strong>{current_mood['title']}</strong> dideteksi memiliki jarak Euclidean terdekat dengan posisi Anda saat ini.
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        st.write("#### Rekomendasi Aktivitas Berdasarkan Vibe")
        st.write("Berdasarkan suasana hati yang dideteksi, aktivitas harian berikut dipetakan secara real-time ke mood Anda saat ini:")
        
        # Cari BMU untuk beberapa aktivitas contoh
        sample_activities = [
            {"name": "Coding & Belajar Intensif", "v": [0.8, 0.2, 0.95]},
            {"name": "Diskusi Kelompok / Rapat", "v": [0.7, 0.8, 0.75]},
            {"name": "Menonton Film / Netflix", "v": [0.3, 0.4, 0.2]},
            {"name": "Bermain Futsal / Gym", "v": [0.95, 0.7, 0.3]},
            {"name": "Tidur & Istirahat Total", "v": [0.05, 0.0, 0.05]}
        ]
        
        for act in sample_activities:
            bmu_idx, _ = lvq_model.find_bmu(np.array(act["v"]))
            vibe_info = moods[bmu_idx]
            st.markdown(f"""
            <div class="vibe-badge" style="border-left: 4px solid {vibe_info['color']} !important; padding: clamp(10px, 2.5vw, 15px); font-size: clamp(0.85rem, 2.4vw, 0.95rem);">
                <strong>{act['name']}</strong> → <span style="color: {vibe_info['color']}; font-weight: bold;">{vibe_info['title']}</span>
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
    norm_sleep_val = sleep_quality
    norm_social_val = social_hours / 10.0
    norm_workload_val = (workload_tasks - params['workload_min']) / (params['workload_max'] - params['workload_min'])
    norm_quiet_val = quiet_hours / 8.0
    
    input_adaline = np.array([[norm_sleep_val, norm_social_val, norm_workload_val, norm_quiet_val]])
    current_prediction_state = ada_model.predict(input_adaline)[0][0]

    st.markdown("""
    <div style="background-color: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 12px; padding: 20px; margin-bottom: 25px;">
        <h4 style="margin-top:0; color: #ff007f;">📊 Panduan Membaca Grafik Visualisasi</h4>
        <p style="font-size: 13.5px; margin-bottom: 0; color: #a0aec0;">
            Tab ini memaparkan visualisasi performa latih model dan hubungan posisi input Anda dengan batas klasifikasi. Kolom kiri memvisualisasikan model <strong>Adaline</strong> (baterai sosial), sedangkan kolom kanan memvisualisasikan model <strong>LVQ</strong> (mood).
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
        st.caption("Plot 2D di bawah ini memproyeksikan data training Kualitas Tidur (x-axis) vs Beban Kerja (y-axis). Garis merah muda adalah Batas Keputusan (Decision Boundary). Simbol bintang melambangkan posisi Anda secara real-time. Gerakkan slider Kualitas Tidur atau Beban Kerja di sidebar untuk melihat pergeseran posisi bintang.")
        
        # Ambil bobot Adaline
        W = ada_model.W.flatten()
        b = ada_model.b[0][0]
        
        # Gambar plot 2D: Sleep Quality (X) vs Workload Tasks (Y)
        fig_bound, ax_bound = plt.subplots(figsize=(6, 4), facecolor='#0d111e')
        ax_bound.set_facecolor('#0d111e')
        
        # Plot training data points
        _, X_adaline_norm, y_adaline_val, _ = generate_social_battery_dataset()
        energized_mask = (y_adaline_val == 1).flatten()
        drained_mask = (y_adaline_val == -1).flatten()
        
        ax_bound.scatter(X_adaline_norm[energized_mask, 0], X_adaline_norm[energized_mask, 2], color='#00e676', alpha=0.3, label='Data Energized (+1)', s=15)
        ax_bound.scatter(X_adaline_norm[drained_mask, 0], X_adaline_norm[drained_mask, 2], color='#ff1744', alpha=0.3, label='Data Drained (-1)', s=15)
        
        # Hitung garis batas keputusan: W[0]*x1 + W[1]*x2 + W[2]*x3 + W[3]*x4 + b = 0
        # Di mana x2 (social) dan x4 (quiet) adalah posisi slider saat ini.
        # Maka x3 (workload) = -(W[0]*x1 + W[1]*x2 + W[3]*x4 + b) / W[2]
        x1_vals = np.linspace(0, 1.0, 100)
        if abs(W[2]) > 1e-5:
            x3_vals = -(W[0] * x1_vals + W[1] * norm_social_val + W[3] * norm_quiet_val + b) / W[2]
            ax_bound.plot(x1_vals, x3_vals, color='#ff007f', linewidth=2, label='Decision Boundary (net=0)')
            ax_bound.fill_between(x1_vals, -0.2, x3_vals, color='#ff1744', alpha=0.05)
            ax_bound.fill_between(x1_vals, x3_vals, 1.2, color='#00e676', alpha=0.05)
        
        # Plot posisi pengguna saat ini
        color_pos = '#00e676' if current_prediction_state == 1 else '#ff1744'
        ax_bound.scatter(norm_sleep_val, norm_workload_val, color=color_pos, edgecolor='white', s=200, marker='*', label='Posisi Anda', zorder=5)
        
        ax_bound.set_xlim(-0.05, 1.05)
        ax_bound.set_ylim(-0.05, 1.05)
        ax_bound.set_xlabel("Normalized Kualitas Tidur (x1)")
        ax_bound.set_ylabel("Normalized Beban Kerja (x3)")
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
        st.caption("Tabel di bawah memuat bobot latih akhir (koordinat ideal) dari 4 pusat kelas mood di ruang input:")
        
        proto_df = pd.DataFrame(
            lvq_model.prototypes,
            columns=["Energi Fisik", "Desir Sosial", "Fokus Mental"],
            index=["Kelas 0: Energetic & Focused", "Kelas 1: Calm & Chill", "Kelas 2: Anxious & Stressed", "Kelas 3: Exhausted & Gloomy"]
        )
        st.dataframe(proto_df.style.background_gradient(cmap="plasma", axis=None))

        st.write("#### Pemetaan Vektor Prototipe & Posisi Anda (3D)")
        st.caption("Ruang 3D di bawah ini memvisualisasikan posisi 4 prototipe mood (bola berwarna) dan posisi Anda saat ini (simbol X berwarna merah muda). Garis penghubung lurus tebal menunjukkan prototipe terdekat (BMU) yang memenangkan klasifikasi input Anda.")
        
        # Data input saat ini
        user_vec = np.array([physical_energy, social_desire, cognitive_focus])
        
        fig_3d = plt.figure(figsize=(6, 5), facecolor='#0d111e')
        ax_3d = fig_3d.add_subplot(111, projection='3d', facecolor='#0d111e')
        
        # Atur warna panel 3D
        ax_3d.xaxis.set_pane_color((0.05, 0.07, 0.12, 1.0))
        ax_3d.yaxis.set_pane_color((0.05, 0.07, 0.12, 1.0))
        ax_3d.zaxis.set_pane_color((0.05, 0.07, 0.12, 1.0))
        
        # Plot Prototypes
        protos = lvq_model.prototypes
        colors_3d = ['#ffea00', '#00e5ff', '#ff9100', '#d500f9']
        labels_3d = ['Energetic & Focused', 'Calm & Chill', 'Anxious & Stressed', 'Exhausted & Gloomy']
        
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
            
        ax_3d.set_xlabel("Energi Fisik", color='white')
        ax_3d.set_ylabel("Desir Sosial", color='white')
        ax_3d.set_zlabel("Fokus Mental", color='white')
        ax_3d.tick_params(colors='white')
        ax_3d.xaxis.label.set_color('white')
        ax_3d.yaxis.label.set_color('white')
        ax_3d.zaxis.label.set_color('white')
        ax_3d.grid(True, color='white', alpha=0.05)
        ax_3d.legend(facecolor='#0d111e', labelcolor='white', loc='upper left', prop={'size': 8})
        
        st.pyplot(fig_3d)
        plt.close(fig_3d)

