import streamlit as st
import pandas as pd

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Portal Panitia SKTB", layout="wide")

# LINK GAMBAR ASAL (LOGO & PENTADBIR)
LOGO_URL = "https://lh3.googleusercontent.com/d/1XV1CIEWhms8jHqJGOKpSluqr7cxtSWrv"
PENTADBIR_URL = "https://lh3.googleusercontent.com/d/1m87eH4bQ-p51DCMVjvM2ID8QgtwNF9ul"

# URL CSV ANDA
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS5qSqI95YSC3Jkb_sLRrgHeczkOQJ8_DksqwhwqJdwXVsVhF2lvWnIxBJCV3JevbycF332KqyVhgxf/pub?output=csv"

# --- FUNGSI FIX LINK GOOGLE DRIVE ---
def fix_drive_url(url):
    if not isinstance(url, str) or url == "#": return "#"
    return url

# --- FUNGSI AMBIL DATA DARI CSV ---
@st.cache_data(ttl=600) # Simpan cache selama 10 minit
def load_data():
    try:
        df = pd.read_csv(CSV_URL)
        # Kita buat dictionary: Nama_Fail sebagai KEY, Link_Drive sebagai VALUE
        links_dict = pd.Series(df.Link_Drive.values, index=df.Nama_Fail).to_dict()
        return links_dict
    except Exception as e:
        st.error(f"Gagal memuatkan data CSV: {e}")
        return {}

# Panggil fungsi untuk ambil pautan sebenar dari CSV
data_links = load_data()

# --- CUSTOM CSS (Sama seperti asal) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
    .stApp { background: linear-gradient(135deg, #fff5f7 0%, #fce4ec 100%); background-attachment: fixed; }
    .super-center { display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; width: 100%; margin: 0 auto; }
    @keyframes blinker { 0% { opacity: 1; } 50% { opacity: 0.2; } 100% { opacity: 1; } }
    .subject-title-blink { color: #ad1457; font-size: 50px; font-weight: 900; animation: blinker 3s linear infinite; line-height: 1.2; margin-top: 15px; text-align: left; }
    .cursive-blink { font-family: 'Dancing Script', cursive; font-size: 95px; color: #ad1457; animation: blinker 3s linear infinite; margin-bottom: 0px; }
    .portal-text { color: #000000 !important; font-size: 38px; font-weight: 800; margin-top: 10px; }
    .year-text { color: #ad1457; font-size: 45px; font-weight: 900; letter-spacing: 2px; margin-bottom: 30px; }
    .head-img-container { display: flex; justify-content: flex-end; align-items: center; padding-right: 20px; }
    .head-img { width: 180px; height: 180px; border-radius: 50%; border: 6px solid #ad1457; background-color: #fce4ec; object-fit: cover; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }
    [data-testid="stSidebar"] { background-color: #fce4ec !important; border-right: 2px solid #f8bbd0; }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, div[role="radiogroup"] label p { color: #000000 !important; font-weight: 800 !important; font-size: 16px !important; }
    .card { border-radius: 20px; padding: 25px; text-align: center; color: #FFFFFF !important; font-weight: bold !important; height: 180px; display: flex; flex-direction: column; justify-content: center; margin-bottom: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
    .color-a { background: linear-gradient(135deg, #008B8B, #20B2AA); }
    .color-b { background: linear-gradient(135deg, #FF8C00, #FFA500); }
    .color-c { background: linear-gradient(135deg, #800080, #9370DB); }
    .color-d { background: linear-gradient(135deg, #2E8B57, #3CB371); }
    .stExpander { background-color: #AED6F1 !important; border-radius: 12px !important; }
    .sublink { display: block; padding: 12px; text-decoration: none !important; color: #000000 !important; font-weight: 600; border-radius: 10px; margin: 8px 0; transition: 0.3s; }
    .sublink:hover { background-color: #fce4ec !important; color: #ad1457 !important; transform: translateX(10px); }
    </style>
    """, unsafe_allow_html=True)

# 2. MENU SIDEBAR
with st.sidebar:
    st.image(LOGO_URL, width=100)
    st.markdown("<h2 style='text-align: center; color: black; margin-top: 0;'>🌸 MENU SKTB</h2>", unsafe_allow_html=True)
    pilihan = st.radio(
        "Navigasi:",
        ["🏠 LAMAN UTAMA", "REKA BENTUK DAN TEKNOLOGI", "BAHASA MELAYU", "BAHASA INGGERIS", "MATEMATIK", "SAINS", "PENDIDIKAN ISLAM", "SEJARAH", "PENDIDIKAN JASMANI DAN KESIHATAN", "PENDIDIKAN SENI VISUAL", "PENDIDIKAN MUZIK", "BAHASA ARAB"]
    )

# --- 3. LAMAN UTAMA ---
if pilihan == "🏠 LAMAN UTAMA":
    st.markdown(f"""
        <div class="super-center">
            <img src="{LOGO_URL}" width="220">
            <div class="cursive-blink">Selamat Datang</div>
            <div class="portal-text">PORTAL FAIL DIGITAL PENGURUSAN PANITIA</div>
            <div class="year-text">SEK. KEB. TELOK BEREMBANG 2026</div>
            <img src="{PENTADBIR_URL}" class="admin-img-box">
        </div>
    """, unsafe_allow_html=True)

# --- 4. LAMAN PANITIA ---
else:
    # Memetakan data dari CSV secara dinamik berdasarkan Nama_Fail yang ada dalam CSV anda
    links = {
        "Carta": data_links.get("Carta Organisasi Panitia", "#"),
        "Biodata": data_links.get("Biodata & Jadual Waktu Guru", "#"),
        "Jadual_M": data_links.get("Jadual Pemantauan & Pencerapan", "#"),
        "Enrolmen": data_links.get("Data Enrolmen Murid", "#"),
        "Kewangan": data_links.get("Pengurusan Kewangan Panitia (PCG)", "#"),
        "Minit": data_links.get("Minit Mesyuarat & Surat-Menyurat", "#"),
        "DSKP": data_links.get("Dokumen Standard Kurikulum (DSKP)", "#"),
        "Manual": data_links.get("Manual & Modul PdPR", "#"),
        "BBM": data_links.get("Bahan Bantu Mengajar (BBM) & Rujukan", "#"),
        "RPT": data_links.get("Perancangan Pengajaran Tahunan & Harian", "#"),
        "Akademik": data_links.get("Program Peningkatan Akademik", "#"),
        "Gantt": data_links.get("Carta Gantt Perancangan", "#"),
        "Laporan": data_links.get("Laporan Program Panitia", "#"),
        "PLC": data_links.get("Program Perkembangan Staf (LDP/PLC)", "#"),
        "PBD": data_links.get("Pelaporan PBD & UASA", "#"),
        "Analisis": data_links.get("Analisis Peperiksaan Awam", "#"),
        "Jadual_E": data_links.get("Jadual Peperiksaan & Penggubal Soalan", "#"),
        "JSU": data_links.get("Analisis Item & JSU", "#"),
        "Bank": data_links.get("Bank Soalan & Skema Permarkahan", "#")
    }

    # Paparan Atas
    st.markdown(f'<div style="text-align:center; color:black; font-family:Pacifico; font-size:30px; margin-bottom:10px;">📂 Portal Fail Digital Pengurusan Panitia</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="text-align:center;"><h1 class="subject-title-blink" style="text-align:center;">{pilihan}</h1></div>', unsafe_allow_html=True)
    st.divider()

    # Susunan Fail
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="card color-a">🔵 FAIL A<br>MAKLUMAT PANITIA</div>', unsafe_allow_html=True)
        with st.expander("BUKA FAIL A"):
            st.markdown(f'<a class="sublink" href="{links["Carta"]}" target="_blank">👤 Carta Organisasi</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Biodata"]}" target="_blank">📋 Biodata & Jadual Guru</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Jadual_M"]}" target="_blank">📅 Jadual Pemantauan</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Enrolmen"]}" target="_blank">👥 Data Enrolmen</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Kewangan"]}" target="_blank">💰 Pengurusan Kewangan</a>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card color-b">🟠 FAIL B<br>KURIKULUM</div>', unsafe_allow_html=True)
        with st.expander("BUKA FAIL B"):
            st.markdown(f'<a class="sublink" href="{links["Minit"]}" target="_blank">📖 Minit Mesyuarat</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["DSKP"]}" target="_blank">📜 DSKP</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Manual"]}" target="_blank">📘 Manual & Modul</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["BBM"]}" target="_blank">📦 BBM</a>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card color-c">🟣 FAIL C<br>PERANCANGAN</div>', unsafe_allow_html=True)
        with st.expander("BUKA FAIL C"):
            st.markdown(f'<a class="sublink" href="{links["RPT"]}" target="_blank">📅 RPT & RPH</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Akademik"]}" target="_blank">🏆 Peningkatan Akademik</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Gantt"]}" target="_blank">📊 Carta Gantt</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Laporan"]}" target="_blank">📝 Laporan Program</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["PLC"]}" target="_blank">🤝 LDP / PLC</a>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="card color-d">🟢 FAIL D<br>PEPERIKSAAN</div>', unsafe_allow_html=True)
        with st.expander("BUKA FAIL D"):
            st.markdown(f'<a class="sublink" href="{links["PBD"]}" target="_blank">📊 Pelaporan PBD & UASA</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Analisis"]}" target="_blank">📈 Analisis Peperiksaan Awam</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Jadual_E"]}" target="_blank">🕒 Jadual & Penggubal</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["JSU"]}" target="_blank">📑 Analisis Item & JSU</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Bank"]}" target="_blank">🏦 Bank Soalan</a>', unsafe_allow_html=True)

    st.divider()
    st.markdown(f'<p style="text-align: center; color: black; font-weight: bold;">Portal Panitia {pilihan} - SEK. KEB. TELOK BEREMBANG 2026</p>', unsafe_allow_html=True)
