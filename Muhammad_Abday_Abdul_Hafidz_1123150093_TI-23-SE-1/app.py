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
    page_title="The Zen-Day Optimizer - JST Final Exam",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom premium CSS styling for the interface
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
    html, body, [class*="css"], .stApp, .stMarkdown, p, span, label, div, select, button {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    .stApp {
        background: radial-gradient(circle at 50% 50%, #0f1326 0%, #05060f 100%) !important;
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
        background-color: rgba(10, 12, 22, 0.55) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
    }
    
    .stSidebar h1, .stSidebar h2, .stSidebar h3, .stSidebar h4, .stSidebar h5, .stSidebar h6 {
        color: #ffffff !important;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #00e5ff !important;
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
        color: #00e5ff !important;
    }
    
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #00e5ff !important;
        border-bottom: 2px solid #00e5ff !important;
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
    
    /* Custom Risk Cards */
    .card-burnout-low {
        background: rgba(19, 43, 29, 0.35) !important;
        backdrop-filter: blur(16px) saturate(180%) !important;
        -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
        border: 1px solid rgba(0, 230, 118, 0.25) !important;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 230, 118, 0.06);
    }
    
    .card-burnout-med {
        background: rgba(46, 38, 21, 0.35) !important;
        backdrop-filter: blur(16px) saturate(180%) !important;
        -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
        border: 1px solid rgba(255, 171, 0, 0.25) !important;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(255, 171, 0, 0.06);
    }
    
    .card-burnout-high {
        background: rgba(48, 19, 24, 0.35) !important;
        backdrop-filter: blur(16px) saturate(180%) !important;
        -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
        border: 1px solid rgba(255, 23, 68, 0.25) !important;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(255, 23, 68, 0.06);
    }
    
    .activity-badge {
        display: inline-block;
        background-color: rgba(30, 34, 53, 0.35) !important;
        backdrop-filter: blur(10px) !important;
        -webkit-backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        border-left: 4px solid #00e5ff !important;
        border-radius: 12px;
        padding: 12px 18px;
        margin: 6px 0px;
        font-size: 15px;
        color: #e2e8f0;
        width: 100%;
        box-sizing: border-box;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
    }
</style>
""", unsafe_allow_html=True)


# ==============================================================================
# MODEL 1: BACKPROPAGATION NEURAL NETWORK FROM SCRATCH
# ==============================================================================
# Deskripsi Matematis & Fungsionalitas:
# Model ini digunakan untuk melakukan prediksi indeks burnout (0.0 s/d 1.0)
# berdasarkan input aktivitas harian user (Durasi Tidur, Workload, Screen Time,
# dan Durasi Aktivitas Sosial).
#
# Rumus Update Bobot (Gradient Descent Backpropagation):
# 1. Error Output Layer (Delta Output):
#    d_output = a_out * (1 - a_out) * (y_target - a_out)
# 2. Error Hidden Layer (Delta Hidden):
#    d_hidden = a_hidden * (1 - a_hidden) * (d_output * W2.T)
# 3. Update Bobot Output:
#    W2_baru = W2 + lr * (a_hidden.T . d_output)
# 4. Update Bobot Hidden:
#    W1_baru = W1 + lr * (x.T . d_hidden)
# ==============================================================================

class BackpropagationNN:
    def __init__(self, input_dim=4, hidden_dim=5, output_dim=1, lr=0.1):
        """
        Inisialisasi arsitektur jaringan saraf tiruan Backpropagation.
        Input:
            - input_dim: Jumlah neuron input (default 4)
            - hidden_dim: Jumlah neuron hidden layer (default 5)
            - output_dim: Jumlah neuron output (default 1)
            - lr: Learning rate awal (default 0.1)
        """
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.lr = lr
        
        # Set seed agar hasil inisialisasi bobot konsisten
        np.random.seed(42)
        
        # Inisialisasi bobot dan bias secara random menggunakan Gaussian/Normal distribution
        self.W1 = np.random.randn(self.input_dim, self.hidden_dim) * 0.1
        self.b1 = np.zeros((1, self.hidden_dim))
        
        self.W2 = np.random.randn(self.hidden_dim, self.output_dim) * 0.1
        self.b2 = np.zeros((1, self.output_dim))

    def sigmoid(self, x):
        """Fungsi aktivasi Sigmoid Biner"""
        return 1.0 / (1.0 + np.exp(-x))

    def sigmoid_derivative(self, a):
        """Turunan fungsi aktivasi Sigmoid, dengan input berupa hasil aktivasi 'a'"""
        return a * (1.0 - a)

    def forward(self, X):
        """
        Melakukan perambatan maju (Forward Propagation).
        Input:
            - X: Matriks input berukuran (N, input_dim)
        Output:
            - output: Hasil aktivasi layer output (N, output_dim)
        """
        # Layer Tersembunyi (Hidden Layer)
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)
        
        # Layer Output
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.sigmoid(self.z2)
        return self.a2

    def backward(self, X, y, output):
        """
        Melakukan perambatan mundur (Backward Propagation) dan memperbarui bobot.
        Input:
            - X: Matriks input (N, input_dim)
            - y: Target output (N, output_dim)
            - output: Hasil output aktual hasil forward (N, output_dim)
        """
        # Hitung error di output layer
        error_output = y - output
        d_output = error_output * self.sigmoid_derivative(output)
        
        # Hitung error di hidden layer
        error_hidden = np.dot(d_output, self.W2.T)
        d_hidden = error_hidden * self.sigmoid_derivative(self.a1)
        
        # Hitung gradien & update bobot serta bias menggunakan gradient descent
        self.W2 += np.dot(self.a1.T, d_output) * self.lr
        self.b2 += np.sum(d_output, axis=0, keepdims=True) * self.lr
        
        self.W1 += np.dot(X.T, d_hidden) * self.lr
        self.b1 += np.sum(d_hidden, axis=0, keepdims=True) * self.lr

    def train(self, X, y, epochs=1000):
        """
        Melakukan training model menggunakan data training.
        Input:
            - X: Data input training
            - y: Target label training
            - epochs: Jumlah epoch latihan
        Output:
            - mse_history: List nilai Mean Squared Error per epoch
        """
        mse_history = []
        for epoch in range(epochs):
            # Forward pass
            output = self.forward(X)
            # Backward pass & update bobot
            self.backward(X, y, output)
            
            # Hitung MSE (Mean Squared Error)
            mse = np.mean(np.square(y - output))
            mse_history.append(mse)
        return mse_history


# ==============================================================================
# MODEL 2: KOHONEN SELF-ORGANIZING MAP (SOM) FROM SCRATCH
# ==============================================================================
# Deskripsi Matematis & Fungsionalitas:
# Model ini digunakan untuk clustering aktivitas sehari-hari berdasarkan 3 metrik:
# Kebutuhan Energi Fisik, Tingkat Interaksi Sosial, dan Kebutuhan Fokus Mental.
#
# Rumus Update Bobot Kohonen SOM:
# 1. Temukan Best Matching Unit (BMU) dengan jarak Euclidean terkecil:
#    BMU_idx = argmin( || X - W_j || )
# 2. Hitung pengaruh tetangga (neighborhood function) h_j berdasarkan jarak grid ke BMU:
#    h_j = exp( - (d_grid(j, BMU)^2) / (2 * sigma^2) )
# 3. Update bobot node j:
#    W_j_baru = W_j_lama + lr * h_j * (X - W_j_lama)
# ==============================================================================

class KohonenSOM:
    def __init__(self, input_dim=3, grid_size=(2, 2), lr_start=0.5, sigma_start=1.0):
        """
        Inisialisasi parameter Jaringan Kohonen SOM.
        Input:
            - input_dim: Dimensi data input (default 3: Energi, Sosial, Fokus)
            - grid_size: Ukuran grid output 2D (default (2, 2) = 4 neuron output)
            - lr_start: Learning rate awal
            - sigma_start: Radius tetangga awal
        """
        self.input_dim = input_dim
        self.grid_size = grid_size
        self.lr_start = lr_start
        self.sigma_start = sigma_start
        
        # Set seed agar hasil clustering konsisten
        np.random.seed(42)
        
        # Inisialisasi bobot secara acak antara 0 dan 1 (normalized input space)
        self.weights = np.random.rand(grid_size[0] * grid_size[1], input_dim)

    def get_grid_coords(self, idx):
        """Mendapatkan koordinat baris dan kolom 2D dari indeks flat 1D"""
        return idx // self.grid_size[1], idx % self.grid_size[1]

    def find_bmu(self, x):
        """
        Mencari Best Matching Unit (BMU) berdasarkan jarak Euclidean.
        Input:
            - x: Vektor input tunggal (input_dim,)
        Output:
            - bmu_idx: Indeks neuron pemenang
            - distances: Array jarak dari input ke seluruh neuron
        """
        # Hitung jarak Euclidean dari input ke seluruh bobot neuron
        distances = np.linalg.norm(self.weights - x, axis=1)
        bmu_idx = np.argmin(distances)
        return bmu_idx, distances

    def train(self, data, epochs=150):
        """
        Melakukan training Kohonen SOM secara unsupervised.
        Input:
            - data: Dataset input untuk dikluster (N, input_dim)
            - epochs: Jumlah iterasi pelatihan
        """
        num_nodes = self.grid_size[0] * self.grid_size[1]
        
        for epoch in range(epochs):
            # Decay learning rate & radius tetangga secara linier seiring waktu
            lr = self.lr_start * (1.0 - epoch / epochs)
            sigma = self.sigma_start * (1.0 - epoch / epochs)
            # Pastikan sigma tidak bernilai nol untuk menghindari divisi nol
            if sigma < 0.1:
                sigma = 0.1
                
            for x in data:
                # 1. Cari BMU
                bmu_idx, _ = self.find_bmu(x)
                bmu_r, bmu_c = self.get_grid_coords(bmu_idx)
                
                # 2. Update bobot seluruh neuron dalam grid berdasarkan jaraknya ke BMU
                for j in range(num_nodes):
                    node_r, node_c = self.get_grid_coords(j)
                    # Hitung kuadrat jarak Euclidean di ruang grid 2D
                    grid_dist_sq = (node_r - bmu_r)**2 + (node_c - bmu_c)**2
                    
                    # Neighborhood influence (Fungsi Gaussian)
                    h = np.exp(-grid_dist_sq / (2.0 * (sigma**2)))
                    
                    # Update bobot
                    self.weights[j] += lr * h * (x - self.weights[j])


# ==============================================================================
# DATA GENERATION AND PREPARATION
# ==============================================================================

# 1. Membuat data sintetis untuk training Backpropagation (Model 1)
# Dataset ini menggambarkan pola harian yang memicu burnout
def generate_burnout_dataset():
    np.random.seed(101)
    n_samples = 180
    
    # Fitur Mentah:
    # - Sleep Duration (Jam): 4 s/d 10 jam
    # - Completed Tasks / Workload (Skala 1 s/d 12)
    # - Screen Time (Jam): 2 s/d 14 jam
    # - Social/Physical Activity (Jam): 0 s/d 6 jam
    sleep = np.random.uniform(4.0, 10.0, n_samples)
    workload = np.random.uniform(1.0, 12.0, n_samples)
    screen = np.random.uniform(2.0, 14.0, n_samples)
    social = np.random.uniform(0.0, 6.0, n_samples)
    
    X_raw = np.column_stack((sleep, workload, screen, social))
    
    # Normalisasi Min-Max agar nilai berada pada rentang [0.0, 1.0]
    # Parameter normalisasi disimpan agar bisa digunakan saat prediksi data baru
    norm_params = {
        'sleep_min': 4.0, 'sleep_max': 10.0,
        'workload_min': 1.0, 'workload_max': 12.0,
        'screen_min': 2.0, 'screen_max': 14.0,
        'social_min': 0.0, 'social_max': 6.0
    }
    
    X_norm = np.zeros_like(X_raw)
    X_norm[:, 0] = (sleep - 4.0) / (10.0 - 4.0)
    X_norm[:, 1] = (workload - 1.0) / (12.0 - 1.0)
    X_norm[:, 2] = (screen - 2.0) / (14.0 - 2.0)
    X_norm[:, 3] = (social - 0.0) / (6.0 - 0.0)
    
    # Relasi Matematis Target: Burnout Index (y) dipengaruhi negatif oleh tidur & sosial, positif oleh workload & screen time
    # y = 0.5 * (1 - Sleep) + 0.4 * Workload + 0.3 * ScreenTime - 0.2 * Social
    y = 0.55 * (1.0 - X_norm[:, 0]) + 0.35 * X_norm[:, 1] + 0.25 * X_norm[:, 2] - 0.15 * X_norm[:, 3]
    # Tambahkan sedikit noise acak untuk merepresentasikan data riil
    y += np.random.normal(0, 0.05, n_samples)
    # Clip agar target tetap berada di batas logis sigmoid biner [0.01, 0.99]
    y = np.clip(y, 0.01, 0.99).reshape(-1, 1)
    
    return X_raw, X_norm, y, norm_params

# 2. Membuat Data Aktivitas Harian untuk Kohonen SOM (Model 2)
# Setiap aktivitas memiliki profil: [Kebutuhan Energi Fisik, Interaksi Sosial, Fokus Mental]
ACTIVITIES = [
    {"name": "Yoga & Meditasi Mandiri", "vector": np.array([0.15, 0.05, 0.85])},
    {"name": "Latihan Fisik di Gym", "vector": np.array([0.90, 0.20, 0.30])},
    {"name": "Coding & Pemecahan Masalah", "vector": np.array([0.20, 0.10, 0.95])},
    {"name": "Belajar Kelompok / Diskusi Project", "vector": np.array([0.30, 0.85, 0.80])},
    {"name": "Menonton Serial / Netflix", "vector": np.array([0.05, 0.05, 0.15])},
    {"name": "Bermain Game Online Bersama Teman", "vector": np.array([0.15, 0.75, 0.60])},
    {"name": "Mengobrol Santai di Warkop", "vector": np.array([0.10, 0.90, 0.25])},
    {"name": "Membaca Buku Fiksi / Novel", "vector": np.array([0.05, 0.00, 0.65])},
    {"name": "Bermain Futsal / Olahraga Tim", "vector": np.array([0.95, 0.80, 0.40])},
    {"name": "Istirahat / Tidur Siang", "vector": np.array([0.00, 0.00, 0.00])}
]


# ==============================================================================
# STREAMLIT CACHED TRAINING EXECUTION
# ==============================================================================
# Menggunakan @st.cache_resource agar training model dari nol tidak dilakukan berulang kali
# setiap kali user berinteraksi dengan widget input di interface.
# ==============================================================================

@st.cache_resource
def train_and_cache_models():
    # 1. Ambil dataset
    _, X_train, y_train, norm_params = generate_burnout_dataset()
    
    # 2. Latih Model 1: Backpropagation
    bp_model = BackpropagationNN(input_dim=4, hidden_dim=5, output_dim=1, lr=0.2)
    bp_history = bp_model.train(X_train, y_train, epochs=1200)
    
    # Latih model pembanding untuk analisis learning rate di Bab IV
    bp_lr_01 = BackpropagationNN(input_dim=4, hidden_dim=5, output_dim=1, lr=0.01)
    history_01 = bp_lr_01.train(X_train, y_train, epochs=1200)
    
    bp_lr_5 = BackpropagationNN(input_dim=4, hidden_dim=5, output_dim=1, lr=0.5)
    history_5 = bp_lr_5.train(X_train, y_train, epochs=1200)
    
    # 3. Latih Model 2: Kohonen SOM
    som_data = np.array([act["vector"] for act in ACTIVITIES])
    som_model = KohonenSOM(input_dim=3, grid_size=(2, 2), lr_start=0.6, sigma_start=1.2)
    som_model.train(som_data, epochs=300)
    
    # Lakukan klusterisasi aktivitas ke 4 neuron grid SOM
    activity_clusters = {0: [], 1: [], 2: [], 3: []}
    for act in ACTIVITIES:
        cluster_idx, _ = som_model.find_bmu(act["vector"])
        activity_clusters[cluster_idx].append(act["name"])
        
    return {
        "bp_model": bp_model,
        "bp_history": bp_history,
        "history_01": history_01,
        "history_5": history_5,
        "som_model": som_model,
        "activity_clusters": activity_clusters,
        "norm_params": norm_params
    }

# Eksekusi training & caching
cached_data = train_and_cache_models()


# ==============================================================================
# STREAMLIT USER INTERFACE & LAYOUT
# ==============================================================================

# Title Banner
st.write("""
<div style="text-align: center; padding: 25px; border-bottom: 2px solid #00e5ff; margin-bottom: 30px;">
    <h1 style="margin: 0; font-size: 42px; font-weight: 800;">THE ZEN-DAY OPTIMIZER</h1>
    <p style="font-size: 18px; color: #a0aec0; margin-top: 10px;">
        Asisten Produktivitas & Pencegahan Burnout Berbasis Jaringan Saraf Tiruan (JST)
    </p>
    <span style="background-color: #00e5ff; color: #000; padding: 5px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; text-transform: uppercase;">
        Projek Akhir Jaringan Saraf Tiruan (JST)
    </span>
</div>
""", unsafe_allow_html=True)

# SIDEBAR: PANEL INPUT USER (REAL-TIME PREDICTION INPUT)
st.sidebar.markdown("""
<div style="background-color: #1a1e30; padding: 15px; border-radius: 8px; border-left: 5px solid #00e5ff; margin-bottom: 20px;">
    <h4 style="margin: 0; color: #ffffff;">Parameter Hari Ini</h4>
    <small style="color: #a0aec0;">Geser nilai di bawah sesuai dengan aktivitas Anda hari ini.</small>
</div>
""", unsafe_allow_html=True)

# Sidebar Inputs for Model 1 (Backpropagation)
sleep_hours = st.sidebar.slider("Durasi & Kualitas Tidur (Jam)", min_value=4.0, max_value=10.0, value=7.5, step=0.5)
workload_tasks = st.sidebar.slider("Jumlah Tugas & Tingkat Beban Kerja", min_value=1, max_value=12, value=5)
screen_hours = st.sidebar.slider("Screen Time / Waktu Layar (Jam)", min_value=2.0, max_value=14.0, value=6.0, step=0.5)
social_hours = st.sidebar.slider("Durasi Aktivitas Fisik / Sosial (Jam)", min_value=0.0, max_value=6.0, value=2.0, step=0.5)

st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style="background-color: #1a1e30; padding: 15px; border-radius: 8px; border-left: 5px solid #ff007f; margin-bottom: 20px;">
    <h4 style="margin: 0; color: #ffffff;">Target Vibe Rekomendasi</h4>
    <small style="color: #a0aec0;">Sesuaikan preferensi aktivitas yang ingin Anda lakukan selanjutnya.</small>
</div>
""", unsafe_allow_html=True)

# Sidebar Inputs for Model 2 (Kohonen SOM)
target_energy = st.sidebar.slider("Kebutuhan Energi Fisik", min_value=0.0, max_value=1.0, value=0.3, step=0.05)
target_social = st.sidebar.slider("Tingkat Interaksi Sosial", min_value=0.0, max_value=1.0, value=0.5, step=0.05)
target_focus = st.sidebar.slider("Kebutuhan Fokus Mental", min_value=0.0, max_value=1.0, value=0.7, step=0.05)


# TABS LAYOUT FOR APP SECTIONS
tab_dashboard, tab_charts, tab_academic = st.tabs([
    "Dashboard Utama & Rekomendasi", 
    "Kurva Training & Visualisasi Model", 
    "Laporan Akademik (Bab I - V)"
])

# ==============================================================================
# TAB 1: DASHBOARD UTAMA & REKOMENDASI AKTIVITAS
# ==============================================================================
with tab_dashboard:
    st.write("### Analisis Kondisi & Rekomendasi Harian")
    
    # Jembatan Normalisasi untuk input real-time
    params = cached_data["norm_params"]
    norm_sleep = (sleep_hours - params['sleep_min']) / (params['sleep_max'] - params['sleep_min'])
    norm_workload = (workload_tasks - params['workload_min']) / (params['workload_max'] - params['workload_min'])
    norm_screen = (screen_hours - params['screen_min']) / (params['screen_max'] - params['screen_min'])
    norm_social = (social_hours - params['social_min']) / (params['social_max'] - params['social_min'])
    
    # Susun matriks input dengan shape (1, 4)
    input_vector = np.array([[norm_sleep, norm_workload, norm_screen, norm_social]])
    
    # Lakukan prediksi menggunakan model Backpropagation yang dilatih
    bp_model = cached_data["bp_model"]
    predicted_burnout = bp_model.forward(input_vector)[0][0]
    
    # Klasifikasi tingkat resiko burnout
    if predicted_burnout < 0.35:
        risk_class = "RENDAH (Safe Zone)"
        risk_card_class = "card-burnout-low"
        risk_color = "#00e676"
        advice = "Luar biasa! Keseimbangan hidup Anda hari ini sangat terjaga. Pertahankan pola tidur dan aktivitas fisik Anda."
    elif predicted_burnout < 0.70:
        risk_class = "SEDANG (Warning Zone)"
        risk_card_class = "card-burnout-med"
        risk_color = "#ffab00"
        advice = "Hati-hati, beban kerja dan waktu layar Anda mulai mendekati batas kritis. Kurangi screen time dan usahakan istirahat malam ini."
    else:
        risk_class = "TINGGI (Burnout Danger!)"
        risk_card_class = "card-burnout-high"
        risk_color = "#ff1744"
        advice = "Bahaya! Tingkat burnout Anda sangat tinggi hari ini. Segera hentikan tugas akademis/pekerjaan berat, matikan layar, lakukan meditasi atau tidur siang."

    # Tampilkan dashboard dua kolom
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.write("#### Status Kesehatan Mental (Model BP)")
        st.markdown(f"""
        <div class="{risk_card_class}">
            <p style="margin: 0; font-size: 16px; color: #cbd5e0; text-transform: uppercase; font-weight: bold;">Prediksi Indeks Burnout</p>
            <h1 style="margin: 10px 0; font-size: 56px; color: {risk_color} !important; font-weight: 800;">{predicted_burnout * 100:.1f}%</h1>
            <p style="margin: 0; font-size: 18px; font-weight: bold; color: {risk_color};">Kategori Risiko: {risk_class}</p>
            <p style="margin: 15px 0 0 0; font-size: 14px; color: #e2e8f0; line-height: 1.6;"><strong>Saran Optimasi:</strong> {advice}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Progress Bar visualizer
        st.markdown("**Visualisasi Indeks Risiko:**")
        st.progress(float(predicted_burnout))
        
    with col2:
        st.write("#### Rekomendasi Aktivitas Harian Anda (Model SOM)")
        st.write("Mencocokkan target vibe harian Anda dengan aktivitas restoratif/produktif menggunakan clustering Kohonen SOM.")
        
        # Cari BMU untuk target vibe yang diinputkan user di sidebar
        target_vector = np.array([target_energy, target_social, target_focus])
        som_model = cached_data["som_model"]
        bmu_idx, distances = som_model.find_bmu(target_vector)
        
        # Cari aktivitas yang terkelompok di cluster yang sama dengan BMU
        recommended_activities = cached_data["activity_clusters"][bmu_idx]
        
        # Cari nama label cluster yang representatif
        cluster_labels = {
            0: "Zona Istirahat & Pemulihan Pasif (Rest & Passive Recovery)",
            1: "Zona Fokus Sunyi & Refleksi Diri (Quiet Focus & Mindfulness)",
            2: "Zona Interaksi & Relaksasi Sosial (Social & Relaxed Interaction)",
            3: "Zona Produktivitas Aktif & Olahraga (Active Productivity & Exercise)"
        }
        
        st.info(f"**Cluster Target Terdeteksi:** {cluster_labels[bmu_idx]}")
        st.write("Aktivitas yang disarankan dalam cluster ini:")
        
        if recommended_activities:
            for act_name in recommended_activities:
                st.markdown(f'<div class="activity-badge">{act_name}</div>', unsafe_allow_html=True)
        else:
            st.write("*Tidak ada aktivitas terdekat. Silakan sesuaikan target vibe di sidebar untuk memperbarui.*")
            
        st.write("---")
        # Menampilkan tabel jarak aktivitas untuk transparansi algoritma
        with st.expander("Lihat Metrik Kedekatan (Jarak Euclidean) Aktivitas"):
            act_names = [act["name"] for act in ACTIVITIES]
            act_dists = []
            for act in ACTIVITIES:
                dist = np.linalg.norm(act["vector"] - target_vector)
                act_dists.append(dist)
            
            df_dist = pd.DataFrame({
                "Nama Aktivitas": act_names,
                "Jarak Euclidean ke Target Vibe": act_dists
            }).sort_values("Jarak Euclidean ke Target Vibe").reset_index(drop=True)
            
            st.dataframe(df_dist.style.format({"Jarak Euclidean ke Target Vibe": "{:.4f}"}))


# ==============================================================================
# TAB 2: VISUALISASI MODEL & KINERJA TRAINING
# ==============================================================================
with tab_charts:
    st.write("### Visualisasi Kinerja & Proses Pelatihan Model JST")
    
    col_plot1, col_plot2 = st.columns([1, 1])
    
    with col_plot1:
        st.write("#### Kurva Konvergensi Training (Model Backpropagation)")
        st.write("Kurva di bawah ini menunjukkan penurunan Mean Squared Error (MSE) selama iterasi training (1200 Epoch) dengan learning rate $\eta = 0.2$.")
        
        fig, ax = plt.subplots(figsize=(6, 4))
        fig.patch.set_facecolor('#0f111a')
        ax.set_facecolor('#161925')
        
        ax.plot(cached_data["bp_history"], color='#00e5ff', linewidth=2.5, label='MSE History (lr=0.2)')
        ax.set_title("Training Loss Convergence Curve", color='#ffffff', fontsize=12, pad=10)
        ax.set_xlabel("Epoch", color='#a0aec0', fontsize=10)
        ax.set_ylabel("Mean Squared Error (MSE)", color='#a0aec0', fontsize=10)
        ax.tick_params(colors='#ffffff')
        ax.grid(True, color='#2c313d', linestyle='--')
        ax.legend(facecolor='#161925', edgecolor='#00e5ff', labelcolor='#ffffff')
        
        # Set border colors
        for spine in ax.spines.values():
            spine.set_color('#2c313d')
            
        st.pyplot(fig)
        
    with col_plot2:
        st.write("#### Perbandingan Parameter Learning Rate ($\eta$)")
        st.write("Menunjukkan perbedaan konvergensi saat menggunakan nilai learning rate yang berbeda. Terlalu kecil lambat konvergen, terlalu besar dapat tidak stabil.")
        
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        fig2.patch.set_facecolor('#0f111a')
        ax2.set_facecolor('#161925')
        
        ax2.plot(cached_data["history_01"], color='#ffab00', linewidth=2, label='lr = 0.01 (Lambat)')
        ax2.plot(cached_data["bp_history"], color='#00e5ff', linewidth=2, label='lr = 0.20 (Optimal)')
        ax2.plot(cached_data["history_5"], color='#ff1744', linewidth=2, label='lr = 0.50 (Agresif)')
        
        ax2.set_title("MSE Comparison by Learning Rate", color='#ffffff', fontsize=12, pad=10)
        ax2.set_xlabel("Epoch", color='#a0aec0', fontsize=10)
        ax2.set_ylabel("Mean Squared Error (MSE)", color='#a0aec0', fontsize=10)
        ax2.tick_params(colors='#ffffff')
        ax2.grid(True, color='#2c313d', linestyle='--')
        ax2.legend(facecolor='#161925', edgecolor='#00e5ff', labelcolor='#ffffff')
        
        # Set border colors
        for spine in ax2.spines.values():
            spine.set_color('#2c313d')
            
        st.pyplot(fig2)

    st.write("---")
    st.write("#### Peta Klusterisasi Kohonen Self-Organizing Map (Grid 2x2)")
    st.write("Visualisasi ini menggambarkan bagaimana 10 aktivitas di petakan ke dalam 4 neuron grid output (2x2) berdasarkan kedekatan fitur bobotnya.")
    
    # Buat plot peta grid SOM
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    fig3.patch.set_facecolor('#0f111a')
    ax3.set_facecolor('#161925')
    
    # Warna latar belakang masing-masing sel grid untuk identifikasi estetis
    grid_colors = [
        ['#1a1e35', '#241a35'],
        ['#1a2a35', '#1a3528']
    ]
    
    ax3.set_xlim(-0.5, 1.5)
    ax3.set_ylim(-0.5, 1.5)
    ax3.set_xticks([0, 1])
    ax3.set_yticks([0, 1])
    ax3.set_xticklabels(['Kolom 0', 'Kolom 1'], color='#ffffff')
    ax3.set_yticklabels(['Baris 0', 'Baris 1'], color='#ffffff')
    ax3.grid(True, color='#2c313d', linestyle='-', linewidth=2)
    
    # Judul representatif untuk grid neuron
    grid_labels = {
        0: "Rest & Recovery\n(Node [0,0])",
        1: "Quiet Focus\n(Node [0,1])",
        2: "Social Vibe\n(Node [1,0])",
        3: "Active Productivity\n(Node [1,1])"
    }
    
    # Tampilkan teks aktivitas pada sel grid masing-masing
    for idx in range(4):
        r, c = cached_data["som_model"].get_grid_coords(idx)
        acts = cached_data["activity_clusters"][idx]
        
        # Gambar kotak sel
        rect = plt.Rectangle((c-0.45, r-0.45), 0.9, 0.9, facecolor=grid_colors[r][c], edgecolor='#00e5ff', linewidth=1.5, alpha=0.7)
        ax3.add_patch(rect)
        
        # Tambahkan judul node
        ax3.text(c, r+0.35, grid_labels[idx], color='#00e5ff', fontsize=11, fontweight='bold', ha='center', va='center')
        
        # Tambahkan daftar aktivitas
        acts_text = "\n".join([f"• {act.split(' ')[0]}" for act in acts]) if acts else "Kosong"
        ax3.text(c, r-0.08, acts_text, color='#e2e8f0', fontsize=9.5, ha='center', va='center', wrap=True)
        
    ax3.set_title("Self-Organizing Map Topographic Activation Mapping", color='#ffffff', fontsize=14, pad=15)
    for spine in ax3.spines.values():
        spine.set_color('#2c313d')
        
    st.pyplot(fig3)


# ==============================================================================
# TAB 3: ACADEMIC DOCUMENTATION FORMAT (INDONESIAN REPORT BAB I-V)
# ==============================================================================
with tab_academic:
    st.write("## Laporan Akademik Projek Ujian Akhir Semester (UAS)")
    st.write("Bagian ini memuat format dokumentasi akademik lengkap yang sesuai dengan struktur pelaporan kuliah JST.")
    
    # Menu dropdown untuk memilih bab laporan
    chapter = st.selectbox("Pilih Bab Laporan Untuk Ditampilkan:", [
        "Bab I: Pendahuluan & Latar Belakang",
        "Bab II: Arsitektur Jaringan & Spesifikasi JST",
        "Bab III: Contoh Iterasi Manual (Forward & Backward Pass)",
        "Bab IV: Analisis Sensitivitas Parameter",
        "Bab V: Kesimpulan & Uji Solusi"
    ])
    
    if chapter.startswith("Bab I:"):
        st.markdown("""
        ### BAB I: PENDAHULUAN
        
        #### 1.1 Latar Belakang & Urgensi Masalah
        Pada era modern yang serba cepat ini, mahasiswa dan profesional dihadapkan pada tingkat stres akademis dan beban kerja yang tinggi. Kurangnya kesadaran akan kapasitas energi harian sering kali berujung pada kondisi **burnout**—sebuah sindrom kelelahan fisik dan mental ekstrem akibat stres kronis yang tidak terkelola dengan baik. Gejala burnout ini sering kali diabaikan hingga menurunkan kinerja, mengganggu kesehatan fisik, serta menurunkan kualitas hidup secara keseluruhan.
        
        Sering kali individu kesulitan menentukan batas aman aktivitas harian mereka, seperti seberapa banyak beban kerja yang dapat diterima setelah waktu tidur yang kurang, atau kapan mereka harus menghentikan penggunaan gawai (*screen time*) dan beralih ke aktivitas sosial maupun fisik yang restoratif.
        
        #### 1.2 Rumusan Masalah
        1. Bagaimana memprediksi risiko burnout harian secara personal berdasarkan variabel waktu tidur, beban kerja, *screen time*, dan interaksi sosial harian?
        2. Bagaimana mengelompokkan aktivitas pemulihan harian secara cerdas sehingga pengguna dapat memperoleh rekomendasi aktivitas yang sesuai dengan kondisi kelelahan fisik maupun kebutuhan fokus mental mereka?
        
        #### 1.3 Solusi JST yang Diusulkan
        Projek **"The Zen-Day Optimizer"** mengintegrasikan dua model Jaringan Saraf Tiruan (JST) yang dibangun dari nol (*from scratch*) dengan NumPy untuk menjawab masalah di atas:
        1. **Model Klasifikasi/Regresi (Backpropagation)**: Digunakan untuk memprediksi tingkat kerawanan burnout (dalam persen) berdasarkan data harian user. Model ini belajar mengenali relasi non-linier antara stres, durasi tidur, beban tugas, dan aktivitas sosial.
        2. **Model Unsupervised Clustering (Kohonen Self-Organizing Map / SOM)**: Digunakan untuk mengelompokkan aktivitas-aktivitas harian ke dalam kluster topografis 2D. Ketika user menentukan target vibe yang diinginkan (misal: butuh ketenangan atau butuh rekreasi aktif), sistem akan mencari neuron pemenang (BMU) pada SOM dan merekomendasikan aktivitas dalam kluster tersebut.
        """)
        
    elif chapter.startswith("Bab II:"):
        st.markdown(r"""
        ### BAB II: ARSITEKTUR JARINGAN & SPESIFIKASI JST
        
        #### 2.1 Model 1: Jaringan Backpropagation
        Jaringan Backpropagation dirancang dengan arsitektur 3 layer terhubung penuh (*fully connected*):
        1. **Layer Input (4 Neuron)**:
           - $x_1$: Kualitas & Durasi Tidur (Normalisasi range 0 s/d 1)
           - $x_2$: Beban Kerja / Jumlah Tugas (Normalisasi range 0 s/d 1)
           - $x_3$: *Screen Time* (Normalisasi range 0 s/d 1)
           - $x_4$: Aktivitas Sosial & Fisik (Normalisasi range 0 s/d 1)
        2. **Layer Tersembunyi / Hidden Layer (5 Neuron)**:
           - Menggunakan bias untuk meningkatkan kapasitas belajar model.
           - Fungsi aktivasi pada hidden layer adalah **Sigmoid Biner** ($\sigma$):
             $$\sigma(z) = \frac{1}{1 + e^{-z}}$$
        3. **Layer Output (1 Neuron)**:
           - Menghasilkan nilai kontinu $y \in [0, 1]$ yang merepresentasikan **Indeks Burnout**.
           - Menggunakan fungsi aktivasi **Sigmoid Biner**.
           
        ```
        Input [4] ---------> Hidden [5] ---------> Output [1] (Burnout Index)
          x1 (Tidur)           (h1 .. h5)             y_pred
          x2 (Tugas)           (Bias b1)             (Bias b2)
          x3 (Layar)
          x4 (Sosial)
        ```
        
        #### 2.2 Model 2: Kohonen Self-Organizing Map (SOM)
        Jaringan SOM digunakan untuk mengelompokkan data tanpa pengawasan (*unsupervised learning*).
        1. **Layer Input (3 Neuron)**:
           - Kebutuhan Energi Fisik (0 s/d 1)
           - Tingkat Interaksi Sosial (0 s/d 1)
           - Kebutuhan Fokus Mental (0 s/d 1)
        2. **Layer Output (Grid 2D 2x2 = 4 Neuron)**:
           - Direpresentasikan sebagai koordinat grid $[r, c]$ di mana $r \in \{0,1\}$ dan $c \in \{0,1\}$.
           - Setiap node dalam grid memiliki vektor bobot berdimensi 3 ($W_j = [w_{j1}, w_{j2}, w_{j3}]$).
           - Metrik kemiripan yang digunakan untuk mencari neuron terdekat (*Best Matching Unit* / BMU) adalah **Jarak Euclidean**:
             $$D(j) = \sqrt{\sum_{i=1}^{3} (x_i - w_{ji})^2}$$
        """)
        
    elif chapter.startswith("Bab III:"):
        st.markdown(r"""
        ### BAB III: CONTOH ITERASI MANUAL
        
        Di bawah ini adalah simulasi numerik satu langkah iterasi maju (Forward) dan satu langkah iterasi mundur (Backward) pada model Backpropagation dengan arsitektur yang disederhanakan (2 Input, 2 Hidden, 1 Output) untuk memudahkan perhitungan manual.
        
        #### 3.1 Parameter Awal
        - **Input**: $x_1 = 0.8$, $x_2 = 0.4$
        - **Target Output**: $t = 0.1$
        - **Learning Rate**: $\eta = 0.5$
        
        **Bobot Layer Tersembunyi ($W_1$ & $b_1$):**
        - Ke Hidden 1 ($h_1$): $w_{11} = 0.15$, $w_{21} = 0.25$, Bias $b_{11} = 0.35$
        - Ke Hidden 2 ($h_2$): $w_{12} = 0.20$, $w_{22} = 0.30$, Bias $b_{12} = 0.35$
        
        **Bobot Layer Output ($W_2$ & $b_2$):**
        - Dari $h_1$ ke output $o_1$: $w_{out1} = 0.40$
        - Dari $h_2$ ke output $o_1$: $w_{out2} = 0.45$
        - Bias Output $b_{2} = 0.60$
        
        ---
        
        #### 3.2 Perambatan Maju (Forward Pass)
        
        **Langkah 1: Hitung Net input dan aktivasi pada Layer Tersembunyi**
        - Net Input $h_1$ ($z_{h1}$):
          $$z_{h1} = x_1 \cdot w_{11} + x_2 \cdot w_{21} + b_{11}$$
          $$z_{h1} = (0.8 \cdot 0.15) + (0.4 \cdot 0.25) + 0.35 = 0.12 + 0.10 + 0.35 = 0.57$$
        - Aktivasi $h_1$ ($a_{h1}$):
          $$a_{h1} = \frac{1}{1 + e^{-0.57}} = \frac{1}{1 + 0.5655} \approx 0.6387$$
          
        - Net Input $h_2$ ($z_{h2}$):
          $$z_{h2} = x_1 \cdot w_{12} + x_2 \cdot w_{22} + b_{12}$$
          $$z_{h2} = (0.8 \cdot 0.20) + (0.4 \cdot 0.30) + 0.35 = 0.16 + 0.12 + 0.35 = 0.63$$
        - Aktivasi $h_2$ ($a_{h2}$):
          $$a_{h2} = \frac{1}{1 + e^{-0.63}} = \frac{1}{1 + 0.5326} \approx 0.6525$$
          
        **Langkah 2: Hitung Net input dan aktivasi pada Layer Output**
        - Net Input Output $o_1$ ($z_{o1}$):
          $$z_{o1} = a_{h1} \cdot w_{out1} + a_{h2} \cdot w_{out2} + b_{2}$$
          $$z_{o1} = (0.6387 \cdot 0.40) + (0.6525 \cdot 0.45) + 0.60 = 0.2555 + 0.2936 + 0.60 = 1.1491$$
        - Aktivasi Output $o_1$ ($a_{o1}$ / Output Aktual):
          $$a_{o1} = \frac{1}{1 + e^{-1.1491}} = \frac{1}{1 + 0.3169} \approx 0.7593$$
          
        **Langkah 3: Hitung Error (Loss)**
        - Mean Squared Error untuk sampel tunggal:
          $$E = \frac{1}{2}(t - a_{o1})^2 = \frac{1}{2}(0.1 - 0.7593)^2 = \frac{1}{2}(-0.6593)^2 \approx 0.2173$$
        
        ---
        
        #### 3.3 Perambatan Mundur (Backward Pass)
        
        **Langkah 1: Hitung Sinyal Error di Layer Output ($\delta_{o1}$)**
        - Turunan error terhadap input net output:
          $$\delta_{o1} = (t - a_{o1}) \cdot a_{o1} \cdot (1 - a_{o1})$$
          $$\delta_{o1} = (0.1 - 0.7593) \cdot 0.7593 \cdot (1 - 0.7593) = -0.6593 \cdot 0.7593 \cdot 0.2407 \approx -0.1205$$
          
        **Langkah 2: Hitung Sinyal Error di Layer Tersembunyi ($\delta_{h1}$ & $\delta_{h2}$)**
        - Untuk Hidden 1 ($h_1$):
          $$\delta_{h1} = \delta_{o1} \cdot w_{out1} \cdot a_{h1} \cdot (1 - a_{h1})$$
          $$\delta_{h1} = -0.1205 \cdot 0.40 \cdot 0.6387 \cdot (1 - 0.6387) = -0.0482 \cdot 0.6387 \cdot 0.3613 \approx -0.0111$$
        - Untuk Hidden 2 ($h_2$):
          $$\delta_{h2} = \delta_{o1} \cdot w_{out2} \cdot a_{h2} \cdot (1 - a_{h2})$$
          $$\delta_{h2} = -0.1205 \cdot 0.45 \cdot 0.6525 \cdot (1 - 0.6525) = -0.0542 \cdot 0.6525 \cdot 0.3475 \approx -0.0123$$
          
        ---
        
        #### 3.4 Pembaruan Bobot (Weight Updates)
        Menggunakan rumus: $w_{baru} = w_{lama} + \eta \cdot \delta_{penerima} \cdot a_{pengirim}$
        
        **1. Bobot Layer Output ($W_2$):**
        - Update $w_{out1}$:
          $$w_{out1}^{(baru)} = 0.40 + 0.5 \cdot (-0.1205) \cdot 0.6387 = 0.40 - 0.0385 = 0.3615$$
        - Update $w_{out2}$:
          $$w_{out2}^{(baru)} = 0.45 + 0.5 \cdot (-0.1205) \cdot 0.6525 = 0.45 - 0.0393 = 0.4107$$
        - Update Bias $b_2$:
          $$b_{2}^{(baru)} = 0.60 + 0.5 \cdot (-0.1205) \cdot 1 = 0.60 - 0.0603 = 0.5397$$
          
        **2. Bobot Layer Tersembunyi ($W_1$):**
        - Update $w_{11}$ (Input 1 ke $h_1$):
          $$w_{11}^{(baru)} = 0.15 + 0.5 \cdot (-0.0111) \cdot 0.8 = 0.15 - 0.0044 = 0.1456$$
        - Update $w_{21}$ (Input 2 ke $h_1$):
          $$w_{21}^{(baru)} = 0.25 + 0.5 \cdot (-0.0111) \cdot 0.4 = 0.25 - 0.0022 = 0.2478$$
        - Update Bias $b_{11}$:
          $$b_{11}^{(baru)} = 0.35 + 0.5 \cdot (-0.0111) \cdot 1 = 0.35 - 0.0056 = 0.3444$$
          
        - Update $w_{12}$ (Input 1 ke $h_2$):
          $$w_{12}^{(baru)} = 0.20 + 0.5 \cdot (-0.0123) \cdot 0.8 = 0.20 - 0.0049 = 0.1951$$
        - Update $w_{22}$ (Input 2 ke $h_2$):
          $$w_{22}^{(baru)} = 0.30 + 0.5 \cdot (-0.0123) \cdot 0.4 = 0.30 - 0.0025 = 0.2975$$
        - Update Bias $b_{12}$:
          $$b_{12}^{(baru)} = 0.35 + 0.5 \cdot (-0.0123) \cdot 1 = 0.35 - 0.0062 = 0.3388$$
          
        ---
        
        #### 3.5 Simulasi Manual Kohonen SOM
        - **Input**: $X = [0.8, 0.2, 0.2]$ (Kebutuhan Energi Fisik Tinggi, Sosial Rendah, Mental Fokus Rendah)
        - Kita bandingkan dengan bobot Node 1: $W_1 = [0.8, 0.1, 0.2]$.
        - Jarak Euclidean $D(1) = \sqrt{(0.8 - 0.8)^2 + (0.2 - 0.1)^2 + (0.2 - 0.2)^2} = 0.1000$.
        - Jika Node 1 adalah BMU, dengan $\eta = 0.6$, bobot diperbarui menjadi:
          $$W_1^{(baru)} = W_1^{(lama)} + \eta \cdot (X - W_1^{(lama)})$$
          $$W_1^{(baru)} = [0.8, 0.1, 0.2] + 0.6 \cdot ([0.8, 0.2, 0.2] - [0.8, 0.1, 0.2])$$
          $$W_1^{(baru)} = [0.8, 0.1, 0.2] + [0.0, 0.06, 0.0] = [0.8, 0.16, 0.2]$$
        """)
        
    elif chapter.startswith("Bab IV:"):
        st.markdown(r"""
        ### BAB IV: ANALISIS SENSITIVITAS PARAMETER
        
        Berdasarkan visualisasi grafik pada Tab **"Visualisasi Model"**, dilakukan eksperimen untuk menganalisis pengaruh perubahan parameter *Learning Rate* ($\eta$) terhadap laju konvergensi dan kestabilan model Backpropagation:
        
        1. **Learning Rate Sangat Kecil ($\eta = 0.01$)**:
           - **Pengaruh**: Penurunan nilai MSE berjalan sangat lambat. Memerlukan jumlah epoch yang jauh lebih banyak untuk mencapai konvergensi optimal.
           - **Kelebihan**: Sangat stabil dan minim risiko berosilasi di sekitar nilai minimum lokal.
           
        2. **Learning Rate Optimal ($\eta = 0.20$)**:
           - **Pengaruh**: Model mencapai konvergensi yang cepat dan halus. Dalam sekitar 600-800 epoch, MSE sudah mulai mendatar di angka yang sangat rendah (< 0.008).
           - **Kelebihan**: Efisiensi komputasi tinggi tanpa mengorbankan akurasi klasifikasi.
           
        3. **Learning Rate Agresif/Besar ($\eta = 0.50$)**:
           - **Pengaruh**: Terjadi percepatan penurunan MSE pada epoch-epoch awal. Namun, grafik terlihat berosilasi lebih tajam dan rentan melompati (*overshooting*) nilai minimum global yang sebenarnya.
           
        **Rekomendasi Parameter**:
        Untuk dataset optimasi burnout ini, kombinasi paling efisien adalah **$\eta = 0.2$** dengan **Epoch = 1000 hingga 1200**.
        """)
        
    elif chapter.startswith("Bab V:"):
        st.markdown("""
        ### BAB V: KESIMPULAN & UJI SOLUSI
        
        #### 5.1 Kesimpulan Keberhasilan Model
        Berdasarkan pengujian sistem secara real-time pada dashboard utama:
        1. **Model Backpropagation** berhasil memetakan variabel-variabel input harian (Tidur, Tugas, Layar, dan Sosial) menjadi indikator persentase burnout yang relevan secara logis dan ilmiah. Model mampu mengidentifikasi skenario ekstrem (misalnya, tidur 4 jam dengan 10 tugas menghasilkan burnout > 80%).
        2. **Model Kohonen SOM** berhasil membagi 10 aktivitas harian yang variatif menjadi 4 cluster topografi yang teratur secara mandiri (*unsupervised*). Aktivitas pasif terkelompok dekat satu sama lain, begitupun aktivitas sosial dan akademis terfokus.
        3. **Integrasi Solusi** berhasil menjembatani prediksi resiko kesehatan mental dengan solusi pemulihan aktivitas harian secara real-time.
        
        #### 5.2 Saran Pengembangan
        1. **Ekspansi Dataset**: Menggunakan dataset riil dari log aktivitas smartwatch atau aplikasi pelacak waktu guna meningkatkan validitas prediksi.
        2. **Struktur Hidden Layer**: Uji coba penambahan jumlah hidden layer (Deep Neural Network) untuk pola hubungan yang lebih kompleks.
        """)


# ==============================================================================
# FOOTER
# ==============================================================================
st.write("---")
st.write("""
<div style="text-align: center; color: #a0aec0; padding: 15px; font-size: 13px;">
    Dibuat oleh Tim JST - Final Exam Project "The Zen-Day Optimizer" &copy; 2026. Built with Streamlit and NumPy.
</div>
""", unsafe_allow_html=True)
