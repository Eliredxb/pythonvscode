"""
#create a simple church age range database
#This will get the name, age, gender of the church memeber
#save this in a database and display on a new page (this page MUST have a login feature)
#Make sure you group members in differnt category based on their age 
# (Kids(3- 12), Teens(13-19), Youth(20-35), Adult(36-64), Elders(65+) )
"""
import streamlit as st
menu = st.sidebar.selectbox("menu",["Login","Church"])
if menu == "Church":
 name = st.text_input("What is your name: ")
 age = st.number_input("How old are you: ",1)
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

if menu == "Login":
 st.title("Welcome to login")
 lona = st.text_input("What is your name:  ")
 lopas = st.text_input("Type your password:  ",type = "password")