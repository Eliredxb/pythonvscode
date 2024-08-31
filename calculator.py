"""
Create a an Arithmetic Calculator that performs addition, subtraction, division and multiplication operation between two numbers.

Ensure to add an image if you wish and also make use of buttons ‘+’, ‘-‘, ‘/‘, and ‘*’.
"""
import streamlit as st
st.set_page_config(layout ="wide")
st.image("https://cdn.pixabay.com/photo/2013/07/28/14/07/calculator-168360_960_720.jpg",width=200)
n1 = st.number_input("Enter a first number: ",1)
n2 = st.number_input("Enter a second number: ",1)
ad,sub,mult,div,aoftc = st.columns(5)
with ad:
    if st.button("_+_"):
        ad = n1+n2
        st.success(f"{ad}")

with sub:
    if st.button("_-_"):
        sub = n1-n2
        st.success(f"{sub}")

with mult:
    if st.button("_*_"):
        mult = n1*n2
        st.success(f"{mult}")

with div:
    if st.button("_/_"):
        div = n1/n2
        st.success(f"{div}")

with aoftc:
    if st.button("_+-*/_"):
        add = n1+n2
        sub = n1-n2
        mult = n1*n2
        div = n1/n2
        st.success(f"{add}__{sub}__{mult}__{div}")
