#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      USER
#
# Created:     30/05/2023
# Copyright:   (c) USER 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import streamlit as st
from streamlit_option_menu import option_menu
import time
import progressbar

#with st.sidebar:
selected=option_menu(
menu_title="RESULTS ANALYTICS",options=["Home","About us","Results", "Login"],
menu_icon="cast",
orientation="horizontal",

  styles={
        "container": {"padding": "0!important", "background-color": "#bfbfa"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px",
        "--hover-color": "#ee"},
        "nav-link-selected": {"background-color": "green"},
    }


    )

if selected=="Home":
    st.title("Welcome to Hope Academy Results analysis System")

if selected=="About us":
    col1,col2,col3=st.columns([4,3,1])
    col1.markdown("# welcome")
    a=col2.camera_input("Take a photo")
    progressBar=col2.progress(0)
    for percent in range(100):
        time.sleep(0.5)
        progressBar.progress(percent+1)
    col2.success("photo uploaded successfully")

if selected=="Results":
    st.write(" Under developement")



if selected=="Login":
    st.write("Under Development")










