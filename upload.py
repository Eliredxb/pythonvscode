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

if menu == "Upload audios":
    st.subheader("View Audios")
    uploadaudios = st.file_uploader("Upload your audios here",type =["mp3","wav"])
    st.audio(uploadaudios,format="audio/mp3")

if menu == "Upload videos":
    st.subheader("Play youtube video")
    youtubelink = st.text_input("Paste in your youtube link here")
    
    if st.button("Play youtube video"):
        st.video(youtubelink)
