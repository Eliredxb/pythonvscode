# create a file called animals.py
# ask for an example of different types of animals like bird, snake, cat, dog, fish and whale
# create a dictionary for this and also a table as well
import streamlit as st
import pandas as pd
name = st.text_input("What is your name: ")
dog = st.selectbox("What kind of dog do you want",["None","Puppy","Lion"])
cat = st.selectbox("What kind of cat do you want",["None","Kitten","Tiger"])
fish = st.selectbox("What kind of fish do you want",["None","Goldfish","Jelltfish"])
bird = st.selectbox("What kind of bird do you want",["None","Eagle","Peakcop"])

anaimalsdict ={"Name":[name],"Dog":[dog],'Cat':[cat],'Fish':[fish],'Bird':[bird]}
st.write(anaimalsdict)
anaimalstable = pd.DataFrame(anaimalsdict)
st.table(anaimalstable)
