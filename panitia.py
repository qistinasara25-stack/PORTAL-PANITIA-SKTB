import streamlit as st
import pandas as pd
import time

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Portal Panitia SKTB", layout="wide")

# LINK GAMBAR & DATA
LOGO_URL = "https://lh3.googleusercontent.com/d/1XV1CIEWhms8jHqJGOKpSluqr7cxtSWrv"
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS5qSqI95YSC3Jkb_sLRrgHeczkOQJ8_DksqwhwqJdwXVsVhF2lvWnIxBJCV3JevbycF332KqyVhgxf/pub?output=csv"

# --- FUNGSI AMBIL DATA (STABIL & FRESH) ---
@st.cache_data(ttl=5) 
def load_data():
    try:
        # Guna timestamp untuk elak cache lama dari Google
        df = pd.read_csv(f"{CSV_URL}&cb={time.time()}")
        df.columns = df.columns.str.strip()
        return pd.Series(df.Link_Drive.values, index=df.Nama_Fail).to_dict()
    except:
        return {}

data_links = load_data()

# --- FUNGSI RENDER LINK (ANTI-REFRESH) ---
def render_link(label, key):
    url = data_links.get(key, "")
    if pd.isna(url) or "http" not in str(url) or "[Tampal" in str(url):
        return f'<div style="color:#999; padding:12px; background:#f0f0f0; border-radius:10px; margin:8px 0; border-left:5px solid #ccc; font-size:14px;">{label} <br><small>(Link Belum Ada)</small></div>'
    else:
        return f'<a href="{url}" target="_blank" class="sublink">{label} 🔗</a>'

# --- CUSTOM CSS (KEMASKINI WARNA PINK PADA TAB) ---
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

    /* --- TUKAR WARNA HITAM PADA EXPANDER KEPADA PINK --- */
    .stExpander {
        background-color: #AED6F1 !important; /* Warna background dalam isi */
        border: none !important;
        border-radius: 15px !important;
        overflow: hidden !important;
    }
    
    .stExpander details summary {
        background-color: #ad1457 !important; /* Bar tajuk jadi Pink Pekat */
        color: white !important;
        border-radius: 15px 15px 0 0 !important;
        padding: 10px !important;
        font-weight: bold !important;
    }
    
    .stExpander details summary p {
        color: white !important; /* Pastikan teks FAIL A, B dsb jadi putih */
        font-size: 18px !important;
    }

    /* Link Button Styling */
    .sublink { 
        display: block; padding: 12px; text-decoration: none !important; color: #000 !important; 
        font-weight: 600; border-radius: 10px; margin: 8px 0; background: white; 
        border-left: 6px solid #ad1457; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); transition: 0.3s;
    }
    .sublink:hover { transform: translateX(10px); background: #fce4ec; color: #ad1457 !important; }
    
    /* SIDEBAR KESAN KHAS (HOVER) */
    [data-testid="stSidebar"] { background-color: #fce4ec !important; border-right: 2px solid #f8bbd0; }
    
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
        color: #000000 !important; font-weight: 800 !important; transition: all 0.3s ease;
    }

    div[role="radiogroup"] label {
        padding: 10px !important; border-radius: 10px !important; margin-bottom: 5px !important;
        transition: all 0.3s ease !important;
    }

    div[role="radiogroup"] label:hover {
        background-color: #f8bbd0 !important;
        transform: translateX(10px);
        cursor: pointer;
    }

    div[role="radiogroup"] label:hover p {
        color: #ad1457 !important; font-weight: 900 !important; font-size: 17px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. SIDEBAR MENU
with st.sidebar:
    st.image(LOGO_URL, width=100)
    st.markdown("<h2 style='text-align: center; color: black;'>🌸 MENU SKTB</h2>", unsafe_allow_html=True)
    pilihan = st.radio(
        "Navigasi:",
        ["🏠 LAMAN UTAMA", "REKA BENTUK DAN TEKNOLOGI", "BAHASA MELAYU", "BAHASA INGGERIS", "MATEMATIK", "SAINS", "PENDIDIKAN ISLAM", "SEJARAH", "PENDIDIKAN JASMANI DAN KESIHATAN", "PENDIDIKAN SENI VISUAL", "PENDIDIKAN MUZIK", "BAHASA ARAB"]
    )
    
    if st.button("🔄 Segarkan Data Baru"):
        st.cache_data.clear()
        st.rerun()

# --- HALAMAN UTAMA ---
if pilihan == "🏠 LAMAN UTAMA":
    st.markdown('<div class="subject-title-blink">Selamat Datang ke Portal Fail Digital</div>', unsafe_allow_html=True)
else:
    st.markdown(f'<div class="subject-title-blink">{pilihan}</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="card color-a">FAIL A<br>MAKLUMAT</div>', unsafe_allow_html=True)
        with st.expander("FAIL A 👇", expanded=True):
            st.markdown(render_link("👤 Carta Organisasi", "Carta Organisasi Panitia"), unsafe_allow_html=True)
            st.markdown(render_link("📋 Biodata Guru", "Biodata & Jadual Waktu Guru"), unsafe_allow_html=True)
            st.markdown(render_link("📅 Jadual Pantau", "Jadual Pemantauan & Pencerapan"), unsafe_allow_html=True)
            st.markdown(render_link("👥 Data Enrolmen", "Data Enrolmen Murid"), unsafe_allow_html=True)
            st.markdown(render_link("💰 Kewangan", "Pengurusan Kewangan Panitia (PCG)"), unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card color-b">FAIL B<br>KURIKULUM</div>', unsafe_allow_html=True)
        with st.expander("FAIL B 👇", expanded=True):
            st.markdown(render_link("📖 Minit Mesyuarat", "Minit Mesyuarat & Surat-Menyurat"), unsafe_allow_html=True)
            st.markdown(render_link("📜 DSKP", "Dokumen Standard Kurikulum (DSKP)"), unsafe_allow_html=True)
            st.markdown(render_link("📘 Manual PdPR", "Manual & Modul PdPR"), unsafe_allow_html=True)
            st.markdown(render_link("📦 BBM", "Bahan Bantu Mengajar (BBM) & Rujukan"), unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card color-c">FAIL C<br>PERANCANGAN</div>', unsafe_allow_html=True)
        with st.expander("FAIL C 👇", expanded=True):
            st.markdown(render_link("📅 RPT & RPH", "Perancangan Pengajaran Tahunan & Harian"), unsafe_allow_html=True)
            st.markdown(render_link("🏆 Akademik", "Program Peningkatan Akademik"), unsafe_allow_html=True)
            st.markdown(render_link("📊 Carta Gantt", "Carta Gantt Perancangan"), unsafe_allow_html=True)
            st.markdown(render_link("📝 Laporan Program", "Laporan Program Panitia"), unsafe_allow_html=True)
            st.markdown(render_link("🤝 LDP / PLC", "Program Perkembangan Staf (LDP/PLC)"), unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="card color-d">FAIL D<br>PENILAIAN</div>', unsafe_allow_html=True)
        with st.expander("FAIL D 👇", expanded=True):
            st.markdown(render_link("📊 PBD & UASA", "Pelaporan PBD & UASA"), unsafe_allow_html=True)
            st.markdown(render_link("📈 Analisis Awam", "Analisis Peperiksaan Awam"), unsafe_allow_html=True)
            st.markdown(render_link("🕒 Jadual Peperiksaan", "Jadual Peperiksaan & Penggubal Soalan"), unsafe_allow_html=True)
            st.markdown(render_link("📑 Analisis Item", "Analisis Item & JSU"), unsafe_allow_html=True)
            st.markdown(render_link("🏦 Bank Soalan", "Bank Soalan & Skema Permarkahan"), unsafe_allow_html=True)

    st.divider()
    st.markdown(f'<p style="text-align: center; color: black; font-weight: bold;">SK. KEB. TELOK BEREMBANG 2026</p>', unsafe_allow_html=True)
