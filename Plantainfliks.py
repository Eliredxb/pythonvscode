"""
Create a Netflix Clone Application that allows user to register and login, then gives them access to menu so they can choose which genre of movie they want.

You can have as many genre as you desire..."gospel, animations, cartoons, fictions.." and the likes.
"""
import streamlit as st
import pandas as pd
movies_df = pd.read_csv("PF.csv")

st.sidebar.header("Login")

name = st.sidebar.text_input("Whats your name : ")
pasword = st.sidebar.text_input("Whats your password: ",type = "password")
login_button = st.sidebar.button("Login")  
if login_button:
      st.balloons()
      st.sidebar.success("You have logged in")
st.title("Movie")
genre =st.sidebar.selectbox("Select Genre", ["All"] + list(movies_df['Genre'].unique()))
filtered_df = movies_df if genre == "All" else movies_df[movies_df['Genre'] == genre]

num_columns = 3
columns = st.columns(num_columns)


for index, row in filtered_df.iterrows():
  col = columns[index % num_columns]
  with col:
     if st.button(row['Title']):
        st.image(row['Image'],width = 450)
        st.subheader(row['Title'])
        st.write(f"**Genre:** {row['Genre']}")
        st.write(row['Description'])
        st.video(row['YouTube'])
        
          
        
       
        
              
        
        
# movietitle = st.text_input("Movie title: ")
# moviegenre = st.selectbox("Movie genre: ",["None","Fiction","Game"])
# moviedescription = st.text_input("Movie description")
# movieimage = st.text_input("Paste in your movie image link: ")
# movievideo = st.text_input("Paste in your youtube link")

# if st.button("Submit video"):
#     videodict = {"Title":[movietitle],"Genre":[moviegenre],"Description":[moviedescription],"Image":[movieimage],"YouTube":[movievideo]}
#     videodf = pd.DataFrame(videodict)
#     videojoin = pd.concat([movies_df,videodf],ignore_index=True)
#     videojoin.to_csv("PF.csv")

        