import streamlit as st

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Portal Panitia SKTB", layout="wide")

# LINK GAMBAR ASAL
LOGO_URL = "https://lh3.googleusercontent.com/d/1XV1CIEWhms8jHqJGOKpSluqr7cxtSWrv"
PENTADBIR_URL = "https://lh3.googleusercontent.com/d/1m87eH4bQ-p51DCMVjvM2ID8QgtwNF9ul"

# --- FUNGSI FIX LINK GOOGLE DRIVE ---
def fix_drive_url(url):
    if "drive.google.com" in url:
        try:
            if "/file/d/" in url:
                file_id = url.split("/file/d/")[1].split("/")[0]
            elif "id=" in url:
                file_id = url.split("id=")[1].split("&")[0]
            else:
                return url
            return f"https://drive.google.com/uc?export=view&id={file_id}"
        except:
            return url
    return url

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
    
    .stApp { background: linear-gradient(135deg, #fff5f7 0%, #fce4ec 100%); background-attachment: fixed; }
    
    @keyframes blinker { 0% { opacity: 1; } 50% { opacity: 0.2; } 100% { opacity: 1; } }

    .subject-title-blink {
        color: #ad1457;
        font-size: 50px;
        font-weight: 900;
        animation: blinker 3s linear infinite;
        line-height: 1.2;
        margin-top: 25px;
        text-align: left;
    }

    /* GAYA GAMBAR KETUA PANITIA - PENUH BULATAN */
    .head-img-container {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        padding-right: 20px;
    }
    
    .head-img {
        width: 170px;
        height: 170px;
        border-radius: 50%;
        border: 6px solid #ad1457;
        object-fit: cover; /* Memastikan gambar memenuhi ruang bulatan */
        object-position: center;
        display: block;
        padding: 0px !important;
        margin: 0px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }

    /* SIDEBAR STYLE */
    [data-testid="stSidebar"] { background-color: #fce4ec !important; border-right: 2px solid #f8bbd0; }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, div[role="radiogroup"] label p {
        color: #000000 !important; font-weight: 800 !important; font-size: 18px !important;
    }

    /* KAD FAIL */
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
        <div style="text-align:center;">
            <img src="{LOGO_URL}" width="220">
            <h1 style="font-family:'Dancing Script'; font-size:95px; color:#ad1457;">Selamat Datang</h1>
            <h2 style="font-weight:800; font-size:38px;">PORTAL FAIL DIGITAL PENGURUSAN PANITIA</h2>
            <h2 style="color:#ad1457; font-weight:900; font-size:45px;">SEK. KEB. TELOK BEREMBANG 2026</h2>
            <img src="{PENTADBIR_URL}" style="width:100%; max-width:1000px; border-radius:15px; border:5px solid white; box-shadow:0 10px 30px rgba(0,0,0,0.15);">
        </div>
    """, unsafe_allow_html=True)

# --- 4. LAMAN PANITIA ---
else:
    links = {k: "#" for k in ["Carta", "Biodata", "Jadual_M", "Enrolmen", "Kewangan", "Minit", "DSKP", "Manual", "BBM", "RPT", "Akademik", "Gantt", "Laporan", "PLC", "PBD", "Analisis", "Jadual_E", "JSU", "Bank"]}
    KP_IMAGE_URL = None

    if pilihan == "REKA BENTUK DAN TEKNOLOGI":
        # LINK TERBARU YANG ANDA BERIKAN
        raw_url = "https://drive.google.com/file/d/1MNlOa_SPMZjKbXPugpswaf6DuzHncMrj/view?usp=drive_link"
        KP_IMAGE_URL = fix_drive_url(raw_url)
        
        links.update({
            "Carta": "https://docs.google.com/presentation/d/1b76mhH6fqiZSt48ARdrNyJulunexr_u7PZj4AFoq_Gc/edit?usp=sharing",
            "Biodata": "https://docs.google.com/presentation/d/18h4II0zdKX5IEZXhMRlxr89j-4CZdhRLuKdqrcR1118/edit?usp=drive_link",
            "Jadual_M": "https://docs.google.com/presentation/d/1vx4yASQI69Dw3WgLbHdLLIi6y6Uvwqx_cPR7jDpnEf4/edit?usp=sharing",
            "Enrolmen": "https://docs.google.com/spreadsheets/d/1lQLHlLLklHhZpKaVTs0D5C7PGaJOvo9g/edit?usp=drive_link",
            "Kewangan": "https://docs.google.com/spreadsheets/d/1DdzyEc8c0OnEY6KN9LPWsYkpdNJcBDr7oZzLLo1_9mc/edit?usp=sharing",
            "Minit": "https://drive.google.com/drive/folders/1KfhRHblLKPyn9VFLq0bwBEgeVPq_9PLP?usp=sharing",
            "DSKP": "https://drive.google.com/drive/folders/15v24g0l9KulIq14F6pwwn-I1naMaO-0S?usp=sharing",
            "Manual": "https://drive.google.com/drive/folders/1__aMuk0rjNRJIPgUAHhBgCYmNRpOuInJ?usp=sharing",
            "BBM": "https://drive.google.com/drive/folders/1AsgXDpVbDMTBOEknbRn-70czAZVUXHVJ?usp=sharing",
            "RPT": "https://drive.google.com/drive/folders/13ONhdCcHDgjo-pMYoMtyQUKqQc3XFGGh?usp=drive_link",
            "Akademik": "https://docs.google.com/presentation/d/1W_pVK4kuv4XHzJrm8Vi6IPjnqhfo7xXSVUo7n54Vflc/edit?usp=sharing",
            "Gantt": "https://drive.google.com/file/d/1POSqk4gZVQ3JuFhwSHmiZBezOGK0tiRr/view?usp=sharing",
            "Laporan": "https://drive.google.com/drive/folders/1VidiLz-pZ3WJj29p13BrVXFHly6IShKc?usp=drive_link",
            "PLC": "https://drive.google.com/drive/folders/1NwX9c5l7SDRPNVa3UKzz1LX1s-Ic3Ghc?usp=sharing",
            "PBD": "https://drive.google.com/drive/folders/1sUR2Sq6fWbZk1gGveuRX935pqWkmUIgx?usp=sharing",
            "Analisis": "https://drive.google.com/drive/folders/1aJspYVKRdzMMpNsYtRA1SjEOKSeWoka8?usp=drive_link",
            "Jadual_E": "https://drive.google.com/drive/folders/17doEPe67XPYLNcSqS-d-aGtCXjMddiDj?usp=sharing",
            "JSU": "https://drive.google.com/drive/folders/17swAo8ZjS9HPE1N1xNTyi9Lfw2LRzc15?usp=sharing",
            "Bank": "https://drive.google.com/drive/folders/17-cMG1Orr1Q5oxbUBzKShiDSuMDyv8gH?usp=sharing"
        })

    st.markdown(f'<div style="text-align:center; font-family:Pacifico; font-size:30px; margin-bottom:10px;">📂 Portal Fail Digital Pengurusan Panitia</div>', unsafe_allow_html=True)
    
    # SUSUNAN GAMBAR KETUA DAN TAJUK
    h_col1, h_col2 = st.columns([1.5, 3.5])
    with h_col1:
        if KP_IMAGE_URL:
            st.markdown(f'<div class="head-img-container"><img src="{KP_IMAGE_URL}" class="head-img"></div>', unsafe_allow_html=True)
    with h_col2:
        st.markdown(f'<div class="subject-title-blink">{pilihan}</div>', unsafe_allow_html=True)

    st.divider()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="card color-a">🔵 FAIL A<br>MAKLUMAT PANITIA</div>', unsafe_allow_html=True)
        with st.expander("FAIL A 👇"):
            st.markdown(f'<a class="sublink" href="{links["Carta"]}" target="_blank">👤 Carta Organisasi</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Biodata"]}" target="_blank">📋 Biodata & Jadual Guru</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Jadual_M"]}" target="_blank">📅 Jadual Pemantauan</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Enrolmen"]}" target="_blank">👥 Data Enrolmen</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Kewangan"]}" target="_blank">💰 Pengurusan Kewangan</a>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card color-b">🟠 FAIL B<br>KURIKULUM</div>', unsafe_allow_html=True)
        with st.expander("FAIL B 👇"):
            st.markdown(f'<a class="sublink" href="{links["Minit"]}" target="_blank">📖 Minit Mesyuarat</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["DSKP"]}" target="_blank">📜 DSKP</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Manual"]}" target="_blank">📘 Manual & Modul</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["BBM"]}" target="_blank">📦 BBM</a>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card color-c">🟣 FAIL C<br>PERANCANGAN</div>', unsafe_allow_html=True)
        with st.expander("FAIL C 👇"):
            st.markdown(f'<a class="sublink" href="{links["RPT"]}" target="_blank">📅 RPT & RPH</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Akademik"]}" target="_blank">🏆 Peningkatan Akademik</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Gantt"]}" target="_blank">📊 Carta Gantt</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Laporan"]}" target="_blank">📝 Laporan Program</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["PLC"]}" target="_blank">🤝 LDP / PLC</a>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="card color-d">🟢 FAIL D<br>PEPERIKSAAN</div>', unsafe_allow_html=True)
        with st.expander("FAIL D 👇"):
            st.markdown(f'<a class="sublink" href="{links["PBD"]}" target="_blank">📊 Pelaporan PBD & UASA</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Analisis"]}" target="_blank">📈 Analisis Peperiksaan Awam</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Jadual_E"]}" target="_blank">🕒 Jadual & Penggubal</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["JSU"]}" target="_blank">📑 Analisis Item & JSU</a>', unsafe_allow_html=True)
            st.markdown(f'<a class="sublink" href="{links["Bank"]}" target="_blank">🏦 Bank Soalan</a>', unsafe_allow_html=True)

    st.divider()
    st.markdown(f'<p style="text-align: center; color: black; font-weight: bold;">Portal Panitia {pilihan} - SEK. KEB. TELOK BEREMBANG 2026</p>', unsafe_allow_html=True)
