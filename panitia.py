
import streamlit as st
import pandas as pd

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Portal Panitia SKTB", layout="wide")

# LINK GAMBAR ASAL
LOGO_URL = "https://lh3.googleusercontent.com/d/1XV1CIEWhms8jHqJGOKpSluqr7cxtSWrv"
PENTADBIR_URL = "https://lh3.googleusercontent.com/d/1m87eH4bQ-p51DCMVjvM2ID8QgtwNF9ul"

# URL CSV ANDA
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS5qSqI95YSC3Jkb_sLRrgHeczkOQJ8_DksqwhwqJdwXVsVhF2lvWnIxBJCV3JevbycF332KqyVhgxf/pub?output=csv"

# --- FUNGSI AMBIL DATA DARI CSV ---
@st.cache_data(ttl=60)
def load_data():
    try:
        df = pd.read_csv(CSV_URL)
        df.columns = df.columns.str.strip()
        return pd.Series(df.Link_Drive.values, index=df.Nama_Fail).to_dict()
    except:
        return {}

data_links = load_data()

# --- FUNGSI FIX LINK GOOGLE DRIVE ---
def fix_drive_url(url):
    if not isinstance(url, str): return url
    if "drive.google.com" in url:
        try:
            if "/file/d/" in url:
                file_id = url.split("/file/d/")[1].split("/")[0]
            elif "id=" in url:
                file_id = url.split("id=")[1].split("&")[0]
            else:
                return url
            return f"https://drive.google.com/thumbnail?id={file_id}&sz=w800"
        except:
            return url
    return url

# --- CUSTOM CSS (KEKAL ASAL DENGAN UPDATE WARNA BULATAN) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
    
    .stApp { background: linear-gradient(135deg, #fff5f7 0%, #fce4ec 100%); background-attachment: fixed; }
    .super-center { display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; width: 100%; margin: 0 auto; }
    
    @keyframes blinker { 0% { opacity: 1; } 50% { opacity: 0.2; } 100% { opacity: 1; } }

    .subject-title-blink {
        color: #ad1457;
        font-size: 50px;
        font-weight: 900;
        animation: blinker 3s linear infinite;
        line-height: 1.2;
        margin-top: 15px;
        text-align: left;
    }

    .cursive-blink { font-family: 'Dancing Script', cursive; font-size: 95px; color: #ad1457; animation: blinker 3s linear infinite; margin-bottom: 0px; }
    .portal-text { color: #000000 !important; font-size: 38px; font-weight: 800; margin-top: 10px; }
    .year-text { color: #ad1457; font-size: 45px; font-weight: 900; letter-spacing: 2px; margin-bottom: 30px; }
    
    .head-img-container {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        padding-right: 20px;
    }
    
    .head-img {
        width: 180px;
        height: 180px;
        border-radius: 50%;
        border: 6px solid #ad1457;
        background-color: #FCE4EC; /* WARNA YANG DIMINTA */
        object-fit: cover;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }

    [data-testid="stSidebar"] { 
        background-color: #fce4ec !important; 
        border-right: 2px solid #f8bbd0; 
    }
    
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, div[role="radiogroup"] label p {
        color: #000000 !important; 
        font-weight: 800 !important; 
        font-size: 16px !important;
    }

    .card { border-radius: 20px; padding: 25px; text-align: center; color: #FFFFFF !important; font-weight: bold !important; height: 180px; display: flex; flex-direction: column; justify-content: center; margin-bottom: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
    .color-a { background: linear-gradient(135deg, #008B8B, #20B2AA); }
    .color-b { background: linear-gradient(135deg, #FF8C00, #FFA500); }
    .color-c { background: linear-gradient(135deg, #800080, #9370DB); }
    .color-d { background: linear-gradient(135deg, #2E8B57, #3CB371); }
    
    .stExpander { background-color: #AED6F1 !important; border-radius: 12px !important; }
    .stExpander details summary p { color: #008080 !important; font-weight: 900; font-size: 22px; font-style: italic; }
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

def get_link(nama_fail):
    link = data_links.get(nama_fail, "#")
    if "http" not in str(link): return "#"
    return link

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
    KP_IMAGE_URL = None
    # Logik imej Ketua Panitia kekal mengikut pilihan
    if pilihan == "REKA BENTUK DAN TEKNOLOGI": KP_IMAGE_URL = fix_drive_url("https://drive.google.com/file/d/11avGiH5w__vXztmo0sjltE46kYgCnNuN/view?usp=sharing")
    elif pilihan == "BAHASA MELAYU": KP_IMAGE_URL = fix_drive_url("https://drive.google.com/file/d/1dysRv55eRjKnGA3ACWUaJvfZXU6GMajL/view?usp=sharing")
    elif pilihan == "BAHASA INGGERIS": KP_IMAGE_URL = fix_drive_url("https://drive.google.com/file/d/1OSPkh5undB9H1PVTWNVPAzEk3DnFXuj2/view?usp=sharing")
    elif pilihan == "MATEMATIK": KP_IMAGE_URL = fix_drive_url("https://drive.google.com/file/d/1edxg1ICltkj3mLqYrpSsdlxl1ZbyP8nC/view?usp=sharing")
    elif pilihan == "SAINS": KP_IMAGE_URL = fix_drive_url("https://drive.google.com/file/d/1g8cmxSC8Ibcq2bTHaULHzi4lF_ovgQT_/view?usp=sharing")
    elif pilihan == "PENDIDIKAN ISLAM": KP_IMAGE_URL = fix_drive_url("https://drive.google.com/file/d/1ghBqi3co12tnWAaJtEpcD_1Spa7vdiUk/view?usp=sharing")
    elif pilihan == "SEJARAH": KP_IMAGE_URL = fix_drive_url("https://drive.google.com/file/d/1pFUbxnxTHe8mOMqYKjTanIT4mmHKIJlj/view?usp=sharing")
    elif pilihan == "PENDIDIKAN JASMANI DAN KESIHATAN": KP_IMAGE_URL = fix_drive_url("https://drive.google.com/file/d/1OMLU8ZlT2EPePvpetyorgE7j0XQNHhuH/view?usp=sharing")
    elif pilihan == "PENDIDIKAN SENI VISUAL": KP_IMAGE_URL = fix_drive_url("https://drive.google.com/file/d/13AiJ6tAqcCrljA3RKj8HcMeV2mjjMZZX/view?usp=sharing")
    elif pilihan == "PENDIDIKAN MUZIK": KP_IMAGE_URL = fix_drive_url("https://drive.google.com/file/d/1fXrKM-QEjA8CqFIEtnz9ESx88HzMBqpe/view?usp=sharing")
    elif pilihan == "BAHASA ARAB": KP_IMAGE_URL = fix_drive_url("https://drive.google.com/file/d/1z2JnCTdprivWuohsfIzvgo7WTvsmrRa5/view?usp=sharing")

    st.markdown(f'<div style="text-align:center; color:black; font-family:Pacifico; font-size:30px; margin-bottom:10px;">📂 Portal Fail Digital Pengurusan Panitia</div>', unsafe_allow_html=True)
    
    h_col1, h_col2 = st.columns([1.5, 3.5])
    with h_col1:
        if KP_IMAGE_URL:
            st.markdown(f'<div class="head-img-container"><img src="{KP_IMAGE_URL}" class="head-img"></div>', unsafe_allow_html=True)
    with h_col2:
        st.markdown(f'<div class="subject-title-blink">{pilihan}</div>', unsafe_allow_html=True)

    st.divider()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="card color-a"><div class="fail-title">🔵 FAIL A</div>MAKLUMAT PANITIA</div>', unsafe_allow_html=True)
        with st.expander("FAIL A 👇"):
            st.markdown(f'<a class="sublink" href="{get_link("Carta Organisasi Panitia")}" target="_blank">👤 Carta Organisasi</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{get_link("Biodata & Jadual Waktu Guru")}" target="_blank">📋 Biodata & Jadual Guru</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{get_link("Jadual Pemantauan & Pencerapan")}" target="_blank">📅 Jadual Pemantauan</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{get_link("Data Enrolmen Murid")}" target="_blank">👥 Data Enrolmen</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{get_link("Pengurusan Kewangan Panitia (PCG)")}" target="_blank">💰 Pengurusan Kewangan</a>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card color-b"><div class="fail-title">🟠 FAIL B</div>KURIKULUM</div>', unsafe_allow_html=True)
        with st.expander("FAIL B 👇"):
            st.markdown(f'<a class="sublink" href="{get_link("Minit Mesyuarat & Surat-Menyurat")}" target="_blank">📖 Minit Mesyuarat</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{get_link("Dokumen Standard Kurikulum (DSKP)")}" target="_blank">📜 DSKP</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{get_link("Manual & Modul PdPR")}" target="_blank">📘 Manual & Modul</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{get_link("Bahan Bantu Mengajar (BBM) & Rujukan")}" target="_blank">📦 BBM</a>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card color-c"><div class="fail-title">🟣 FAIL C</div>PERANCANGAN</div>', unsafe_allow_html=True)
        with st.expander("FAIL C 👇"):
            st.markdown(f'<a class="sublink" href="{get_link("Perancangan Pengajaran Tahunan & Harian")}" target="_blank">📅 RPT & RPH</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{get_link("Program Peningkatan Akademik")}" target="_blank">🏆 Peningkatan Akademik</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{get_link("Carta Gantt Perancangan")}" target="_blank">📊 Carta Gantt</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{get_link("Laporan Program Panitia")}" target="_blank">📝 Laporan Program</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{get_link("Program Perkembangan Staf (LDP/PLC)")}" target="_blank">🤝 LDP / PLC</a>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="card color-d"><div class="fail-title">🟢 FAIL D</div>PEPERIKSAAN</div>', unsafe_allow_html=True)
        with st.expander("FAIL D 👇"):
            st.markdown(f'<a class="sublink" href="{get_link("Pelaporan PBD & UASA")}" target="_blank">📊 Pelaporan PBD & UASA</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{get_link("Analisis Peperiksaan Awam")}" target="_blank">📈 Analisis Peperiksaan Awam</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{get_link("Jadual Peperiksaan & Penggubal Soalan")}" target="_blank">🕒 Jadual & Penggubal</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{get_link("Analisis Item & JSU")}" target="_blank">📑 Analisis Item & JSU</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{get_link("Bank Soalan & Skema Permarkahan")}" target="_blank">🏦 Bank Soalan</a>', unsafe_allow_html=True)

    st.divider()
    st.markdown(f'<p style="text-align: center; color: black; font-weight: bold;">Portal Panitia {pilihan} - SEK. KEB. TELOK BEREMBANG 2026</p>', unsafe_allow_html=True)
