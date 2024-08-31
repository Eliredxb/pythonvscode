"""
simple test
write a program for a use
-ask for the name and -age - use a radio to ask for gender
-use a selectbox to ask to choose best color - use a type to ask best game
-use a type to ask to type best movie - use a type to ask best friend
create a submit button and show this in a success bar
Jeida (F), your best game is: Minecraft, Color: Blue, Movie: Spiderman, Friend: Tofe
"""

import streamlit as st
name = st.text_input("What is your name: ")
age = st.number_input("How old are you: ",1)
gender = st.radio("What is your gender: ",["Boy","Girl"])
colour = st.selectbox("Whats your favorite colour: ",["Red","Orange","Yellow","Green","Blue","Purple","Pink","Brown","Black","Grey","White"])
movie = st.selectbox("Whats your favorite movie: ",["Sonic movie 1","Sonic movie 2","Mario movie"])
if st.button("Show who i am"):
    st.success(f"You are {name} you are {age} years old your gender is {gender} your favourite colour is {colour} and your favourite movie is {movie}")