import streamlit as st
import pandas as pd
import os
import seaborn as sns

import matplotlib.pyplot as plt

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))


# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)



# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

Data_Path = os.path.join(dir_of_interest,"Laptop_price_prediction.csv")


df = pd.read_csv(Data_Path)

st.write("Countplot of RAM and OS:")

st.bar_chart(df["RAM"].value_counts())

st.bar_chart(df["OS"].value_counts())

st.write("Let's see how the MRP is varying with respect to features:")

fig = plt.figure(figsize=(10, 4))

sns.lineplot(data=df, x='OS', y='MRP')



st.pyplot(fig)

fig = plt.figure(figsize=(10, 4))

sns.lineplot(data=df, x='RAM', y='MRP')


st.pyplot(fig)


fig = plt.figure(figsize=(10, 4))

sns.lineplot(data=df, x='SSD', y='MRP')



st.pyplot(fig)
