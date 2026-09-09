import streamlit as st

st.header("LEARNING CHECK BOX")

st.write("What would you like to order ?")
ice_cream = st.checkbox('Ice Cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if ice_cream:
    st.write(f'Thanks for ordering Ice Cream')
if coffee:
    st.write(f'Thanks for ordering Coffee')
if cola:
    st.write(f'Thanks for ordering Cola')