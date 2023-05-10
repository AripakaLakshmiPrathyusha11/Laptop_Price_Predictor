import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os


FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

# import the model
Model_PATH = os.path.join(dir_of_interest,"prediction.pkl")
model = joblib.load(Model_PATH)

st.title("Laptop Price Predictor")

# Operating System 
OS = st.selectbox('Operating System',("Windows 10","Windows 11","Mac"))

# Processor
Processor = st.selectbox('Processor',("Intel Core i3","Intel Core i5","Intel Core i7","AMD","Other Intel"))

# Ram
RAM = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

# Display
Display = st.selectbox('Display(in Cm)',[29.46,33.02,33.78,34.04,34.29,35.56,35.81,36.07,39.62,40.64,40.89,41.15,42.16])

# RAM Type
RAM_Type = st.selectbox('Ram_Type',['DDR3','DDR4','DDR5'])

# Bit
Bit = st.selectbox('bit',[32,64])

#storage
ssd = st.selectbox('SSD(in GB|TB)',[0,1,128,256,512])

if st.button('Predict Price'):
    query = np.array([OS,Processor,Display,RAM,RAM_Type,Bit,ssd])

    query = query.reshape(1,7)
    st.write("Your Laptop Predicted Price is ₹"+str(int(model.predict(query))))
