import streamlit as st
st.set_page_config(layout="wide")
st.title("Welcome to Grace high schools voting exercise")
st.image("https://static.vecteezy.com/system/resources/thumbnails/007/343/251/small_2x/school-building-in-flat-style-modern-school-college-building-illustration-vector.jpg")
name = st.text_input("What is your name: ")
age = st.number_input("How old are you: ",1)

yl = 11 - age

if age < 11:
    st.success(f"You are not eligible to vote. You have {yl} year(s) left" )

else:
    st.success("you are eligible to vote")     