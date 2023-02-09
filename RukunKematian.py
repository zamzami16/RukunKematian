"""
Requirements:
   pip install streamlit
   pip install streamlit-aggrid
"""

import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid
from datetime import datetime
import pytz

st.set_page_config(
    page_title="Rukun Kematian",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
        "Report a bug": "https://www.extremelycoolapp.com/bug",
        "About": "# This is a header. This is an *extremely* cool app!",
    },
)


st.write("# **KAS RUKUN KEMATIAN.**")

# excel_data = "https://docs.google.com/spreadsheets/d/1hdNOhGoTdkIVqioERIcdLlN3NgayhJtUEf-BDYScYsk/edit?usp=share_link";

url = "https://docs.google.com/spreadsheets/d/1hdNOhGoTdkIVqioERIcdLlN3NgayhJtUEf-BDYScYsk/edit#gid=1131523744"
url_1 = url.replace("/edit#gid=", "/export?format=csv&gid=")

df = pd.read_csv(url_1)

saldo = []
for i in range(len(df)):
    masuk = df.iloc[0 : i + 1]["Pemasukan"].sum()
    keluar = df.iloc[0 : i + 1]["Pengeluaran"].sum()
    saldo.append(masuk - keluar)

df["Saldo"] = saldo
# print(df.columns.tolist())
dff = df[["Tanggal", "Pemasukan", "Pengeluaran", "Saldo", "Keterangan"]]

# AgGrid
gb = GridOptionsBuilder.from_dataframe(dff)
gb.configure_auto_height()
gb.configure_column(
    "Tanggal",
    type=["customDateTimeFormat", "nonEditableColumn"],
    custom_format_string="yyyy-mm-dd",
)
gb.configure_column(
    "Pemasukan",
    type=["numericColumn", "customCurrencyFormat"],
    custom_currency_symbol="Rp",
)
gb.configure_column(
    "Pengeluaran",
    type=["numericColumn", "customCurrencyFormat"],
    custom_currency_symbol="Rp",
)
gb.configure_column(
    "Saldo",
    type=["numericColumn", "customCurrencyFormat"],
    custom_currency_symbol="Rp",
)

gridOptions = gb.build()

# st.write("### Streamlit AgGrid")
AgGrid(dff, gridOptions=gridOptions)

st.write(
    "### Saldo sekarang Tgl: {1} | Rp{0}".format(
        dff["Pemasukan"].sum() - dff["Pengeluaran"].sum(),
        datetime.now(pytz.timezone("Asia/Jakarta")).strftime("%d-%m-%Y")
    )
)

# st.write("Created with :purple_heart: by Zami16")
st.markdown(
    """<div style="text-align: center"> Created with &#128153; by Zami16 </div>""",
    unsafe_allow_html=True,
)
