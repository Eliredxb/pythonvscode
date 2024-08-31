"""
write a program for a use
-ask for the name and -age 
- ask for gender
-ask to choose best color 
-  ask best game
-use a type to ask to type best movie - use a type to ask best friend
create a submit button and show this
Jeida (F), your best game is: Minecraft, Color: Blue, Movie: Spiderman, Friend: Tofe
"""

import streamlit as st
friend= st.text_input("Whats the name of your friend freind: ")
age = st.number_input("How old is you friend : ",1)
gender = st.radio("What gender is your firend: ",["Boy","Girl"])
colour = st.selectbox("Whats your friend favorite colour: ",["Red","Orange","Yellow","Green","Blue","Purple","Pink"])
game = st.selectbox("Whats your friend favorite game: ",["Roblox","Minecraft",])    
movie = st.selectbox("Whats your friend favorite movie: ",["Sonic movie 1","Sonic movie 2","Mario movie"])
if st.button("Show who my friend is "):
    st.success(f"Your friend name is  {friend} your friend is {age} years old your friends gender is {gender} your friend favourite colour is {colour} your friend favourite game is {game} and your friend favourite movie is {movie}")
