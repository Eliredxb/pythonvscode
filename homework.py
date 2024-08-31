"""
#homework: create a simple church form that has a name (text), age range (selectbox) and gender (radio) on 3 columns
#then a text area to ask for other additional message
#create a login feature to let them in if they enter the correct password
"""
import streamlit as st
name = st.text_input("What is your name: ")
age = st.number_input("How old are you: ",1)
gender = st.radio("What gender are you",["Boy","Girl","Unkown"])
if st.button ("Show me what im part of"):
  if age  > 3 and age < 12:
         st.success("You are part of the Kids")
  if age  > 13 and age < 19:
         st.success("You are part of the Teens")
  if age  > 20 and age < 35:
         st.success("You are part of the Youth")
  if age  > 35 and age < 64:
         st.success("You are part of the Adults")
  if age > 64:
         st.success("You are part of the Elders")