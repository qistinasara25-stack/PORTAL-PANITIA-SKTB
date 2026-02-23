import streamlit as st
import pandas as pd
import time

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Portal Panitia SKTB", layout="wide")

# LINK GAMBAR & DATA
LOGO_URL = "https://lh3.googleusercontent.com/d/1XV1CIEWhms8jHqJGOKpSluqr7cxtSWrv"
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS5qSqI95YSC3Jkb_sLRrgHeczkOQJ8_DksqwhwqJdwXVsVhF2lvWnIxBJCV3JevbycF332KqyVhgxf/pub?output=csv"

# --- FUNGSI AMBIL DATA DARI CSV ---
@st.cache_data(ttl=5) 
def load_data():
    try:
        df = pd.read_csv(f"{CSV_URL}&cb={time.time()}")
        df.columns = df.columns.str.strip()
        return pd.Series(df.Link_Drive.values, index=df.Nama_Fail).to_dict()
    except:
        return {}

data_links = load_data()

# --- CUSTOM CSS (KEKAL RUPA ASAL DALAM GAMBAR) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
    
    .stApp { background: linear-gradient(135deg, #fff5f7 0%, #fce4ec 100%); background-attachment: fixed; }
    
    /* Subject Title Style */
    .subject-title-blink {
        color: #ad1457; font-size: 50px; font-weight: 900; text-align: center;
        font-family: 'Pacifico', cursive; margin-bottom: 20px;
        animation: blinker 3s linear infinite;
    }
    @keyframes blinker { 0% { opacity: 1; } 50% { opacity: 0.2; } 100% { opacity: 1; } }

    /* Card Styling */
    .card { border-radius: 20px; padding: 25px; text-align: center; color: white; font-weight: bold; height: 120px; display: flex; align-items: center; justify-content: center; margin-bottom: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
    .color-a { background: linear-gradient(135deg, #008B8B, #20B2AA); }
    .color-b { background: linear-gradient(135deg, #FF8C00, #FFA500); }
    .color-c { background: linear-gradient(135deg, #800080, #9370DB); }
    .color-d { background: linear-gradient(135deg, #2E8B57, #3CB371); }

    /* --- BAR HITAM PADA EXPANDER --- */
    .stExpander { border: none !important; box-shadow: none !important; margin-bottom: 10px !important; }
    .stExpander details summary {
        background-color: #1a1a1a !important; 
        border-radius: 8px !important;
        padding: 10px !important;
        color: #00A8A8 !important;
    }
    
    .stExpander details summary p { 
        color: #00A8A8 !important; 
        font-weight: 900 !important; 
        font-size: 20px !important;
        margin: 0 !important;
    }

    /* Sidebar Style Asal */
    [data-testid="stSidebar"] { background-color: #fce4ec !important; border-right: 2px solid #f8bbd0; }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span { color: #000 !important; font-weight: 800 !important; }
    div[role="radiogroup"] label:hover { background-color: #f8bbd0 !important; transform: translateX(10px); cursor: pointer; }
    
    /* Sublink Styling */
    .sublink { display: block; padding: 10px; text-decoration: none !important; color: #333 !important; font-weight: 600; border-radius: 8px; margin: 5px 0; background: #e0f2f1; transition: 0.3s; border-left: 4px solid #ad1457; }
    .sublink:hover { transform: translateX(5px); background: #fce4ec; }
    </style>
    """, unsafe_allow_html=True)

# 2. SIDEBAR MENU
with st.sidebar:
    st.image(LOGO_URL, width=100)
    st.markdown("<h2 style='text-align: center; color: black;'>🌸 MENU SKTB</h2>", unsafe_allow_html=True)
    pilihan = st.radio("Navigasi:", ["🏠 LAMAN UTAMA", "REKA BENTUK DAN TEKNOLOGI", "BAHASA MELAYU", "BAHASA INGGERIS", "MATEMATIK", "SAINS", "PENDIDIKAN ISLAM", "SEJARAH", "PENDIDIKAN JASMANI DAN KESIHATAN", "PENDIDIKAN SENI VISUAL", "PENDIDIKAN MUZIK", "BAHASA ARAB"])

def get_url(key):
    val = data_links.get(key, "#")
    return "#" if "[Tampal" in str(val) else val

# --- HALAMAN UTAMA ---
if pilihan == "🏠 LAMAN UTAMA":
    st.markdown('<div class="subject-title-blink" style="font-size: 70px; margin-top: 50px;">Selamat Datang</div>', unsafe_allow_html=True)
else:
    st.markdown(f'<div class="subject-title-blink">{pilihan}</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="card color-a">FAIL A<br>MAKLUMAT PANITIA</div>', unsafe_allow_html=True)
        # expanded=False supaya sub-fail tidak terus keluar
        with st.expander("FAIL A 👆", expanded=False):
            st.markdown(f'<a class="sublink" href="{get_url("Carta Organisasi Panitia")}" target="_blank">👤 Carta Organisasi</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{get_url("Biodata & Jadual Waktu Guru")}" target="_blank">📋 Biodata & Jadual</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{get_url("Jadual Pemantauan & Pencerapan")}" target="_blank">📅 Jadual Pemantauan</a>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card color-b">FAIL B<br>KURIKULUM</div>', unsafe_allow_html=True)
        with st.expander("FAIL B 👆", expanded=False):
            st.markdown(f'<a class="sublink" href="{get_url("Minit Mesyuarat & Surat-Menyurat")}" target="_blank">📖 Minit Mesyuarat</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{get_url("Dokumen Standard Kurikulum (DSKP)")}" target="_blank">📜 DSKP</a>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card color-c">FAIL C<br>PERANCANGAN</div>', unsafe_allow_html=True)
        with st.expander("FAIL C 👆", expanded=False):
            st.markdown(f'<a class="sublink" href="{get_url("Perancangan Pengajaran Tahunan & Harian")}" target="_blank">📅 RPT & RPH</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{get_url("Program Peningkatan Akademik")}" target="_blank">🏆 Peningkatan</a>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="card color-d">FAIL D<br>PENILAIAN</div>', unsafe_allow_html=True)
        with st.expander("FAIL D 👆", expanded=False):
            st.markdown(f'<a class="sublink" href="{get_url("Pelaporan PBD & UASA")}" target="_blank">📊 PBD & UASA</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{get_url("Analisis Peperiksaan Awam")}" target="_blank">📈 Analisis</a>', unsafe_allow_html=True)
