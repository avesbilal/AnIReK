import base64
import json
import pathlib
import shutil
import requests as r
import time as t
from altair import ThetaValue
import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from bs4 import BeautifulSoup

st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed",
    page_title="AnIReK",
    page_icon=":robot_face:",
)

selected = option_menu(
    None, ["ReK", "About","Contact"],
    icons=['robot', 'info-circle','envelope-at'],
    default_index=0, 
    orientation="horizontal"
    )

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
    
    

if selected == "About":
    
    st.markdown("""
            <!--<h1 style="color: #F4447D;">Problem Statement</h1>-->
            
            :rainbow[Anime] :grey[is a form of hand-drawn or computer-generated animation originating from Japan.]
            <br>
            :grey[In terms of genres, there are more than] **34,211+** :grey[anime listed on] [myanimelist.net](https://myanimelist.net/anime.php)
            <br>
            <br>
            **The problem is the difficulty in finding anime that aligns with individual viewer preferences due to the vast number of options available.**
            :grey[**This leads to users spending excessive time searching instead of watching content.**]
            <br>
            <br>
            <!--## :violet[Audience]-->
            
             ##### :grey[An effective recommendation system is needed to predict and suggest anime based on user preferences. Therefore :green[**ReK**] helps us to find our next anime to watch with minimal wastage of time.]
             
             <br>
             
            <i style="text-align: left; color: #808495; font-size: 30px;">This is web app is designed for anime viewers who :</i>
            
            
            
            - Feel overwhelmed by the vast amount of anime available: :grey[with countless shows and movies to choose from, it can be difficult to know where to start. ReK helps you cut through the noise and discover hidden gems based on your preferences.]
            
            -  Want to avoid wasting time on anime they won't enjoy: :grey[ReK personalizes recommendations based on your watched anime increasing the chances you'll find similar.]
            -  Appreciate a streamlined and user-friendly experience: :grey[ReK's intuitive interface makes it easy to provide feedback and discover new recommendations with no Ads.]
            """, unsafe_allow_html=True)
        
if selected == "ReK":
    st.markdown("""
                # 🤖 :blue[Hello!]
                # :grey[My name is :green[ReK]]
                # :grey[I'm under development]
                """)
    st.progress(57)
    
    st.checkbox("Web App hosted", value=True,)
    st.checkbox("Model deployment", value=False)
    st.checkbox("Google analytics", value=True)
    st.checkbox("Analytics report", value=False)
    
if selected == "Contact":
    
        st.header(":email: GET IN TOUCH")

        contact_form = """
        <form action="https://formsubmit.co/avesbilal.school@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Name" required>
        <input type="email" name="email" placeholder="Email" required>
        <textarea name="message" placeholder="Message"></textarea>
        <br>
        <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)

        # Use Local CSS File
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
                
                local_css("style.css")
                
if selected == "Model":
    
    st.title('ML Model Progress')
    st.checkbox("Gathering Data", value=True)
    st.checkbox("Data Preparation", value=True)
    st.checkbox("Data Wrangling", value=True)
    st.checkbox("Analyse Data", value=True)
    st.checkbox("Model Training", value=False)
    st.checkbox("Model Testing", value=False)
    st.checkbox("Deployment", value=False)
    
    st.header('Sample Data')


    st.markdown("""
             ```
             dt.shape(4)
             ```
             """, unsafe_allow_html=True)
    dt = pd.read_csv('dataset/sample.csv')
    st.dataframe(dt)
    st.markdown('**Source:** https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset')