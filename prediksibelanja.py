import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ===== KONFIGURASI TEMA ELEGAN =====
st.set_page_config(
    page_title="Prediksi Biaya Belanja Pasien Rumah Sakit", 
    layout="wide",
    page_icon="🏥",
    initial_sidebar_state="expanded"
)

# ===== STYLING CSS ELEGAN =====
st.markdown("""
<style>
    /* Main background */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
    }
    
    /* Header container dengan gradient */
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        text-align: center;
    }
    
    /* Card styling modern */
    .elegant-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.3);
        margin-bottom: 1.5rem;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .elegant-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
    }
    
    /* Metric card styling */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    }
    
    /* Button styling elegan */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 50px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
    }
    
    /* Input field styling */
    .stTextInput>div>div>input, 
    .stNumberInput>div>div>input,
    .stSelectbox>div>div>select {
        border-radius: 15px;
        border: 2px solid #e9ecef;
        padding: 0.75rem 1rem;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput>div>div>input:focus, 
    .stNumberInput>div>div>input:focus,
    .stSelectbox>div>div>select:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Sidebar header styling */
    .sidebar-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem 1rem;
        text-align: center;
        border-radius: 0 0 20px 20px;
        margin-bottom: 2rem;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        background: transparent;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 15px 15px 0 0;
        padding: 1rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(255, 255, 255, 0.95);
    }
    
    .stTabs [aria-selected="true"] {
        background: white !important;
        color: #667eea !important;
    }
    
    /* Success message styling */
    .stSuccess {
        border-radius: 15px;
        padding: 1.5rem;
        background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
        border-left: 5px solid #28a745;
    }
    
    /* Warning message styling */
    .stWarning {
        border-radius: 15px;
        padding: 1.5rem;
        background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%);
        border-left: 5px solid #ffc107;
    }
    
    /* Info message styling */
    .stInfo {
        border-radius: 15px;
        padding: 1.5rem;
        background: linear-gradient(135deg, #d1ecf1 0%, #b8e6f1 100%);
        border-left: 5px solid #17a2b8;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        font-weight: 600;
    }
    
    /* Footer styling */
    .footer {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin-top: 3rem;
    }
    
    /* Custom metric styling */
    [data-testid="metric-container"] {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# ===== HEADER ELEGAN =====
st.markdown("""
<div class="header-container">
    <h1 style="margin:0; font-size: 3rem; font-weight: 700;">Prediksi Biaya Belanja Pasien Rumah Sakit</h1>
    <p style="margin:0; font-size: 1.3rem; opacity: 0.9; margin-top: 1rem;">
        Berbasis Analisis Data Historis Januari–Juni 2025
    </p>
    <div style="margin-top: 2rem;">
        <div style="display: inline-block; background: rgba(255,255,255,0.2); padding: 0.5rem 1.5rem; border-radius: 25px; margin: 0 0.5rem;">
            Analytics Dashboard
        </div>
        <div style="display: inline-block; background: rgba(255,255,255,0.2); padding: 0.5rem 1.5rem; border-radius: 25px; margin: 0 0.5rem;">
            Cost Prediction
        </div>
        <div style="display: inline-block; background: rgba(255,255,255,0.2); padding: 0.5rem 1.5rem; border-radius: 25px; margin: 0 0.5rem;">
            Trend Analysis
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ===== SIDEBAR ELEGAN =====
with st.sidebar:
    st.markdown("""
    <div class="sidebar-header">
        <h2>Tugas Machine Learning</h2>
        <p>Kelola prediksi dan analisis</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="elegant-card">', unsafe_allow_html=True)
    st.header("Masukkan Tanggal Kunjungan")
    bulan = st.selectbox('**Bulan**', options=list(range(1, 13)), index=0)
    hari_dlm_bulan = st.selectbox('**Hari dalam Bulan**', options=list(range(1, 32)), index=0)
    
    # Validasi tanggal
    tanggal_valid = True
    try:
        pd.Timestamp(year=2025, month=bulan, day=hari_dlm_bulan)
    except ValueError:
        tanggal_valid = False
        st.warning("Tanggal tidak valid untuk bulan yang dipilih")
    
    if st.button("**Prediksi Belanja**", type="primary", use_container_width=True):
        st.session_state.predict_clicked = True
    else:
        if 'predict_clicked' not in st.session_state:
            st.session_state.predict_clicked = False
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Quick Stats di Sidebar
    st.markdown('<div class="elegant-card">', unsafe_allow_html=True)
    st.markdown("### Quick Stats")
    st.markdown("""
    <div style="text-align: center;">
        <p><strong>Data Historis</strong><br>Jan - Jun 2025</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ===== KONTEN UTAMA DENGAN FUNGSI ASLI =====

# === 1. Baca dataset ===
@st.cache_data
def load_data():
    file_path = r'lap_belanja_jan-juni2025.csv'
    
    if not os.path.exists(file_path):
        st.error(f"File tidak ditemukan: {file_path}")
        return None
        
    try:
        df = pd.read_csv(file_path, sep=';', header=None, low_memory=False, encoding='utf-8')
        if df.shape[1] == 12:
            df.columns = [
                'id_transaksi', 'id_pasien', 'no_urut', 'nama_pasien', 'waktu',
                'dokter', 'jenis_layanan', 'poli', 'sumber_pembayaran', 'biaya',
                'diskon', 'flag'
            ]
        else:
            st.warning(f"Jumlah kolom tidak sesuai. Ditemukan {df.shape[1]} kolom, harap periksa file CSV.")
            return None
        return df
    except Exception as e:
        st.error(f"Error membaca file: {str(e)}")
        return None

df = load_data()
if df is None:
    st.stop()

# === 2. Preprocessing: waktu + biaya ===
def preprocess(df):
    # Tampilkan sample data mentah untuk debugging
    st.sidebar.write("**Sample Data Biaya Mentah:**")
    st.sidebar.write(df['biaya'].head(10).tolist())
    
    # Konversi waktu
    df['waktu'] = pd.to_datetime(df['waktu'], format='%d/%m/%Y', errors='coerce')
    
    # Fungsi cleaning biaya yang DIPERBAIKI
    def clean_biaya(value):
        if pd.isna(value) or value == '':
            return np.nan
        
        try:
            str_value = str(value).strip()
            
            # Skip jika value adalah header/string non-numeric
            if str_value.lower() == 'biaya' or not any(char.isdigit() for char in str_value):
                return np.nan
            
            # Case 1: Format "503,000.00" - koma sebagai pemisah ribuan, titik desimal
            if ',' in str_value and '.' in str_value:
                # Format: "58,922,400.00" -> hapus koma, biarkan titik
                str_value = str_value.replace(',', '')
            
            # Case 2: Format "1.539.800,00" - titik sebagai pemisah ribuan, koma desimal
            elif '.' in str_value and ',' in str_value:
                # Format: "1.539.800,00" -> hapus titik, ganti koma dengan titik
                str_value = str_value.replace('.', '').replace(',', '.')
            
            # Case 3: Hanya koma (mungkin desimal)
            elif ',' in str_value:
                if len(str_value) > 3 and str_value[-3] == ',':
                    # Koma sebagai pemisah desimal: "1500,00" -> "1500.00"
                    str_value = str_value.replace(',', '.')
                else:
                    # Koma sebagai pemisah ribuan: "1,500" -> "1500"
                    str_value = str_value.replace(',', '')
            
            # Case 4: Hanya titik (mungkin ribuan)
            elif '.' in str_value:
                if len(str_value) > 3 and str_value[-3] == '.':
                    # Titik sebagai pemisah desimal: "1500.00" -> biarkan
                    pass
                else:
                    # Titik sebagai pemisah ribuan: "1.500" -> "1500"
                    str_value = str_value.replace('.', '')
            
            # Konversi ke float
            result = float(str_value)
            
            # Validasi: perbaiki range untuk mengakomodasi biaya rumah sakit yang legit
            if result < -1000000 or result > 100000000:  # Range: -1jt sampai 100jt
                return result  # Kembalikan nilai asli, jangan di-drop
            
            return result
            
        except (ValueError, TypeError) as e:
            return np.nan
    
    # Apply cleaning
    df['biaya_cleaned'] = df['biaya'].apply(clean_biaya)
    
    # Tampilkan hasil cleaning
    st.sidebar.write("**Sample Data Biaya Setelah Cleaning:**")
    st.sidebar.write(df['biaya_cleaned'].head(10).tolist())
    
    # Hapus baris dengan nilai NaN di kolom penting
    initial_count = len(df)
    df = df.dropna(subset=['waktu', 'biaya_cleaned']).copy()
    final_count = len(df)
    
    st.sidebar.write(f"**Data Cleaning:**")
    st.sidebar.write(f"- Awal: {initial_count} transaksi")
    st.sidebar.write(f"- Valid: {final_count} transaksi")
    st.sidebar.write(f"- Dihapus: {initial_count - final_count} transaksi")
    
    # Ganti kolom biaya dengan yang sudah dibersihkan
    df['biaya'] = df['biaya_cleaned']
    df = df.drop('biaya_cleaned', axis=1)
    
    # Validasi final
    st.sidebar.write("**Validasi Final:**")
    st.sidebar.write(f"- Total Biaya: Rp {df['biaya'].sum():,.0f}")
    st.sidebar.write(f"- Rata-rata: Rp {df['biaya'].mean():,.0f}")
    st.sidebar.write(f"- Min/Max: Rp {df['biaya'].min():,.0f} / Rp {df['biaya'].max():,.0f}")
    
    # Ekstrak fitur
    df['bulan'] = df['waktu'].dt.month
    df['hari_dlm_bulan'] = df['waktu'].dt.day
    df['hari_dlm_minggu'] = df['waktu'].dt.dayofweek
    df['minggu_dlm_bulan'] = df['waktu'].dt.isocalendar().week - df['waktu'].dt.to_period('M').apply(lambda r: r.start_time.isocalendar().week) + 1
    
    return df

try:
    df = preprocess(df)
except Exception as e:
    st.error(f"Error dalam preprocessing data: {str(e)}")
    st.stop()

# === 3. Hitung rata-rata biaya per (bulan, hari_dlm_bulan) ===
@st.cache_data
def create_lookup(df):
    lookup = df.groupby(['bulan', 'hari_dlm_bulan'])['biaya'].agg(['mean', 'count']).reset_index()
    lookup.rename(columns={'mean': 'rata_rata_biaya'}, inplace=True)
    lookup = lookup[lookup['count'] > 0]
    return lookup

lookup_df = create_lookup(df)
global_avg = df['biaya'].mean()

# === 4. Format Rupiah seperti yang diinginkan ===
def format_rupiah(angka):
    """Format angka menjadi string Rupiah dengan format: '503,000.00'"""
    try:
        if pd.isna(angka) or angka == 0:
            return "0.00"
        
        # Format dengan 2 desimal
        formatted = f"{angka:,.2f}"
        return formatted
    except (ValueError, TypeError):
        return "0.00"

def format_rupiah_display(angka):
    """Format untuk display dengan tambahan Rp"""
    formatted = format_rupiah(angka)
    return f"Rp {formatted}"

def format_rupiah_compact(angka):
    """Format untuk nilai besar dengan penyederhanaan"""
    try:
        if pd.isna(angka) or angka == 0:
            return "Rp 0"
        
        if angka >= 1_000_000_000:  # Miliar
            return f"Rp {angka/1_000_000_000:,.1f}M"
        elif angka >= 1_000_000:    # Juta
            return f"Rp {angka/1_000_000:,.1f}Jt"
        elif angka >= 1_000:        # Ribu
            return f"Rp {angka/1_000:,.1f}K"
        else:
            return f"Rp {angka:,.0f}"
    except (ValueError, TypeError):
        return "Rp 0"

# === 6. Prediksi saat tombol diklik ===
if st.session_state.predict_clicked:
    if not tanggal_valid:
        st.error("Tanggal tidak valid (misal: 31 April). Silakan perbaiki input.")
    else:
        # Cari data historis
        match = lookup_df[
            (lookup_df['bulan'] == bulan) &
            (lookup_df['hari_dlm_bulan'] == hari_dlm_bulan)
        ]
        
        if not match.empty:
            prediksi = match.iloc[0]['rata_rata_biaya']
            jumlah_data = int(match.iloc[0]['count'])
            
            st.markdown('<div class="elegant-card">', unsafe_allow_html=True)
            st.success(f"**Perkiraan Biaya Belanja: {format_rupiah_display(prediksi)}**")
            st.info(f"Berdasarkan **{jumlah_data} transaksi** pada tanggal **{hari_dlm_bulan}/{bulan}** dalam data historis.")
            
            # Tampilkan visualisasi
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Prediksi Biaya", format_rupiah_display(prediksi))
            with col2:
                st.metric("Jumlah Data", f"{jumlah_data:,}")
            with col3:
                st.metric("Bulan", bulan)
            st.markdown('</div>', unsafe_allow_html=True)
                
        else:
            st.markdown('<div class="elegant-card">', unsafe_allow_html=True)
            st.warning(f"Tidak ditemukan data historis pada tanggal **{hari_dlm_bulan}/{bulan}**.")
            st.success(f"**Prediksi (rata-rata seluruh data): {format_rupiah_display(global_avg)}**")
            
            # Tampilkan info data terdekat
            st.info("**Rekomendasi berdasarkan data terdekat:**")
            same_month = lookup_df[lookup_df['bulan'] == bulan]
            if not same_month.empty:
                closest_day = same_month.iloc[(same_month['hari_dlm_bulan'] - hari_dlm_bulan).abs().argsort()[:1]]
                prediksi_dekat = closest_day.iloc[0]['rata_rata_biaya']
                hari_dekat = closest_day.iloc[0]['hari_dlm_bulan']
                jumlah_dekat = int(closest_day.iloc[0]['count'])
                st.write(f"- Tanggal terdekat: **{hari_dekat}/{bulan}** → {format_rupiah_display(prediksi_dekat)} ({jumlah_dekat} transaksi)")
            st.markdown('</div>', unsafe_allow_html=True)

# === 7. Tampilkan Data dan Grafik ===
st.markdown('<div class="elegant-card">', unsafe_allow_html=True)
st.header("Statistik Data Lengkap")

# Row 1: Basic Stats
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(
        "Total Transaksi", 
        f"{len(df):,}",
        help="Jumlah total transaksi dalam dataset"
    )
with col2:
    st.metric(
        "Rata-rata Biaya", 
        format_rupiah_display(df['biaya'].mean()),
        help="Rata-rata biaya per transaksi"
    )
with col3:
    st.metric(
        "Total Biaya", 
        format_rupiah_compact(df['biaya'].sum()),
        help="Total akumulasi semua biaya"
    )

# Row 2: Range Stats
col4, col5, col6 = st.columns(3)
with col4:
    # Handle nilai negatif
    biaya_min = df['biaya'].min()
    if biaya_min < 0:
        st.metric(
            "Biaya Minimum", 
            format_rupiah_display(biaya_min),
            delta="NEGATIF",
            delta_color="inverse",
            help="Biaya transaksi terendah (mungkin refund/diskon)"
        )
    else:
        st.metric(
            "Biaya Minimum", 
            format_rupiah_display(biaya_min),
            help="Biaya transaksi terendah"
        )
with col5:
    st.metric(
        "Biaya Maksimum", 
        format_rupiah_compact(df['biaya'].max()),
        help="Biaya transaksi tertinggi"
    )
with col6:
    st.metric(
        "Biaya Median", 
        format_rupiah_display(df['biaya'].median()),
        help="Nilai tengah dari semua biaya"
    )

# Row 3: Additional Stats
col7, col8, col9 = st.columns(3)
with col7:
    st.metric(
        "Standar Deviasi", 
        format_rupiah_compact(df['biaya'].std()),
        help="Tingkat variasi data biaya"
    )
with col8:
    # Hitung persentase nilai negatif
    negatif_count = len(df[df['biaya'] < 0])
    negatif_persen = (negatif_count / len(df)) * 100
    st.metric(
        "Transaksi Negatif", 
        f"{negatif_count:,}",
        delta=f"{negatif_persen:.1f}%",
        help="Jumlah transaksi dengan biaya negatif (refund)"
    )
with col9:
    st.metric(
        "Rentang Biaya", 
        format_rupiah_compact(df['biaya'].max() - df['biaya'].min()),
        help="Selisih biaya tertinggi dan terendah"
    )
st.markdown('</div>', unsafe_allow_html=True)

# Tampilkan nilai lengkap dalam expander
st.markdown('<div class="elegant-card">', unsafe_allow_html=True)
with st.expander("Detail Nilai Lengkap"):
    st.write("**Nilai Lengkap Tanpa Pemendekan:**")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("**Statistik Dasar:**")
        st.write(f"- Total Transaksi: **{len(df):,}**")
        st.write(f"- Rata-rata Biaya: **{format_rupiah_display(df['biaya'].mean())}**")
        st.write(f"- Total Biaya: **{format_rupiah_display(df['biaya'].sum())}**")
        st.write(f"- Biaya Minimum: **{format_rupiah_display(df['biaya'].min())}**")
        st.write(f"- Biaya Maksimum: **{format_rupiah_display(df['biaya'].max())}**")
        st.write(f"- Biaya Median: **{format_rupiah_display(df['biaya'].median())}**")
    
    with col_b:
        st.write("**Statistik Tambahan:**")
        st.write(f"- Standar Deviasi: **{format_rupiah_display(df['biaya'].std())}**")
        st.write(f"- Q1 (25%): **{format_rupiah_display(df['biaya'].quantile(0.25))}**")
        st.write(f"- Q3 (75%): **{format_rupiah_display(df['biaya'].quantile(0.75))}**")
        st.write(f"- IQR: **{format_rupiah_display(df['biaya'].quantile(0.75) - df['biaya'].quantile(0.25))}**")
        st.write(f"- Transaksi > 0: **{len(df[df['biaya'] > 0]):,}**")
        st.write(f"- Transaksi = 0: **{len(df[df['biaya'] == 0]):,}**")
        st.write(f"- Transaksi < 0: **{len(df[df['biaya'] < 0]):,}**")
st.markdown('</div>', unsafe_allow_html=True)

# === 8. Grafik Pasien dengan Biaya Terbanyak ===
st.markdown('<div class="elegant-card">', unsafe_allow_html=True)
st.header("👥 Top 20 Pasien dengan Biaya Terbanyak")

if 'nama_pasien' in df.columns and 'biaya' in df.columns:
    # Hitung total biaya per pasien
    pasien_biaya = df.groupby('nama_pasien')['biaya'].sum()
    
    # Ambil top 20 pasien dengan biaya tertinggi
    top_pasien = pasien_biaya.nlargest(20)
    
    if len(top_pasien) > 0:
        # Buat grafik batang horizontal
        fig_pasien, ax_pasien = plt.subplots(figsize=(12, 10))
        
        # Urutkan dari terbesar ke terkecil untuk grafik horizontal
        top_pasien_sorted = top_pasien.sort_values(ascending=True)
        
        bars = ax_pasien.barh(range(len(top_pasien_sorted)), top_pasien_sorted.values, 
                             color='#667eea', edgecolor='#764ba2', alpha=0.8)
        
        ax_pasien.set_yticks(range(len(top_pasien_sorted)))
        ax_pasien.set_yticklabels(top_pasien_sorted.index)
        ax_pasien.set_xlabel('Total Biaya (Rupiah)')
        ax_pasien.set_title('Top 20 Pasien dengan Total Biaya Terbanyak')
        
        # Format sumbu x dengan label Rupiah
        ax_pasien.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'Rp {x:,.0f}'))
        
        # Tambah nilai di bar
        for i, bar in enumerate(bars):
            width = bar.get_width()
            ax_pasien.text(width + 1000000, bar.get_y() + bar.get_height()/2., 
                          f'Rp {width:,.0f}', ha='left', va='center', fontsize=9)
        
        plt.tight_layout()
        st.pyplot(fig_pasien)
        
        # Tampilkan tabel detail
        st.subheader("Tabel Detail Top 20 Pasien")
        
        pasien_table = pd.DataFrame({
            'Nama Pasien': top_pasien.index,
            'Total Biaya': top_pasien.values
        })
        
        # Format biaya untuk tabel
        pasien_table['Total Biaya Formatted'] = pasien_table['Total Biaya'].apply(format_rupiah_display)
        
        st.dataframe(
            pasien_table[['Nama Pasien', 'Total Biaya Formatted']].rename(
                columns={'Total Biaya Formatted': 'Total Biaya'}
            ),
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("Tidak ada data pasien yang tersedia untuk ditampilkan.")
st.markdown('</div>', unsafe_allow_html=True)

# === 9. Tampilan Sort by Poli Terbanyak ===
st.markdown('<div class="elegant-card">', unsafe_allow_html=True)
st.header("Analisis Berdasarkan Poli")

if 'poli' in df.columns:
    # Hitung statistik per poli
    poli_stats = df.groupby('poli').agg({
        'biaya': ['count', 'mean', 'sum'],
        'id_transaksi': 'nunique'
    }).round(2)
    
    poli_stats.columns = ['Jumlah_Transaksi', 'Rata_rata_Biaya', 'Total_Biaya', 'Jumlah_Pasien']
    poli_stats = poli_stats.sort_values('Jumlah_Transaksi', ascending=False)
    
    # Tampilkan top 10 poli terbanyak
    st.subheader("Top 10 Poli dengan Transaksi Terbanyak")
    
    top_10_poli = poli_stats.head(10)
    
    # Buat grafik batang untuk top 10 poli
    fig_poli, ax_poli = plt.subplots(figsize=(12, 6))
    bars = ax_poli.barh(range(len(top_10_poli)), top_10_poli['Jumlah_Transaksi'], 
                       color='#667eea', edgecolor='#764ba2', alpha=0.8)
    ax_poli.set_yticks(range(len(top_10_poli)))
    ax_poli.set_yticklabels(top_10_poli.index)
    ax_poli.set_xlabel('Jumlah Transaksi')
    ax_poli.set_title('Top 10 Poli dengan Transaksi Terbanyak')
    
    # Tambah nilai di bar
    for i, bar in enumerate(bars):
        width = bar.get_width()
        ax_poli.text(width + 5, bar.get_y() + bar.get_height()/2., 
                    f'{int(width):,}', ha='left', va='center')
    
    st.pyplot(fig_poli)
    
    # Tampilkan tabel detail poli
    st.subheader("Tabel Detail Semua Poli")
    
    # Format angka dalam tabel
    display_poli = top_10_poli.copy()
    display_poli['Rata_rata_Biaya'] = display_poli['Rata_rata_Biaya'].apply(format_rupiah_display)
    display_poli['Total_Biaya'] = display_poli['Total_Biaya'].apply(format_rupiah_display)
    
    st.dataframe(
        display_poli.rename(columns={
            'Jumlah_Transaksi': 'Jumlah Transaksi',
            'Rata_rata_Biaya': 'Rata-rata Biaya', 
            'Total_Biaya': 'Total Biaya',
            'Jumlah_Pasien': 'Jumlah Pasien'
        }),
        use_container_width=True
    )
    
    # Grafik rata-rata biaya per poli
    st.subheader("Rata-rata Biaya per Poli (Top 10)")
    
    fig_biaya_poli, ax_biaya_poli = plt.subplots(figsize=(12, 6))
    bars_biaya = ax_biaya_poli.barh(range(len(top_10_poli)), top_10_poli['Rata_rata_Biaya'], 
                                   color='#764ba2', edgecolor='#667eea', alpha=0.8)
    ax_biaya_poli.set_yticks(range(len(top_10_poli)))
    ax_biaya_poli.set_yticklabels(top_10_poli.index)
    ax_biaya_poli.set_xlabel('Rata-rata Biaya')
    ax_biaya_poli.set_title('Rata-rata Biaya per Poli (Top 10)')
    
    # Tambah nilai di bar
    for i, bar in enumerate(bars_biaya):
        width = bar.get_width()
        ax_biaya_poli.text(width + 1000, bar.get_y() + bar.get_height()/2., 
                          f'Rp {width:,.0f}', ha='left', va='center', fontsize=9)
    
    st.pyplot(fig_biaya_poli)
st.markdown('</div>', unsafe_allow_html=True)

# Grafik 1: Distribusi Transaksi per Bulan
st.markdown('<div class="elegant-card">', unsafe_allow_html=True)
st.subheader("Distribusi Transaksi per Bulan")
bulan_counts = df['bulan'].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(bulan_counts.index, bulan_counts.values, color='#667eea', edgecolor='#764ba2', alpha=0.8)
ax.set_xlabel('Bulan')
ax.set_ylabel('Jumlah Transaksi')
ax.set_title('Distribusi Transaksi per Bulan')
ax.set_xticks(range(1, 13))

# Tambah nilai di atas bar
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 5,
            f'{int(height):,}', ha='center', va='bottom')

st.pyplot(fig)
st.markdown('</div>', unsafe_allow_html=True)

# Grafik 2: Rata-rata Biaya per Bulan
st.markdown('<div class="elegant-card">', unsafe_allow_html=True)
st.subheader("Rata-rata Biaya per Bulan")
biaya_per_bulan = df.groupby('bulan')['biaya'].mean()
fig2, ax2 = plt.subplots(figsize=(10, 6))
bars2 = ax2.bar(biaya_per_bulan.index, biaya_per_bulan.values, color='#764ba2', edgecolor='#667eea', alpha=0.8)
ax2.set_xlabel('Bulan')
ax2.set_ylabel('Rata-rata Biaya')
ax2.set_title('Rata-rata Biaya per Bulan')
ax2.set_xticks(range(1, 13))

# Format nilai di atas bar
for bar in bars2:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 10000,
            f'Rp {height:,.0f}', ha='center', va='bottom', fontsize=9)

st.pyplot(fig2)
st.markdown('</div>', unsafe_allow_html=True)

# Informasi tentang data negatif
if len(df[df['biaya'] < 0]) > 0:
    st.markdown('<div class="elegant-card">', unsafe_allow_html=True)
    st.info(f"**Catatan:** Terdapat **{len(df[df['biaya'] < 0]):,} transaksi negatif** ({(len(df[df['biaya'] < 0])/len(df)*100):.1f}%) yang mungkin merupakan refund atau koreksi transaksi.")
    st.markdown('</div>', unsafe_allow_html=True)

# ===== FOOTER ELEGAN =====
st.markdown("""
<div class="footer">
    <h3>Prediksi Belanja Pasien Rumah Sakit</h3>
    <p>Berbasis Akumulasi Data Historis | UTS Machine Learning - Magister Informatika UII</p>
    <p style="opacity: 0.8; margin-top: 1rem;">© 2025 Advanced Healthcare Analytics Dashboard</p>
</div>
""", unsafe_allow_html=True)
