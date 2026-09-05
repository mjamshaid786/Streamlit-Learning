import streamlit as st

st.header("LEARNING BUTTON")
st.subheader('1. Button Types')
l, m, r = st.columns(3)
if l.button('Primary Button', type='primary', width='stretch'):
    l.markdown('Hello Buddy')
if m.button('Secondary Button', type='secondary', width='stretch'):
    m.markdown('Hello Buddy')
if r.button('Tertiary Button', type='tertiary', width='stretch'):
    r.markdown(f'Good Work {':smile:'}')
#=========================================
#            BUTTON ICONS
#=========================================
st.subheader('2. Button Icons')

left, middle, right = st.columns(3)
if left.button('Plain Button', width='stretch'):
    left.markdown('Your clicked the Plain Button')
if middle.button('Emoji Button', icon="🦢", width='stretch'):
    middle.markdown(f'You clicked the Emoji Button {':smile:'}')
if right.button('Material Button', icon=":material/downloading:", width='stretch'):
    right.markdown('You clicked the material button')