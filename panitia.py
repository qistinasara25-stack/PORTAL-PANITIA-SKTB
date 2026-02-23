import streamlit as st
import pandas as pd
import time

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Portal Panitia SKTB", layout="wide")

# LINK GAMBAR & DATA
LOGO_URL = "https://lh3.googleusercontent.com/d/11avGiH5w__vXztmo0sjltE46kYgCnNuN" # Logo Sekolah
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS5qSqI95YSC3Jkb_sLRrgHeczkOQJ8_DksqwhwqJdwXVsVhF2lvWnIxBJCV3JevbycF332KqyVhgxf/pub?output=csv"

# --- FUNGSI AMBIL DATA (STABIL) ---
@st.cache_data(ttl=5) 
def load_data():
    try:
        # Guna timestamp untuk elak cache lama
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

# --- CUSTOM CSS (KEMBALIKAN SEMUA KESAN ASAL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
    
    /* Background Keseluruhan */
    .stApp { background: linear-gradient(135deg, #fff5f7 0%, #fce4ec 100%); background-attachment: fixed; }
    
    /* Tajuk Subjek Berkelip */
    .subject-title-blink {
        color: #ad1457; font-size: 55px; font-weight: 900; text-align: center;
        font-family: 'Pacifico', cursive; margin-bottom: 30px;
        animation: blinker 3s linear infinite;
    }
    @keyframes blinker { 0% { opacity: 1; } 50% { opacity: 0.2; } 100% { opacity: 1; } }

    /* Kad Fail (FAIL A, B, C, D) */
    .card { border-radius: 20px; padding: 25px; text-align: center; color: white; font-weight: bold; height: 140px; display: flex; align-items: center; justify-content: center; margin-bottom: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); font-size: 22px; }
    .color-a { background: linear-gradient(135deg, #008B8B, #20B2AA); }
    .color-b { background: linear-gradient(135deg, #FF8C00, #FFA500); }
    .color-c { background: linear-gradient(135deg, #800080, #9370DB); }
    .color-d { background: linear-gradient(135deg, #2E8B57, #3CB371); }

    /* Gaya Expander (Tukar Hitam ke Pink) */
    .stExpander { border: none !important; background-color: transparent !important; }
    .stExpander details summary {
        background-color: #ad1457 !important; color: white !important;
        border-radius: 15px !important; padding: 12px !important;
        font-weight: bold !important; margin-bottom: 5px;
    }
    .stExpander details summary p { color: white !important; font-size: 18px !important; margin: 0; }
    .stExpander details [data-testid="stMarkdownContainer"] { background: rgba(255,255,255,0.3); border-radius: 15px; padding: 10px; }

    /* Butang Pautan (Hover Effect) */
    .sublink { 
        display: block; padding: 12px; text-decoration: none !important; color: #000 !important; 
        font-weight: 600; border-radius: 10px; margin: 8px 0; background: white; 
        border-left: 6px solid #ad1457; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); transition: 0.3s;
    }
    .sublink:hover { transform: translateX(10px); background: #fce4ec; color: #ad1457 !important; }
    
    /* Sidebar Kesan Khas (Hover) */
    [data-testid="stSidebar"] { background-color: #fce4ec !important; border-right: 2px solid #f8bbd0; }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span { color: #000 !important; font-weight: 800 !important; }
    div[role="radiogroup"] label { padding: 10px !important; border-radius: 10px !important; transition: 0.3s ease !important; }
    div[role="radiogroup"] label:hover { background-color: #f8bbd0 !important; transform: translateX(10px); cursor: pointer; }
    div[role="radiogroup"] label:hover p { color: #ad1457 !important; font-weight: 900 !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. SIDEBAR
with st.sidebar:
    st.image(LOGO_URL, width=120)
    st.markdown("<h2 style='text-align: center; color: black;'>🌸 MENU SKTB</h2>", unsafe_allow_html=True)
    pilihan = st.radio(
        "Navigasi:",
        ["🏠 LAMAN UTAMA", "REKA BENTUK DAN TEKNOLOGI", "BAHASA MELAYU", "BAHASA INGGERIS", "MATEMATIK", "SAINS", "PENDIDIKAN ISLAM", "SEJARAH", "PENDIDIKAN JASMANI DAN KESIHATAN", "PENDIDIKAN SENI VISUAL", "PENDIDIKAN MUZIK", "BAHASA ARAB"]
    )
    st.button("🔄 Segarkan Data", on_click=lambda: st.cache_data.clear())

# --- HALAMAN UTAMA ---
if pilihan == "🏠 LAMAN UTAMA":
    st.markdown('<div class="subject-title-blink" style="font-size: 70px; margin-top: 50px;">Selamat Datang</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center; font-size:30px; color:#ad1457; font-weight:800;">PORTAL FAIL DIGITAL PANITIA 2026</div>', unsafe_allow_html=True)
else:
    st.markdown(f'<div class="subject-title-blink">{pilihan}</div>', unsafe_allow_html=True)
    
    # SUSUNAN 4 LAJUR SEPERTI ASAL
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="card color-a">FAIL A<br>MAKLUMAT PANITIA</div>', unsafe_allow_html=True)
        with st.expander("FAIL A 👇", expanded=True):
            st.markdown(render_link("👤 Carta Organisasi", "Carta Organisasi Panitia"), unsafe_allow_html=True)
            st.markdown(render_link("📋 Biodata & Jadual Guru", "Biodata & Jadual Waktu Guru"), unsafe_allow_html=True)
            st.markdown(render_link("📅 Jadual Pemantauan", "Jadual Pemantauan & Pencerapan"), unsafe_allow_html=True)
            st.markdown(render_link("👥 Data Enrolmen", "Data Enrolmen Murid"), unsafe_allow_html=True)
            st.markdown(render_link("💰 Pengurusan Kewangan", "Pengurusan Kewangan Panitia (PCG)"), unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card color-b">FAIL B<br>KURIKULUM</div>', unsafe_allow_html=True)
        with st.expander("FAIL B 👇", expanded=True):
            st.markdown(render_link("📖 Minit Mesyuarat", "Minit Mesyuarat & Surat-Menyurat"), unsafe_allow_html=True)
            st.markdown(render_link("📜 DSKP", "Dokumen Standard Kurikulum (DSKP)"), unsafe_allow_html=True)
            st.markdown(render_link("📘 Manual & Modul", "Manual & Modul PdPR"), unsafe_allow_html=True)
            st.markdown(render_link("📦 BBM", "Bahan Bantu Mengajar (BBM) & Rujukan"), unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card color-c">FAIL C<br>PERANCANGAN</div>', unsafe_allow_html=True)
        with st.expander("FAIL C 👇", expanded=True):
            st.markdown(render_link("📅 RPT & RPH", "Perancangan Pengajaran Tahunan & Harian"), unsafe_allow_html=True)
            st.markdown(render_link("🏆 Peningkatan Akademik", "Program Peningkatan Akademik"), unsafe_allow_html=True)
            st.markdown(render_link("📊 Carta Gantt", "Carta Gantt Perancangan"), unsafe_allow_html=True)
            st.markdown(render_link("📝 Laporan Program", "Laporan Program Panitia"), unsafe_allow_html=True)
            st.markdown(render_link("🤝 LDP / PLC", "Program Perkembangan Staf (LDP/PLC)"), unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="card color-d">FAIL D<br>PENILAIAN</div>', unsafe_allow_html=True)
        with st.expander("FAIL D 👇", expanded=True):
            st.markdown(render_link("📊 Pelaporan PBD & UASA", "Pelaporan PBD & UASA"), unsafe_allow_html=True)
            st.markdown(render_link("📈 Analisis Peperiksaan", "Analisis Peperiksaan Awam"), unsafe_allow_html=True)
            st.markdown(render_link("🕒 Jadual & Penggubal", "Jadual Peperiksaan & Penggubal Soalan"), unsafe_allow_html=True)
            st.markdown(render_link("📑 Analisis Item & JSU", "Analisis Item & JSU"), unsafe_allow_html=True)
            st.markdown(render_link("🏦 Bank Soalan", "Bank Soalan & Skema Permarkahan"), unsafe_allow_html=True)

    st.divider()
    st.markdown(f'<p style="text-align: center; color: black; font-weight: bold;">SK. KEB. TELOK BEREMBANG 2026</p>', unsafe_allow_html=True)
