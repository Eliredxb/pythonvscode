"""
Question 1: CSV|Chart
July 24, 2024
Max is a football coach who wants to track the performance of his players over the season. He needs to collect data on various metrics like goals scored, assists, tackles, and passes for each player. This information will be saved to a CSV file and visualized using bar charts to identify areas of improvement and top performers.

Scenario:

Max’s tasks involve several steps:

Collect Player Performance Data:

Max needs to collect performance metrics for each player in his team.
Each player has metrics like goals scored, assists, tackles, and passes.
Save Data to CSV:

After collecting the data, Max will save this information to a CSV file named player_performance.csv.
Visualize Performance Data:

Max wants to create bar charts to visualize the average performance metrics for each player.
Let’s create a Python program to help Max with his tasks.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
firsttable = pd.read_csv("fzizball.csv")
radio = st.radio("Which one do you want to see",["Choose","Goals","Assists","Tackles","Passes"],horizontal = True)

if radio == "Goals":
    barchart = px.bar(firsttable, x = "Name",y = "Goals" )
    st.plotly_chart(barchart)

if radio == "Assists":
    barchart = px.bar(firsttable, x = "Name",y = "Assists")
    st.plotly_chart(barchart)

if radio == "Tackles":
    barchart = px.bar(firsttable, x = "Name",y = "Tackles")
    st.plotly_chart(barchart)

if radio == "Passes":
    barchart = px.bar(firsttable,x ="Name",y = "Passes")
    st.plotly_chart(barchart)

name = st.text_input("What is your name: ")
goals = st.number_input("How many goals did you score: ",0)
assists = st.number_input("How many assists did you need: ",0)
tackles = st.number_input("How many tackles did you do: ",0)
passes = st.number_input("How many passes did you do: ",0)

if st.button("Submit"):
 metricsdict = {"Name":[name],"Goals":[goals],"Assists":[assists],"Tactles":[tactles],"Passes":[passes]}
 secondtable = pd.DataFrame(metricsdict)
 tablesjoin = pd.concat([firsttable,secondtable],ignore_index=True)
 tablesjoin.to_csv("fzizball.csv",index = False)