"""
Write a Python program to recommend fun learning materials based on a child’s school grade.

 

Start by asking for the child’s name (or a nickname if they prefer).

Next, ask which grade they are in.

Then, inquire about their favorite subject: math or science.

If the child is in grades 4 to 6, suggest exciting study materials suitable for upper elementary school level.

If the child is in grades 1 to 3, recommend interactive study materials perfect for lower elementary school level.

If the child is in kindergarten, offer playful learning materials designed for early education.

Display the recommended materials with colorful illustrations to spark their interest!
"""
import streamlit as st
import pandas as pd 
name = st.text_input("Whats your name: ")
grade = st.selectbox("Whats your grade",["None","Kindergarten","Grade 1","Grade 2","Grade 3","Grade 4","Grade 5","Grade 6"])
subject = st.selectbox("Whats your favourite subject",["None","Math","Science"])
if grade == "Grade 4" or grade == "Grade 5" or grade == "Grade 6":
    st.write("I suggest exciting study materials")

elif grade == "Grade 1" or grade == "Grade 2" or grade == "Grade 3":
    st.write("I reccomend interactive study materials")

elif grade == "Kindergarten":
    st.write("I offer playful learning materials")

if subject == "Math":
    m1,m2,m3 = st.columns(3)
    with m1:
     st.write("Compass with pencil")
     st.image("https://i.ebayimg.com/images/g/WVcAAOSw2dBjNVKd/s-l1200.webp",width = 220)
    
    with m2:
     st.write("Ruler")
     st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQrlok7MiHqqLPTY1FRhpH79QgnMNLFiTpbnZAOh0aul2_HlehvrdNegm6khur-KYi84iw&usqp=CAU")
    
    with m3:
     st.write("Divider")
     st.image("https://5.imimg.com/data5/UR/DO/YO/SELLER-3992929/ceitix-divider.png",width = 220)

if subject == "Science":
    s1,s2,s3 = st.columns(3)
    with s1:
     st.write("Space")
     st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSE8rlBbqnDycGlg4HYo7CnnMOdSE7JA6ICkg&s")
    
    with s2:
     st.write("Artificial Inteligence")
     st.image("https://www.simplilearn.com/ice9/free_resources_article_thumb/Types_of_Artificial_Intelligence.jpg",width = 290)
    
    with s3:
     st.write("Aeroplane")
     st.image("https://i.pinimg.com/736x/b0/d5/97/b0d59733d5541b8ecbf628f84fbb863e.jpg",width = 290)