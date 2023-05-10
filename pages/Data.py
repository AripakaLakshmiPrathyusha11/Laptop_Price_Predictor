import streamlit as st
import os
import pandas as pd



# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))


# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)



# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

Data_Path = os.path.join(dir_of_interest,"laptop_details.csv")

df = pd.read_csv(Data_Path)

st.subheader("DataSets")
Data_Path = os.path.join(dir_of_interest,"laptop_price_prediction.csv")

df_1 = pd.read_csv(Data_Path)







tab1, tab2 = st.tabs(["Laptop Data", "Feature Extraction dataset"])

with tab1:
   st.header("Laptop Data")
   st.dataframe(df)


with tab2:
   st.header("Feature Extraction dataset")
   st.dataframe(df_1)





