import streamlit as st
import pandas as pd

menu = st.sidebar.selectbox("Choose an option",["Upload csv","Upload image","Upload audios","Upload videos"])
if menu == "Upload csv":
    st.subheader("Upload csv and view database")
    uploadcsv = st.file_uploader("Upload your csv file here",type = "csv")

    if uploadcsv:
        readcsv = pd.read_csv(uploadcsv)


        with st.expander("View csv table"):
            st.table(readcsv)

if menu == "Upload image":
    st.subheader("View image")
    uploadimage = st.file_uploader("Upload your images here ",type = ["jpg","png","jpeg","webp"])


    if uploadimage:
        st.image(uploadimage)






