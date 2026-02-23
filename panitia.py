import streamlit as st
import pandas as pd
import time

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Portal Panitia SKTB", layout="wide")

# LINK GAMBAR
LOGO_URL = "https://lh3.googleusercontent.com/d/1XV1CIEWhms8jHqJGOKpSluqr7cxtSWrv"
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS5qSqI95YSC3Jkb_sLRrgHeczkOQJ8_DksqwhwqJdwXVsVhF2lvWnIxBJCV3JevbycF332KqyVhgxf/pub?output=csv"

# --- FUNGSI AMBIL DATA (SISTEM STABIL) ---
@st.cache_data(ttl=10) # Simpan memori 10 saat sahaja, supaya data sentiasa baru
def load_data():
    try:
        # Tambah parameter nocache supaya Google bagi data terkini
        df = pd.read_csv(f"{CSV_URL}&nocache={time.time()}")
        df.columns = df.columns.str.strip()
        return pd.Series(df.Link_Drive.values, index=df.Nama_Fail).to_dict()
    except:
        return {}

data_links = load_data()

# --- FUNGSI RENDER LINK (ANTI-PATAH BALIK) ---
def render_link(label, key):
    url = data_links.get(key, "")
    # Jika link kosong atau belum diisi
    if pd.isna(url) or "http" not in str(url) or "[Tampal" in str(url):
        return f'<div style="color:#999; padding:12px; background:#f0f0f0; border-radius:10px; margin:8px 0; border-left:5px solid #ccc; font-size:14px;">{label} <br><small>(Link Belum Dikemaskini)</small></div>'
    else:
        # Link sebenar yang tidak akan refresh portal
        return f'<a href="{url}" target="_blank" class="sublink">{label} 🔗</a>'

# --- CUSTOM CSS (Kekal Gaya Asal Anda) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
    .stApp { background: linear-gradient(135deg, #fff5f7 0%, #fce4ec 100%); background-attachment: fixed; }
    
    .subject-title-blink {
        color: #ad1457; font-size: 45px; font-weight: 900; text-align: center;
        font-family: 'Pacifico', cursive; margin-bottom: 20px;
    }

    .card { border-radius: 20px; padding: 20px; text-align: center; color: white; font-weight: bold; height: 120px; display: flex; align-items: center; justify-content: center; margin-bottom: 10px; }
    .color-a { background: linear-gradient(135deg, #008B8B, #20B2AA); }
    .color-b { background: linear-gradient(135deg, #FF8C00, #FFA500); }
    .color-c { background: linear-gradient(135deg, #800080, #9370DB); }
    .color-d { background: linear-gradient(135deg, #2E8B57, #3CB371); }

    .sublink { 
        display: block; padding: 12px; text-decoration: none !important; color: #000 !important; 
        font-weight: 600; border-radius: 10px; margin: 8px 0; background: white; 
        border-left: 6px solid #ad1457; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); transition: 0.3s;
    }
    .sublink:hover { transform: translateX(10px); background: #fce4ec; }
    
    [data-testid="stSidebar"] { background-color: #fce4ec !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. SIDEBAR
with st.sidebar:
    st.image(LOGO_URL, width=100)
    st.markdown("### 🌸 MENU SKTB")
    pilihan = st.radio("Pilih Panitia:", ["🏠 LAMAN UTAMA", "REKA BENTUK DAN TEKNOLOGI", "BAHASA MELAYU", "BAHASA INGGERIS", "MATEMATIK", "SAINS"])
    
    # Butang refresh manual jika pautan tak muncul
    if st.button("🔄 Segarkan Pautan"):
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
        st.markdown(render_link("👤 Carta Organisasi", "Carta Organisasi Panitia"), unsafe_allow_html=True)
        st.markdown(render_link("📋 Biodata Guru", "Biodata & Jadual Waktu Guru"), unsafe_allow_html=True)
        st.markdown(render_link("📅 Jadual Pantau", "Jadual Pemantauan & Pencerapan"), unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card color-b">FAIL B<br>KURIKULUM</div>', unsafe_allow_html=True)
        st.markdown(render_link("📖 Minit Mesyuarat", "Minit Mesyuarat & Surat-Menyurat"), unsafe_allow_html=True)
        st.markdown(render_link("📜 DSKP", "Dokumen Standard Kurikulum (DSKP)"), unsafe_allow_html=True)
        st.markdown(render_link("📘 Manual PdPR", "Manual & Modul PdPR"), unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card color-c">FAIL C<br>PERANCANGAN</div>', unsafe_allow_html=True)
        st.markdown(render_link("📅 RPT & RPH", "Perancangan Pengajaran Tahunan & Harian"), unsafe_allow_html=True)
        st.markdown(render_link("🏆 Peningkatan", "Program Peningkatan Akademik"), unsafe_allow_html=True)
        st.markdown(render_link("📝 Laporan Program", "Laporan Program Panitia"), unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="card color-d">FAIL D<br>PENILAIAN</div>', unsafe_allow_html=True)
        st.markdown(render_link("📊 PBD & UASA", "Pelaporan PBD & UASA"), unsafe_allow_html=True)
        st.markdown(render_link("📈 Analisis", "Analisis Peperiksaan Awam"), unsafe_allow_html=True)
        st.markdown(render_link("🏦 Bank Soalan", "Bank Soalan & Skema Permarkahan"), unsafe_allow_html=True)
