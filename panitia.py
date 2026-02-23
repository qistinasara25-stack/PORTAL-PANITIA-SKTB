import streamlit as st

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Portal Panitia SKTB", layout="wide")

# LINK GAMBAR ASAL (LOGO & PENTADBIR)
LOGO_URL = "https://lh3.googleusercontent.com/d/1XV1CIEWhms8jHqJGOKpSluqr7cxtSWrv"
PENTADBIR_URL = "https://lh3.googleusercontent.com/d/1m87eH4bQ-p51DCMVjvM2ID8QgtwNF9ul"

# --- FUNGSI FIX LINK GOOGLE DRIVE (PENTING!) ---
def fix_drive_url(url):
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

# --- CUSTOM CSS ---
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
        background-color: #fce4ec; 
        object-fit: cover;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }

    /* SIDEBAR STYLE & HOVER EFFECT */
    [data-testid="stSidebar"] { 
        background-color: #fce4ec !important; 
        border-right: 2px solid #f8bbd0; 
    }
    
    /* Gaya teks asal di sidebar */
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, div[role="radiogroup"] label p {
        color: #000000 !important; 
        font-weight: 800 !important; 
        font-size: 16px !important;
        transition: all 0.3s ease; /* Kesan transisi yang lembut */
    }

    /* KESAN HOVER PADA NAMA SUBJEK */
    div[role="radiogroup"] label {
        padding: 10px !important;
        border-radius: 10px !important;
        margin-bottom: 5px !important;
        transition: all 0.3s ease !important;
    }

    div[role="radiogroup"] label:hover {
        background-color: #f8bbd0 !important; /* Warna pink bila hover */
        transform: translateX(10px); /* Gerak ke kanan sedikit */
        cursor: pointer;
    }

    div[role="radiogroup"] label:hover p {
        color: #ad1457 !important; /* Warna teks tukar merah gelap */
        font-weight: 900 !important;
        font-size: 17px !important;
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
    links = {k: "#" for k in ["Carta", "Biodata", "Jadual_M", "Enrolmen", "Kewangan", "Minit", "DSKP", "Manual", "BBM", "RPT", "Akademik", "Gantt", "Laporan", "PLC", "PBD", "Analisis", "Jadual_E", "JSU", "Bank"]}
    KP_IMAGE_URL = None

    if pilihan == "REKA BENTUK DAN TEKNOLOGI":
        raw_url_rbt = "https://drive.google.com/file/d/11avGiH5w__vXztmo0sjltE46kYgCnNuN/view?usp=sharing"
        KP_IMAGE_URL = fix_drive_url(raw_url_rbt)
    elif pilihan == "BAHASA MELAYU":
        raw_url_bm = "https://drive.google.com/file/d/1dysRv55eRjKnGA3ACWUaJvfZXU6GMajL/view?usp=sharing"
        KP_IMAGE_URL = fix_drive_url(raw_url_bm)
    elif pilihan == "BAHASA INGGERIS":
        raw_url_bi = "https://drive.google.com/file/d/1OSPkh5undB9H1PVTWNVPAzEk3DnFXuj2/view?usp=sharing"
        KP_IMAGE_URL = fix_drive_url(raw_url_bi)
    elif pilihan == "MATEMATIK":
        raw_url_mt = "https://drive.google.com/file/d/1edxg1ICltkj3mLqYrpSsdlxl1ZbyP8nC/view?usp=sharing"
        KP_IMAGE_URL = fix_drive_url(raw_url_mt)
    elif pilihan == "SAINS":
        raw_url_sn = "https://drive.google.com/file/d/1g8cmxSC8Ibcq2bTHaULHzi4lF_ovgQT_/view?usp=sharing"
        KP_IMAGE_URL = fix_drive_url(raw_url_sn)
    elif pilihan == "PENDIDIKAN ISLAM":
        raw_url_pi = "https://drive.google.com/file/d/1ghBqi3co12tnWAaJtEpcD_1Spa7vdiUk/view?usp=sharing"
        KP_IMAGE_URL = fix_drive_url(raw_url_pi)
    elif pilihan == "SEJARAH":
        raw_url_sj = "https://drive.google.com/file/d/1pFUbxnxTHe8mOMqYKjTanIT4mmHKIJlj/view?usp=sharing"
        KP_IMAGE_URL = fix_drive_url(raw_url_sj)
    elif pilihan == "PENDIDIKAN JASMANI DAN KESIHATAN":
        raw_url_pjk = "https://drive.google.com/file/d/1OMLU8ZlT2EPePvpetyorgE7j0XQNHhuH/view?usp=sharing"
        KP_IMAGE_URL = fix_drive_url(raw_url_pjk)
    elif pilihan == "PENDIDIKAN SENI VISUAL":
        raw_url_psv = "https://drive.google.com/file/d/13AiJ6tAqcCrljA3RKj8HcMeV2mjjMZZX/view?usp=sharing"
        KP_IMAGE_URL = fix_drive_url(raw_url_psv)
    elif pilihan == "PENDIDIKAN MUZIK":
        raw_url_muzik = "https://drive.google.com/file/d/1fXrKM-QEjA8CqFIEtnz9ESx88HzMBqpe/view?usp=sharing"
        KP_IMAGE_URL = fix_drive_url(raw_url_muzik)
    elif pilihan == "BAHASA ARAB":
        raw_url_ba = "https://drive.google.com/file/d/1z2JnCTdprivWuohsfIzvgo7WTvsmrRa5/view?usp=sharing"
        KP_IMAGE_URL = fix_drive_url(raw_url_ba)

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
            st.markdown(f'<a class="sublink" href="{links["Carta"]}" target="_blank">👤 Carta Organisasi</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Biodata"]}" target="_blank">📋 Biodata & Jadual Guru</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Jadual_M"]}" target="_blank">📅 Jadual Pemantauan</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Enrolmen"]}" target="_blank">👥 Data Enrolmen</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Kewangan"]}" target="_blank">💰 Pengurusan Kewangan</a>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card color-b"><div class="fail-title">🟠 FAIL B</div>KURIKULUM</div>', unsafe_allow_html=True)
        with st.expander("FAIL B 👇"):
            st.markdown(f'<a class="sublink" href="{links["Minit"]}" target="_blank">📖 Minit Mesyuarat</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["DSKP"]}" target="_blank">📜 DSKP</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Manual"]}" target="_blank">📘 Manual & Modul</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["BBM"]}" target="_blank">📦 BBM</a>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card color-c"><div class="fail-title">🟣 FAIL C</div>PERANCANGAN</div>', unsafe_allow_html=True)
        with st.expander("FAIL C 👇"):
            st.markdown(f'<a class="sublink" href="{links["RPT"]}" target="_blank">📅 RPT & RPH</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Akademik"]}" target="_blank">🏆 Peningkatan Akademik</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Gantt"]}" target="_blank">📊 Carta Gantt</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Laporan"]}" target="_blank">📝 Laporan Program</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["PLC"]}" target="_blank">🤝 LDP / PLC</a>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="card color-d"><div class="fail-title">🟢 FAIL D</div>PEPERIKSAAN</div>', unsafe_allow_html=True)
        with st.expander("FAIL D 👇"):
            st.markdown(f'<a class="sublink" href="{links["PBD"]}" target="_blank">📊 Pelaporan PBD & UASA</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Analisis"]}" target="_blank">📈 Analisis Peperiksaan Awam</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Jadual_E"]}" target="_blank">🕒 Jadual & Penggubal</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["JSU"]}" target="_blank">📑 Analisis Item & JSU</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Bank"]}" target="_blank">🏦 Bank Soalan</a>', unsafe_allow_html=True)

    st.divider()
    st.markdown(f'<p style="text-align: center; color: black; font-weight: bold;">Portal Panitia {pilihan} - SEK. KEB. TELOK BEREMBANG 2026</p>', unsafe_allow_html=True)
