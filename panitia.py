import streamlit as st
import pandas as pd

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Portal Panitia SKTB", layout="wide")

# URL CSV ANDA
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS5qSqI95YSC3Jkb_sLRrgHeczkOQJ8_DksqwhwqJdwXVsVhF2lvWnIxBJCV3JevbycF332KqyVhgxf/pub?output=csv"

# --- FUNGSI AMBIL DATA DARI CSV ---
@st.cache_data(ttl=60) 
def load_data():
    try:
        df = pd.read_csv(CSV_URL)
        df.columns = df.columns.str.strip()
        # Buat dictionary: Nama_Fail -> Link_Drive
        return pd.Series(df.Link_Drive.values, index=df.Nama_Fail).to_dict()
    except:
        return {}

data_links = load_data()

# --- FUNGSI RENDER LINK (PENTING UNTUK ELAK REFRESH) ---
def render_link(label, key):
    url = data_links.get(key, "")
    # Jika link kosong atau masih ada teks arahan, jangan buat <a> tag
    if pd.isna(url) or "http" not in str(url) or "[Tampal" in str(url):
        return f'<div style="color:#999; padding:10px; background:#f0f0f0; border-radius:8px; margin:5px 0; border-left:5px solid #ccc;">{label} <br><small>(Link belum dikemaskini di Sheet)</small></div>'
    else:
        # Gunakan target="_blank" supaya buka tab baru, bukan refresh portal
        return f'<a href="{url}" target="_blank" style="display:block; text-decoration:none; color:#333; padding:10px; background:white; border-radius:8px; margin:5px 0; border-left:5px solid #ad1457; font-weight:600; box-shadow: 2px 2px 5px rgba(0,0,0,0.05);">{label} 🔗</a>'

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background: #fff5f7; }
    .header-box { background: #ad1457; color: white; padding: 25px; border-radius: 15px; text-align: center; margin-bottom: 20px; }
    .card-title { background: #333; color: white; padding: 10px; border-radius: 10px 10px 0 0; text-align: center; font-weight: bold; }
    .fail-container { background: rgba(255,255,255,0.5); padding: 10px; border-radius: 0 0 10px 10px; border: 1px solid #ddd; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 2. SIDEBAR
with st.sidebar:
    st.title("🌸 MENU SKTB")
    pilihan = st.radio("Navigasi Panitia:", ["🏠 LAMAN UTAMA", "REKA BENTUK DAN TEKNOLOGI", "BAHASA MELAYU", "BAHASA INGGERIS", "MATEMATIK", "SAINS"])

if pilihan == "🏠 LAMAN UTAMA":
    st.markdown('<div class="header-box"><h1>PORTAL FAIL DIGITAL PANITIA</h1><p>Sila kemaskini pautan fail di Google Sheets anda.</p></div>', unsafe_allow_html=True)
else:
    st.markdown(f'<div class="header-box"><h1>{pilihan}</h1></div>', unsafe_allow_html=True)
    
    # Susunan Fail
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="card-title" style="background:#008B8B;">FAIL A</div>', unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="fail-container">', unsafe_allow_html=True)
            st.markdown(render_link("👤 Carta Organisasi", "Carta Organisasi Panitia"), unsafe_allow_html=True)
            st.markdown(render_link("📋 Biodata Guru", "Biodata & Jadual Waktu Guru"), unsafe_allow_html=True)
            st.markdown(render_link("📅 Jadual Pantau", "Jadual Pemantauan & Pencerapan"), unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card-title" style="background:#FF8C00;">FAIL B</div>', unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="fail-container">', unsafe_allow_html=True)
            st.markdown(render_link("📖 Minit Mesyuarat", "Minit Mesyuarat & Surat-Menyurat"), unsafe_allow_html=True)
            st.markdown(render_link("📜 DSKP", "Dokumen Standard Kurikulum (DSKP)"), unsafe_allow_html=True)
            st.markdown(render_link("📘 Manual PdPR", "Manual & Modul PdPR"), unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card-title" style="background:#800080;">FAIL C</div>', unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="fail-container">', unsafe_allow_html=True)
            st.markdown(render_link("📅 RPT & RPH", "Perancangan Pengajaran Tahunan & Harian"), unsafe_allow_html=True)
            st.markdown(render_link("🏆 Peningkatan", "Program Peningkatan Akademik"), unsafe_allow_html=True)
            st.markdown(render_link("📊 Carta Gantt", "Carta Gantt Perancangan"), unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="card-title" style="background:#2E8B57;">FAIL D</div>', unsafe_allow_html=True)
        with st.container():
            st.markdown('<div class="fail-container">', unsafe_allow_html=True)
            st.markdown(render_link("📊 PBD & UASA", "Pelaporan PBD & UASA"), unsafe_allow_html=True)
            st.markdown(render_link("📈 Analisis", "Analisis Peperiksaan Awam"), unsafe_allow_html=True)
            st.markdown(render_link("🏦 Bank Soalan", "Bank Soalan & Skema Permarkahan"), unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
