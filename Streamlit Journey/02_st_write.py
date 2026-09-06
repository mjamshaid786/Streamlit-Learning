import streamlit as st
import numpy as np
import altair as alt
import pandas as pd

st.header('Learning st.write Method ')

# ----------------- STRINGS -------------------
st.write('Hello, *World!* :sunglasses:')

# ----------------- NUMBERS -------------------
st.write(1234)

# ----------------- DATA FRAME -------------------
df = pd.DataFrame({
    'column_1' : [1, 2, 3, 4],
    'column_2' : [10, 20, 30 , 40],
    'column_3' : [11, 22, 33, 44]
})
st.write(df)
# st.write('Below is a dataframe:', df, 'Above is dataframe')
# ----------------- VISUALS -------------------
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)