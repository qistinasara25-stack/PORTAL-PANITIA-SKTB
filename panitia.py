import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(layout="wide", page_title="Dashboard RBT Live")

# 2. LINK CSV (Pastikan Link ni 'Published to Web' sebagai CSV)
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRu_niX3sDJqOr_JDETbN11kS7JAcyGAiNHQGBb8iqK-eHzlfRXfoPz4HFdlkfAhlAiSON6793kHsHQ/pub?output=csv"

@st.cache_data(ttl=10) # Bubu set 10 saat supaya tak berat sangat
def ambil_data():
    try:
        # Guna pandas terus baca URL CSV
        data = pd.read_csv(SHEET_URL)
        data.columns = [str(c).strip().replace(' ', '_').lower() for c in data.columns]
        return data
    except Exception as e:
        st.error(f"Alamak! Ada masalah nak panggil data: {e}")
        return None

# 3. GAYA VISUAL (Bubu tambah kesan Zoom lebih sikit!)
st.markdown("""
    <style>
    @keyframes blinker { 50% { opacity: 0; } }
    .sub-title-blink {
        text-align: center; color: #1a5276; font-size: 40px; font-weight: 900;
        animation: blinker 1.5s linear infinite; text-transform: uppercase;
        margin-bottom: 25px; text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .info-card {
        background-color: white; border-radius: 12px; padding: 15px; margin-bottom: 15px;
        display: flex; align-items: center; box-shadow: 3px 3px 12px rgba(0,0,0,0.1);
        border: 1px solid #eee; min-height: 100px; transition: 0.3s;
    }
    .info-card:hover { 
        transform: scale(1.1) rotate(1deg); /* Kesan Zoom & Senget Sikit */
        box-shadow: 5px 12px 25px rgba(0,0,0,0.2); 
        border: 1px solid #1a5276;
    }
    .kategori-header {
        background: linear-gradient(90deg, #1a5276, #2980b9); color: white; 
        padding: 12px; border-radius: 8px; margin: 20px 0 10px 0; 
        font-weight: bold; font-size: 20px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="sub-title-blink">PANITIA REKA BENTUK & TEKNOLOGI</div>', unsafe_allow_html=True)

df = ambil_data()

if df is not None:
    # Kategori ikut gambar Moon
    kategori_list = [
        ("📁 FAIL A: MAKLUMAT PANITIA", ["organisasi", "biodata", "pemantauan", "enrolmen", "kewangan"]),
        ("📖 FAIL B: KURIKULUM", ["mesyuarat", "standard", "pdpr", "bantu", "bbm"]),
        ("📊 FAIL C: PERANCANGAN", ["tahunan", "akademik", "gantt", "laporan", "staf", "ldp", "plc"]),
        ("📝 FAIL D: PEPERIKSAAN", ["pbd", "uasa", "peperiksaan", "jsu", "bank", "skema"])
    ]

    for tajuk_kat, keywords in kategori_list:
        pattern = '|'.join(keywords)
        # Filter data ikut keyword
        data_kat = df[df['nama_fail'].str.contains(pattern, case=False, na=False)]
        
        st.markdown(f'<div class="kategori-header">{tajuk_kat}</div>', unsafe_allow_html=True)
        
        # Guna Expander supaya tak serabut kalau fail banyak
        with st.expander(f"Klik untuk Lihat Senarai {tajuk_kat}", expanded=True):
            cols = st.columns(4)
            for index, (_, row) in enumerate(data_kat.iterrows()):
                nama = row['nama_fail']
                desc = row.get('deskripsi', 'Klik untuk buka fail')
                warna = row.get('warna', '#1a5276')
                ikon = row.get('ikon', '📄')
                link = str(row.get('link_drive', '#'))
                
                with cols[index % 4]:
                    st.markdown(f"""
                        <a href="{link}" target="_blank" style="text-decoration: none;">
                            <div class="info-card" style="border-left: 8px solid {warna};">
                                <div style="font-size:30px; flex:1; text-align:center;">{ikon}</div>
                                <div style="flex:3; padding-left:10px;">
                                    <div style="font-weight:bold; color:#333; font-size:13px;">{nama}</div>
                                    <div style="font-size:10px; color:#777;">{desc}</div>
                                </div>
                            </div>
                        </a>
                    """, unsafe_allow_html=True)
else:
    st.warning("⚠️ Data tak dapat dimuatkan. Pastikan Google Sheet anda telah 'Publish to Web' sebagai CSV.")
