import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize



df_personne=pd.read_excel("data.xlsx", sheet_name='personne') #, sheet_name='Sheet1'


df_personne["prenom_nom"] = df_personne[["nom", "prenom"]].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)

df_personne["sexe"] = df_personne["sexe"].str.lower()


def Personne():

        
    nom=st.sidebar.multiselect(
        "Prenom et nom",
        options=df_personne["prenom_nom"].unique(),
        default=[],
    )
    sexe=st.sidebar.multiselect(
        "Sexe",
        options=df_personne["sexe"].unique(),
        default=[],
    )
    annee_nee=st.sidebar.multiselect(
        "Date de naissance",
        options=df_personne["date_naissance"].unique(),
        default=[],
    )
    lieu_nee=st.sidebar.multiselect(
        "Lieu de naissance",
        options=df_personne["lieu_naissance"].unique(),
        default=[],
    )

    annee_mort=st.sidebar.multiselect(
        "Date de mort",
        options=df_personne["date_mort"].unique(),
        default=[],
    )
    lieu_mort=st.sidebar.multiselect(
        "Lieu de mort",
        options=df_personne["lieu_mort"].unique(),
        default=[],
    )







    conditions = []

    if nom:
        conditions.append(f'prenom_nom== @nom')
    if sexe:
        conditions.append(f"sexe==@sexe")
    if annee_nee:
        conditions.append(f"date_naissance==@annee_nee")
    if lieu_nee:
        conditions.append(f"lieu_naissance==@lieu_nee")
    if annee_mort:
        conditions.append(f"date_mort==@annee_mort")
    if lieu_mort:
        conditions.append(f"lieu_mort==@lieu_mort")

    
    

    # Utilisez la condition construite pour filtrer le DataFrame
    if conditions:
        query = " & ".join(conditions)
        df_selection = df_personne.query(query)
    else:
        # Si rien n'est sélectionné, affichez tout le DataFrame
        df_selection = df_personne

        



    if not df_selection.empty:

        total_nbr_lignes = df_selection.shape[0]

        lieu_principal = df_selection['lieu_naissance'].mode().iloc[0]




        total1,total2=st.columns(2,gap='large')
        with total1:
            st.info("Nombre de personne",icon="📌")
            st.metric(label="",value=f"{total_nbr_lignes:,.0f}")



        with total2:
            st.info('Lieu de naissance le plus présent',icon="📌")
            st.text(lieu_principal)

        
        

        st.markdown("""---""")


    if not df_selection.empty: 
        with st.expander("Filter par collonnes"):
            showData=st.multiselect('Filter: ',df_selection.columns,default=["nom","prenom","sexe","date_naissance","lieu_naissance","date_mort","lieu_mort"])
            
        # Afficher le tableau
        st.dataframe(df_selection[showData], use_container_width=True)
        
        # Convertir le DataFrame en CSV avec encodage UTF-8
        csv_data = df_selection[showData].to_csv().encode('utf-8')
        
        # Ajouter un bouton de téléchargement en CSV
        st.download_button(
            label="Télécharger en CSV (UTF-8)",
            data=csv_data,
            key="download-csv",
            on_click=None,  # Laisser "None" pour le téléchargement immédiat
            help="Téléchargez le tableau au format CSV (UTF-8).",
            mime="text/csv"  # Spécifiez le type MIME du fichier
        )

        if not showData:
             st.warning("Sélectionnez au moins un champ à afficher.")

        

    else:
        st.warning("Aucun élément trouvé avec la sélection actuelle.")

    

#graphs

