import streamlit as st
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie
import requests
from matplotlib import image
import os

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "laptop_prediction")

st.set_page_config(page_title ="Portfolio", page_icon=":tada:", layout="wide")
st.title(":red[_Portfolio_]")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ----Load Assets----
lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_wpugsrme.json")

# ----Header section----

st.subheader("A Data Scientist Intern in Innomatics Reaserch Labs")
st.write(
            "I'm well, decently acknowledged about analytics,passionate about vizualization and also exploring new technics everyday,learning them and improving my skills more better than yesterday ,in order to be best fit for Data science role.")
st.subheader("Skills")
st.write(
            """
            - Python
            - Mysql
            - Machine Learning
            - Tableau
            - PowerBI
            - Zoho CRM
            - Zoho Analytics
            - Microsoft Excel
            """
        )

with st.container():
    left_column, right_column = st.columns(2)
    with right_column:
        st.header("Experience")
        st.write('##')
        st.write(
            """ 
            I've completed graduation in BSC computer science and currently pursuing Data science course & gained knowledge  on analytics,vizualization,
            and implemented as a :red[Data Analyst intern at _Abhyaz MTAB technologies_].Now started a new position as :red[_Data scientist intern in Innomatics Research Labs_].
            - Worked as a Data Analyst and gained real world experience in making dashboards.
            - Letting people to know what are the insights of the company.
            - This allowed me to get a well-rounded understanding of the marketing industry and develop a range of skills. 
           """
        )
        st.write("[Experience Blog At Abhyaz > ](https://www.abhyaz.com/blogs/post/internship-experience-blog1)")

    with left_column:
        st_lottie(lottie_coding, height=500, key="Coding")

with st.container():
    with right_column:
        st.header("Follow for updates")
        st.write("[Github >](https://github.com/AripakaLakshmiPrathyusha11)")
        st.write("[LikedIn >](https://www.linkedin.com/in/a-lakshmi-prathyusha-a14a0025a/)")
