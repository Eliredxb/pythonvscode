"""
---

📚 **Bookworm's Haven Activity** 📚

**1. Name:**
What is your name?


**3. Book Selection:**
Explore our library and choose your next read by selecting from the following options E.g:

Make sure you arrange your books in different categories:

Fiction
Non-Fiction
Mystery
Fantasy
Science Fiction
Etc

Books in checkboxes with images, names and prices

Please check the boxes next to the books you'd like to purchase.

**Total Amount:**
Based on your selections, the total amount will be calculated automatically.


Happy reading!

--- 
"""


import streamlit as st
total = 0
name = st.text_input("Whats is your name: ")
genre = st.radio("What is your genre",["NonFiction","Fiction","Mystery","Science Fiction","Bible stories"])



st.subheader("Fiction")
f1,f2,f3,f4 = st.columns(4) 
with f1:
    st.image("https://m.media-amazon.com/images/I/91jwRAg09EL._AC_UY327_FMwebp_QL65_.jpg")
    dino = st.checkbox("How to Catch a Dinosaur: $30")
    total += 30

with f2:
   st.image("https://m.media-amazon.com/images/I/91Xqo-RwhfL._AC_UY327_FMwebp_QL65_.jpg")
   plane = st.checkbox("8 little planets:  $30")
   total += 30
with f3:
   st.image("https://m.media-amazon.com/images/I/61GI6ossJJL._AC_UY327_FMwebp_QL65_.jpg")
   draw = st.checkbox("How to draw 101 things: $30")
   total += 30
with f4:
    st.image("https://m.media-amazon.com/images/I/71Aj3RpT9rL._AC_UY327_FMwebp_QL65_.jpg")
    aligp = st.checkbox("See you later alligator: $30")
    total += 30

st.subheader("Non fiction")
nf1,nf2,nf3,nf4 = st.columns(4)

with nf1:
    st.image("https://m.media-amazon.com/images/I/71vIWX6aiQL._AC_UY327_FMwebp_QL65_.jpg")
    anima =st.checkbox("The fascinating animal book: $40")
    total += 40

with nf2:
    st.image("https://m.media-amazon.com/images/I/71hJD5LzXuL._AC_UY327_FMwebp_QL65_.jpg")
    scie =st.checkbox("The fascinating science book: $40")
    total += 40

with nf3:
    st.image("https://m.media-amazon.com/images/I/715zH-ej1qL._AC_UY327_FMwebp_QL65_.jpg")
    engin =st.checkbox("The fascinating engeneering book:$40")
    total += 40

with nf4:
    st.image("https://m.media-amazon.com/images/I/81jgSrWjJBL._AC_UY327_FMwebp_QL65_.jpg")
    underw =st.checkbox("The fascinating ocean book:$40")
    total += 40

st.subheader("Mystery")
m1,m2,m3,m4 = st.columns(4)

with m1:
    st.image("https://m.media-amazon.com/images/I/71TWHQx2CVL._AC_UY327_FMwebp_QL65_.jpg")
    unk =st.checkbox("Hailey Haddie's Minute Mysteries: $40")
    total += 40

with m2:
    st.image("https://m.media-amazon.com/images/I/719ggCmK6CL._AC_UY327_FMwebp_QL65_.jpg")
    unk =st.checkbox("The Mystery of the Haunted House: $40")
    total += 40

with m3:
    st.image("https://m.media-amazon.com/images/I/71rrC4O0T6L._AC_UY327_FMwebp_QL65_.jpg")
    unk =st.checkbox("The Key House:$40")
    total += 40

with m4:
    st.image("https://m.media-amazon.com/images/I/711j60bSaGL._AC_UY327_FMwebp_QL65_.jpg")
    unk =st.checkbox("The Secret Lake :$40")
    total += 40

st.subheader("Science fiction")
s1,s2,s3,s4 = st.columns(4)

with s1:
    st.image("https://m.media-amazon.com/images/I/71TWHQx2CVL._AC_UY327_FMwebp_QL65_.jpg")
    unk =st.checkbox("Hailey Haddie's Minute Mysteries: $40")
    total += 40

with s2:
    st.image("https://m.media-amazon.com/images/I/719ggCmK6CL._AC_UY327_FMwebp_QL65_.jpg")
    unk =st.checkbox("The Mystery of the Haunted House: $40")
    total += 40

with s3:
    st.image("https://m.media-amazon.com/images/I/71rrC4O0T6L._AC_UY327_FMwebp_QL65_.jpg")
    unk =st.checkbox("The Key House:$40")
    total += 40

with s4:
    st.image("https://m.media-amazon.com/images/I/711j60bSaGL._AC_UY327_FMwebp_QL65_.jpg")
    unk =st.checkbox("The Secret Lake :$40")
    total += 40




if st.button("Show what i need to pay"):
    st.write(f"You have to pay ${total}")


