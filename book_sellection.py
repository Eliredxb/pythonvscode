"""
**3. Book Selection:**

Make sure you arrange your books in different categories:

Children Books

Teenagers Books

Family Books

Christian Books

Science Books



Books in checkboxes with images, names and prices
**Total Amount:**
Based on your selections, the total amount will be calculated automatically.

Mr. tee: get purchased book and plot chart
"""

import streamlit as st
name = st.text_input("Whats is your name: ")
genre = st.radio("What is your genre",["Children","Teenage","Family","Science","Christians"],horizontal = True)

st.title("Children")
c1,c2,c3,c4 = st.columns(4)
with c1:
 st.image("https://m.media-amazon.com/images/I/A18OnuYW2dL._SY466_.jpg")

with c2:
 st.image("https://m.media-amazon.com/images/I/81mpSoJzv4L._AC_UL480_FMwebp_QL65_.jpg")

with c3:
 st.image("https://m.media-amazon.com/images/I/81iNCKsNLiL._AC_UL480_FMwebp_QL65_.jpg")   

with c4:
 st.image("https://m.media-amazon.com/images/I/71sMdsqsNXL._AC_UL480_FMwebp_QL65_.jpg")

st.title("Teenage")
t1,t2,t3,t4 = st.columns(4)
with t1:
    st.image("https://m.media-amazon.com/images/I/91FkwrxEvCL._AC_UL480_FMwebp_QL65_.jpg")

with t2:
    st.image("https://m.media-amazon.com/images/I/71RR-TIkbrL._AC_UL480_FMwebp_QL65_.jpg")

with t3:
    st.image("https://m.media-amazon.com/images/I/81vO5Hx00OL._AC_UL480_FMwebp_QL65_.jpg")

with t4:
    st.image("https://m.media-amazon.com/images/I/717YNvFoV-L._AC_UL480_FMwebp_QL65_.jpg")