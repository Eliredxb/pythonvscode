"""
Prompt the user to input values for five different fields (e.g., name, age, city, occupation, and salary).
Store the user inputs in a dictionary.
Convert the dictionary to a pandas DataFrame.
Print the DataFrame.
"""
import streamlit as st 
import pandas as pd

firsttable = pd.read_csv("DF.csv")
st.table(firsttable)

name = st.text_input("Whats your name : ")
age = st.number_input("Whats your age : ",1)
city = st.text_input("Whats your city : ")
occupation = st.text_input("Whats your occupation : ")
salary = st.number_input("Whats your salary : ",1)

DFdict ={"Name":[name],"Age":[age],"City":[city],"Occupation":[occupation],"Salary":[salary]}
st.write(DFdict)
secondtable = pd.DataFrame(DFdict)
st.table(secondtable)
tablejoin = pd.concat([firsttable,secondtable],ignore_index=True)
tablejoin.to_csv('DF.csv',index =False)