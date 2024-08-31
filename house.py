 #TEST 1
#write a python program for house buyers
#Ask them for their name
#ask them for their yearly salary
#If the earn between 100000-500000 they can buy a bungalow
#If the earn between >500000-1000000 they can buy a duplex
#If the earn between >1000000-5000000 they can buy a manshion

import streamlit as st
import pandas as pd
csvfile = pd.read_csv("house.csv")
st.table(csvfile)
name = st.text_input("What is your name:  ")
salary = st.number_input("What is your yearly salary",1)

if st.button("Show what i can buy"):
 if salary >= 100000 and salary < 500000:
    house = "bugalow"
    st.success("You can buy a bugalow")

 elif salary >= 500000 and salary < 1000000:
    house = "duplex"
    st.success("You can buy a duplex")

 elif salary >= 1000000:
    house = "mansion"
    st.success("You can buy a mansion")    
 elif salary < 100000:
    house = "None"
    st.error("Sorry you dont have enough to buy a house")
 housedict = {"name":[name],"salary":[salary],"house":[house]}
 st.write(housedict)

 housetable = pd.DataFrame(housedict)
 st.table(housetable)  
 jointables = pd.concat([csvfile,housetable],ignore_index=True)
 jointables.to_csv("house.csv",index = False)