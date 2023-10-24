import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
from page.encyclopedie import Encyclopedie
from page.ouvrage import Ouvrage
from page.personne import Personne
from page.article import Article

#from query import *
import time

st.set_page_config(page_title="Dashboard",page_icon="📰",layout="wide")
#st.subheader("Exploration des donnée PatriMaths")
st.markdown("##")

theme_plotly = None # None or streamlit

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

#fetch data
#result = view_all_data()

#side bar
st.sidebar.image("data/logo1.png",caption="Outils de visualisation des données")

#switcher
st.sidebar.header("Selectionez vos filtres")

def sideBar():

    selected2 = option_menu(None, ["Article", "Encyclopedie", "Ouvrage", 'Personne', 'Exploration'], 
    icons=['house', 'book', "list-task", 'neutal-face', 'map'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
    selected2
    if selected2=="Article":
    #st.subheader(f"Page: {selected}")
     Article()
    
    if selected2=="Encyclopedie":
    #st.subheader(f"Page: {selected}")
     Encyclopedie()

    if selected2=="Ouvrage":
    #st.subheader(f"Page: {selected}")
     Ouvrage()

    if selected2=="Personne":
    #st.subheader(f"Page: {selected}")
     Personne()

    if selected2=="Exploration":
    #st.subheader(f"Page: {selected}")
     Article()

sideBar()

#theme
hide_st_style=""" 

<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""



