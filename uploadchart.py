"""
Make an app that can upload a csv file, 
asks users to choose columns to plot (use multiselectbox), choose what type of chart to plot
then plot what the users selected"st.subheader("Upload csv and view database")
uploadcsv = st.file_uploader("Upload your csv file here",type = "csv")
"""
import streamlit as st
import pandas as pd
import plotly.express as px
st.subheader("Upload csv and view database")
uploadcsv = st.file_uploader("Upload your csv file here",type = "csv")

if uploadcsv:
    readcsv = pd.read_csv(uploadcsv)


    with st.expander("View csv table"):
        st.table(readcsv)
    columns = readcsv.select_dtypes(include='number').columns
    
    
    selectcolumns = st.multiselect("Choose columns to plot",columns)
    readcolumns = readcsv[selectcolumns].mean().reset_index()
    choosechart = st.radio("Choose chart to plot",["Choose","Barchart","Piechart"])
    if selectcolumns:
        if choosechart == "Barchart":
            
            barchart = px.bar(readcolumns,x= "index",y=0,labels={"index" : "subject","0":"Average"})
            st.plotly_chart(barchart)
      
        elif choosechart == "Piechart":
        
            piechart = px.pie(readcolumns,names="index",values =0,labels={"index":"suject","0":"Average"})
            st.plotly_chart(piechart)
            


























           
