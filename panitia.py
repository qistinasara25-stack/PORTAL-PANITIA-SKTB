import streamlit as st
import pandas as pd

# 1. Konfigurasi Halaman
st.set_page_config(layout="wide", page_title="Dashboard RBT Live")

# 2. LINK CSV CIKGU (Dah betul)
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRu_niX3sDJqOr_JDETbN11kS7JAcyGAiNHQGBb8iqK-eHzlfRXfoPz4HFdlkfAhlAiSON6793kHsHQ/pub?output=csv"

@st.cache_data(ttl=1)
def ambil_data():
    try:
        data = pd.read_csv(SHEET_URL)
        # Cuci nama kolum supaya tidak pening
        data.columns = [str(c).strip().replace(' ', '_').lower() for c in data.columns]
        return data
    except:
        return None

# 3. GAYA VISUAL
st.markdown("""
    <style>
    @keyframes blinker { 50% { opacity: 0; } }
    .sub-title-blink {
        text-align: center; color: #1a5276; font-size: 45px; font-weight: 900;
        animation: blinker 1.5s linear infinite; text-transform: uppercase;
        margin-bottom: 25px; text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .info-card {
        background-color: white; border-radius: 12px; padding: 18px; margin-bottom: 15px;
        display: flex; align-items: center; box-shadow: 3px 3px 12px rgba(0,0,0,0.1);
        border: 1px solid #eee; min-height: 125px; transition: 0.3s;
    }
    .info-card:hover { transform: scale(1.05); box-shadow: 5px 12px 25px rgba(0,0,0,0.15); }
    .kategori-header {
        background: #1a5276; color: white; padding: 10px; border-radius: 8px;
        margin: 25px 0 15px 0; font-weight: bold; font-size: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="sub-title-blink">PANITIA REKA BENTUK & TEKNOLOGI</div>', unsafe_allow_html=True)

df = ambil_data()

if df is not None:
    # Buang baris kosong
    df = df.dropna(subset=['nama_fail'])
    
    # KUMPULAN FAIL (Kod akan cari keyword secara automatik)
    kategori_list = [
        ("📁 FAIL A: MAKLUMAT", ["organisasi", "biodata", "pemantauan", "enrolmen", "kewangan"]),
        ("📖 FAIL B: KURIKULUM", ["mesyuarat", "standard", "pdpr", "bantu"]),
        ("📊 FAIL C: PERANCANGAN", ["tahunan", "akademik", "gantt", "laporan", "staf"]),
        ("📝 FAIL D: PEPERIKSAAN", ["pbd", "uasa", "peperiksaan"])
    ]

    for tajuk_kat, keywords in kategori_list:
        # Cari baris yang mengandungi mana-mana keyword di atas
        pattern = '|'.join(keywords)
        data_kat = df[df['nama_fail'].str.contains(pattern, case=False, na=False)]
        
        if not data_kat.empty:
            st.markdown(f'<div class="kategori-header">{tajuk_kat}</div>', unsafe_allow_html=True)
            cols = st.columns(4)
            for index, (_, row) in enumerate(data_kat.iterrows()):
                nama = row['nama_fail']
                desc = row.get('deskripsi', '')
                warna = row.get('warna', '#cccccc')
                ikon = row.get('ikon', '📁')
                link = str(row.get('link_drive', '#'))
                url = link if link.startswith('http') else "#"

                with cols[index % 4]:
                    st.markdown(f"""
                        <a href="{url}" target="_blank" style="text-decoration: none;">
                            <div class="info-card" style="border-left: 10px solid {warna};">
                                <div style="font-size:35px; flex:1; text-align:center;">{ikon}</div>
                                <div style="flex:4; padding-left:15px;">
                                    <div style="font-weight:bold; color:#333; font-size:14px;">{nama}</div>
                                    <div style="font-size:10px; color:#666; line-height:1.2;">{desc}</div>
                                </div>
                            </div>
                        </a>
                    """, unsafe_allow_html=True)
else:
    st.info("Bubu sedang panggil data... Klik 'Clear Cache' k cikgu!")
