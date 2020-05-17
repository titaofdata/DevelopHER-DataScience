# -*- coding: utf-8 -*-
"""
Created on Sat May 16 20:17:17 2020

@author: Shanelle Recheta, Data Scientist
"""


# import packages
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# import streamlit
import streamlit as st
import joblib as jl


# Web app title
st.title('Sagana')
st.subheader("ML-based Food Distribution Web App")
# describe the web app
st.write("This app aims to use Open Data and Data Science to address problems in food security")
st.text("Sagana is currently trained on MRT, LRT, NHTS and BFT  dataset")


st.subheader("Watch the video that inspired the creation of Sagana")
st.video('https://www.youtube.com/watch?v=6RlxySFrkIM') 


st.write("View the Sagana Pitch Deck here: https://for-the-echo-dot.netlify.app/")    


st.title('Input the Brgy Code of your current location using the slider')
st.subheader('Sagana finds the optimal location to drop off your goods based on')
st.text('• Where there are most people in need') 
st.text('• The food terminal where there is currently least foot traffic') 
st.text('• Location that is within 2km of your input Brgy Code')

feat1 = st.slider('Brgy Code',100000000,168507009,148507009)


st.title('Food Terminal Locator')


@st.cache
def get_data():
    return pd.read_csv("ph.csv")
df = get_data()
st.header("Which is the best drop off for your goods?")
st.markdown("The following map shows where the food terminals can be found.")
option = st.selectbox('Which type of drop off works best for you?',['MRT Station','LRT Station','Brgy Food Terminal'])

'You selected: ', option

st.map(df,zoom=6)
st.text('Map coordinates imported from https://simplemaps.com/data/world-cities')


# read the data
data = pd.read_csv('cons.csv')

#display data
if st.checkbox('Show raw data'):
    st.subheader('Consolidated NHTS data')
    st.write(data)



st.markdown("## Party time!")
st.write("Thank you for taking part in the movement towards hunger free PH. Click below to celebrate.")
btn = st.button("Celebrate!")
if btn:
    st.balloons()
    
from PIL import Image
image = Image.open('poor_household_graph.png')
st.image(image, caption='This graph shows poor households per region based on data collected by NHTS. Rest assured that poor constituents are given priority in the food distribution',
          use_column_width=True)



st.markdown("**AUTHOR**")
st.markdown("Shane, Full Stack Data Scientist")


st.text("Hiring data scientists? Visit us at www.ftwfoundation.org")
