import streamlit as st #helps us to create a page for are python app
import pandas as pd #helps us to read csvfiles create dataframe/tables
import plotly.express as px #helps us to plot charts in python

firsttable = pd.read_csv("studentsdata.csv")


menu = st.sidebar.selectbox("Menu",["Submit scores","Database/chart"])
if menu == "Database/chart":
 st.table(firsttable)
 subjects = ["Math","English","Computer","Art","Science"]
 subjectstable = firsttable[subjects].mean().reset_index()
 renamedtable = subjectstable.rename(columns ={'index':'Subject',0:"Average"})
  
 menu = st.sidebar.selectbox("Charts",["Choose","Barchart","Piechart"]) 
 if menu == "Barchart": 
   barchart = px.bar(renamedtable, x ="Subject" ,y ="Average")
   st.plotly_chart(barchart)
 if menu == "Piechart":
   piechart= px.pie(renamedtable, names = "Subject", values = "Average")
   st.plotly_chart(piechart)

if menu == "Submit scores":
 head1,head2,head3 = st.columns([0.5,3,0.5])
 with head2:
    st.subheader(":red[Amazing]:orange[Intern]:green[ational]:blue[School]")
 st.image("school.jpg")

 coli1,coli2 = st.columns(2)
 with coli1:
    name = st.text_input(":red[What is the students name]")
    math = st.number_input(":blue[What is the students maths score]",1)
    science = st.number_input(":red[What is the students science score]",1)
    computer = st.number_input(":blue[What is the students computer score]",1)


 with coli2:
    year = st.selectbox(":orange[What is the students year]",[1,2,3,4,5,6,7]) 
    english = st.number_input(":green[What is the students english score]",1)
    art = st.number_input(":orange[What is the students art score]",1)
    st.write("")
    st.write("")
    submit = st.button(":green[Submit students score]")
 
 total = math+english+art+science+computer

 average = total / 5
 if submit:
    if average >= 70:
      grade = "A"
      st.success(f"{name} Your total score is: {total} average is: {average} grade is: {grade}")
      st.balloons()
    elif average >= 60 and average < 70:
      grade = "C"
      st.info(f"{name} Your total score is: {total} average is: {average} grade is: {grade}")
      
    elif average >= 50 and average < 60:
      grade = "P"
      st.warning(f"{name} Your total score is: {total} average is: {average} grade is: {grade}")
      
    elif average < 50:
      grade = "F"
      st.error(f"{name} Your total score is: {total} average is: {average} grade is: {grade}")
    
    studentdict ={"Name":[name],"Year":[year],"Math":[math],"English":[english],"Computer":[computer],"Art":[art],"Science":[science],"Total":[total],"Average":[average],"Grade":[grade],}
    # st.write(studentdict)
    secondtable = pd.DataFrame(studentdict)
    # st.table(secondtable)
    tablesjoin = pd.concat([firsttable,secondtable],ignore_index=True)
    tablesjoin.to_csv("studentsdata.csv",index = False)  
