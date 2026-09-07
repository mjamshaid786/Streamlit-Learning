import streamlit as st
from datetime import time, datetime
st.header("LEARNING SLIDER")
st.subheader("SLIDER")
#------------------- SLIDER -----------------------
age = st.slider("How old are you ?", 0, 130, 25)
st.write(f"I'm {age} years old.")

#------------------- RANGE SLIDER -----------------------
st.subheader("RANGE SLIDER")
values = st.slider("Select range of values", 1, 100, (25, 75))
st.write(f"Values: {values}")

#------------------- RANGE TIME SLIDER -----------------------
st.subheader("RANGE TIME SLIDER")
appointment = st.slider("Schedule your appointment time", value=(time(11, 30), time(12, 45)))
st.write(f"You are scheduled for : {appointment}")

#------------------- DATETIME SLIDER -----------------------
st.subheader("DATETIME SLIDER")
start_time = st.slider(
    "When do you start",
    value=datetime(2020, 1, 1, 9, 30),
    format="YY/MM/DD - hh:mm"
)
st.write(f"Start Time: {start_time}")


#------------------- COLORS SLIDER -----------------------
color = st.select_slider(
    "Select a color of the rainbow",
    options=[
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet",
    ],
)
st.write("My favorite color is", color)