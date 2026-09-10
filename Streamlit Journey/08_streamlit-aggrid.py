import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

df = pd.DataFrame({
    "Name": ["Ali", "Sara", "Ahmed"],
    "Role": ["Developer", "Designer", "Manager"],
    "Age": [25, 28, 32]
})

gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_pagination(paginationAutoPageSize=True)
gb.configure_selection('single') # Row select karne ke liye
gridOptions = gb.build()

st.subheader("Interactive AgGrid Table")
grid_response = AgGrid(df, gridOptions=gridOptions)