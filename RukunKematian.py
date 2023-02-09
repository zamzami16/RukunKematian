"""
Requirements:
   pip install streamlit
   pip install streamlit-aggrid
"""

import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid

st.write("**KAS RUKUN KEMATIAN.**")

# excel_data = "https://docs.google.com/spreadsheets/d/1hdNOhGoTdkIVqioERIcdLlN3NgayhJtUEf-BDYScYsk/edit?usp=share_link";

url = "https://docs.google.com/spreadsheets/d/1hdNOhGoTdkIVqioERIcdLlN3NgayhJtUEf-BDYScYsk/edit#gid=1131523744"
url_1 = url.replace("/edit#gid=", "/export?format=csv&gid=")

df = pd.read_csv(url_1)
# print(df.columns.tolist())
dff = df[["Tanggal", "Pemasukan", "Pengeluaran", "Keterangan"]]

# AgGrid
gb = GridOptionsBuilder.from_dataframe(dff)
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

gridOptions = gb.build()

st.write("### Streamlit AgGrid")
AgGrid(dff, gridOptions=gridOptions, height=200)
