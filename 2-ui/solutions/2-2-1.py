# Challenge 2-2-1
import streamlit as st

if 'length' not in st.session_state:
    st.session_state.length = 0.0
if 'width' not in st.session_state:
    st.session_state.width = 0.0

st.title("Area and Perimeter")
length = st.number_input("Enter the length")
width = st.number_input("Enter the width")
btn_clicked = st.button("Calculate")
if btn_clicked:
    area = length * width
    perimeter = 2 * (length + width)
    st.write(f"Area: {area}")
    st.write(f"Perimeter: {perimeter}")
if btn_clear:
    st.session_state.length = 0.0
    st.session_state.width = 0.0
    st.rerun()