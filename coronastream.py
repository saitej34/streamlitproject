import streamlit as st 
import json
import pandas as pd
import requests
import daily
import state
import time
st.title("Corona Virus Dashboard")
a=st.sidebar.radio("Types of Data : ",["Daily Corona cases Report Over World","Indian State Cases Details","Find Nearest Vaccination Center"])
if(a=="Daily Corona cases Report Over World"):
    st.write("Made by Using JohnHopkins University API")
    st.header("Corona cases Report Over World")
    year=st.number_input("Select the year",2020,2022)
    month=st.number_input("Select the Month Number: ",1,12)
    Date=st.number_input("selct the date: ",1,31)
    dt=str(("%d-0%d-0%d" %(year,month,Date)))
    st.write("Date Entered is " + dt)
    j,v = daily.getDetails(dt)
    st.write("Total number of confirmed cases are {}".format(j))
    st.write("Total Number of Deaths are {}".format(v))
    #st.write("Fatality rate is {}".format(y))
    Deathr=(v/j)*100
    st.write("Death rate of the day is {}".format(Deathr))
    st.success("Fetched successfully")
    
if(a=="Indian State Cases Details"):
    st.write("Fetching Data using RapidApi")
    st.header("State Wise Corona Details")
    #stc = pd.read_excel('gst-state-code-list-excel.xlsx')
    #st.dataframe(stc)
    cod = st.text_input("Enter the State code: ")
    l,a,b,c,d,e,f,g=state.getState(cod)
    st.info("Data Fetched Successfully")
    st.write("The Covid data of today")
    st.write("State name : {}".format(l))
    st.write("Total number of cases recorder today: {}".format(a))
    st.write("Total number of deaths recorded today: {}".format(b))
    st.write("Total number of recovered cases recorded today: {}".format(c))
    st.write("Total number of active today recorded today: {}".format(d))
    st.write("Total number of cases recorded till today: {}".format(e))
    st.write("Total number of cases recovered recorded till today: {}".format(f))
    st.write("Total number of deaths recorded till today: {}".format(g))
    deathr=(g/e)*100
    st.write("Death Rate is {}".format(deathr))
