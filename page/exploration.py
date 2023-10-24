import streamlit as st
import pandas as pd

# Chargez les DataFrames
df_ouvrage=pd.read_excel("data.xlsx", sheet_name='ouvrage') #, sheet_name='Sheet1'
df_encyclopedie=pd.read_excel("data.xlsx", sheet_name='encyclopedie') #, sheet_name='Sheet1'
df_article=pd.read_excel("data.xlsx", sheet_name='articles') #, sheet_name='Sheet1'
df_personne=pd.read_excel("data.xlsx", sheet_name='personne') #, sheet_name='Sheet1'

df_revu=pd.read_excel("data.xlsx", sheet_name='revue') #, sheet_name='Sheet1'
df_revu_cite=pd.read_excel("data.xlsx", sheet_name='revue_cité') #, sheet_name='Sheet1'
df_personne_cite=pd.read_excel("data.xlsx", sheet_name='personne_cité') #, sheet_name='Sheet1'
df_ouvrage_cite=pd.read_excel("data.xlsx", sheet_name='ouvrage_cité') #, sheet_name='Sheet1'

# Fusionnez les DataFrames pour associer les informations
personne_cité_article = df_personne_cite.merge(df_article, left_on="id_article", right_on="id", how="left")
personne_cité_article = personne_cité_article.merge(df_personne, left_on="id_personne", right_on="id", how="left")

ouvrage_cite_article = df_ouvrage_cite.merge(df_article, left_on="id_article", right_on="id", how="left")
ouvrage_cite_article = ouvrage_cite_article.merge(df_ouvrage, left_on="id_ouvrage", right_on="id", how="left")
revu_cite_article = df_revu_cite.merge(df_article, left_on="id_article", right_on="id", how="left")
revu_cite_article = revu_cite_article.merge(df_revu, left_on="id_revue", right_on="id", how="left")
revu_cite_article = revu_cite_article.merge(df_personne, left_on="id_auteur_autrice", right_on="id", how="left", suffixes=("_revu", "_personne"))

df_article["renvoi"] = df_article[["renvoi1", "theme2", "theme3", "theme4", "theme5", "theme6", "theme7", "theme8", "theme9", "renvoi10"]].apply(lambda x: ' , '.join(x.dropna().astype(str)), axis=1)
df_article["theme"] = df_article[["theme1", "theme2", "theme3", "theme4", "theme5", "theme6", "theme7", "theme8", "theme9", "theme10"]].apply(lambda x: ' , '.join(x.dropna().astype(str)), axis=1)


def Exploration():
    
    
    article = st.sidebar.multiselect("Nom de l'article", options=df_article["nom"].unique(), default=[])
    encyclopedie = st.sidebar.multiselect("Titre", options=df_encyclopedie["titre"].unique(), default=[])
    ouvrage = st.sidebar.multiselect("Ouvrage cité", options=ouvrage_cite_article["titre"].unique(), default=[])
    revu = st.sidebar.multiselect("Nom de la revue citée", options=revu_cite_article["titre"].unique(), default=[])
    personne = st.sidebar.multiselect("Auteur / autrice", options=df_personne["nom_complet"].unique(), default=[])
    theme = st.sidebar.multiselect("Thème", options=df_article["theme1"].unique(), default=[])
    renvoie = st.sidebar.multiselect("Article renvoyé", options=df_article["renvoi"].unique(), default=[])
    personne_cite = st.sidebar.multiselect("Auteur / autrice cité", options=personne_cité_article["nom_complet"].unique(), default=[])

    conditions = []

    if article:
        conditions.append(personne_cité_article["nom"].isin(article))
    if ouvrage:
        conditions.append(ouvrage_cite_article["titre"].isin(ouvrage))
    if revu:
        conditions.append(revu_cite_article["titre"].isin(revu))
    if personne:
        conditions.append(personne_cité_article["nom_complet"].isin(personne))
    if theme:
        conditions.append(personne_cité_article["theme1"].isin(theme))
    if renvoie:
        conditions.append(personne_cité_article["renvoi"].isin(renvoie))
    if personne_cite:
        conditions.append(personne_cité_article["nom_complet"].isin(personne_cite))

    if conditions:
        filtered_df = personne_cité_article[conditions[0]]
        for condition in conditions[1:]:
            filtered_df = filtered_df[condition]
    else:
        filtered_df = personne_cité_article

    





    if not filtered_df.empty: 
        with st.expander("Filter par collonnes"):
            showData=st.multiselect('Filter: ',filtered_df.columns,default=["encyclopedie","volume","nom","theme","signataire","renvoi","titre_complet","auteur_autrice1","annee_publication","theme1","auteur_autrice10","nom_complet","titre"])
            
        # Afficher le tableau
        st.dataframe(filtered_df[showData], use_container_width=True)
        

# Appel de la fonction Exploration pour l'affichage des résultats
Exploration()
