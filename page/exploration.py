import json
import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import Pie
from streamlit_echarts import st_pyecharts
from Query import count_articles_with_attributes
from ressources.graph_and_plot.pie import pie
from ressources.graph_and_plot.bar_label import bar_label
from ressources.graph_and_plot.pie_personne import display_most_cited_people_chart
from ressources.graph_and_plot.network import render_article_sankey

import uuid

# Générer une clé unique
unique_key = str(uuid.uuid4())



def Exploration(selected_plot=None):
    # Définir les options de tracé disponibles
    plot_options = ["Renvois en fonction de la cible", "Renvois en fonction des encyclopédie", "Personnes citées en fonction des encyclopédie", "Reseau des renvois"]  # Ajoutez d'autres options au besoin
    
    # Sélectionner le type de tracé à afficher à partir de la liste déroulante
    selected_plot = st.sidebar.selectbox("Sélectionner le graphe souhaité", plot_options, key=unique_key)
    
    # Afficher le graphique approprié en fonction de la sélection
    if selected_plot == "Renvois en fonction de la cible":
        pie()
    elif selected_plot == "Renvois en fonction des encyclopédie":
        bar_label()
        
    elif selected_plot == "Personnes citées en fonction des encyclopédie":
        display_most_cited_people_chart()
    
    elif selected_plot == "Reseau des renvois":
        render_article_sankey()



# Appel de la fonction pour afficher le graphique
