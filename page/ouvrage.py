import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize

df_ouvrage=pd.read_excel("data.xlsx", sheet_name='ouvrage') #, sheet_name='Sheet1'


df_ouvrage["theme"] = df_ouvrage[["theme1", "theme2", "theme3", "theme4", "theme5", "theme6", "theme7", "theme8", "theme9", "theme10"]].apply(lambda x: ' , '.join(x.dropna().astype(str)), axis=1)



def Ouvrage():

        
    titre=st.sidebar.multiselect(
        "Titre",
        options=df_ouvrage["titre"].unique(),
        default=[],
    )
    auteur=st.sidebar.multiselect(
        "Auteur/autrice",
        options=df_ouvrage["auteur_autrice1"].unique(),
        default=[],
    )
    annee_publi=st.sidebar.multiselect(
        "Année de publication",
        options=df_ouvrage["annee_publication"].unique(),
        default=[],
    )
    orga=st.sidebar.multiselect(
        "Organisme d'édition",
        options=df_ouvrage["organisme_edition"].unique(),
        default=[],
    )


    langue=st.sidebar.multiselect(
        "Langue",
        options=df_ouvrage["langue"].unique(),
        default=[],
    )

    lieu_publi=st.sidebar.multiselect(
        "Lieu de publication",
        options=df_ouvrage["lieu_publication"].unique(),
        default=[],
    )

    

    theme=st.sidebar.multiselect(
            "Thème",
            options=df_ouvrage["theme1"].unique(),
            default=[],
        )
 





    conditions = []

    if titre:
        conditions.append(f"titre==@titre")
    if auteur:
        conditions.append(f"auteur_autrice1==@auteur")
    if annee_publi:
        conditions.append(f"annee_publication==@annee_publi")
    if orga:
        conditions.append(f"organisme_edition==@orga")
    if lieu_publi:
        conditions.append(f"texte_presentation==@lieu_publi")
    if langue:
        conditions.append(f"langue==@langue")

    if theme:
        conditions.append(f"theme1==@theme")
    

    # Utilisez la condition construite pour filtrer le DataFrame
    if conditions:
        query = " & ".join(conditions)
        df_selection = df_ouvrage.query(query)
    else:
        # Si rien n'est sélectionné, affichez tout le DataFrame
        df_selection = df_ouvrage

        



    if not df_selection.empty:

        total_nbr_lignes = df_selection.shape[0]

        theme_principal = df_selection['theme1'].mode().iloc[0]

        if not df_selection['langue'].mode().empty:
            langue1 = df_selection['langue'].mode().iloc[0]

        else :
            langue1 = "Aucun thème n'a été entré"



        total1,total2,total3=st.columns(3,gap='large')
        with total1:
            st.info("Nombre d'ouvrage",icon="📌")
            st.metric(label="",value=f"{total_nbr_lignes:,.0f}")

        with total2:
            st.info('Langue la plus représenté', icon="📌")
            st.text(langue1)

        
        with total3:
                st.info('Thème le plus présent',icon="📌")
                st.text(theme_principal)
           
        
        

        st.markdown("""---""")


    if not df_selection.empty: 
        with st.expander("Filter par collonnes"):
            showData=st.multiselect('Filter: ',df_selection.columns,default=["titre","auteur_autrice1","auteur_autrice2","auteur_autrice3","auteur_autrice4","auteur_autrice5","auteur_autrice6","auteur_autrice7","auteur_autrice8","auteur_autrice9","auteur_autrice10","theme","organisme_edition","lieu_publication","annee_publication","langue","responsable_edition"])
            
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

