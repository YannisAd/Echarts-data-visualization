import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize

df_encyclopedie=pd.read_excel("data.xlsx", sheet_name='encyclopedie') #, sheet_name='Sheet1'

def Encyclopedie():

        
    titre=st.sidebar.multiselect(
        "Titre",
        options=df_encyclopedie["titre"].unique(),
        default=[],
    )
    volume=st.sidebar.multiselect(
        "Nombre de volume",
        options=df_encyclopedie["nbr_volumes"].unique(),
        default=[],
    )
    table_aut=st.sidebar.multiselect(
        "Présence d'une table d'auteurs/autrices",
        options=df_encyclopedie["table_auteurs_autrices"].unique(),
        default=[],
    )
    table=st.sidebar.multiselect(
        "Présence d'une table d'articles",
        options=df_encyclopedie["table_articles"].unique(),
        default=[],
    )
    text_pre=st.sidebar.multiselect(
        "Présence d'un texte de présentation",
        options=df_encyclopedie["texte_presentation"].unique(),
        default=[],
    )

    langue=st.sidebar.multiselect(
        "Langue",
        options=df_encyclopedie["langue"].unique(),
        default=[],
    )

    debut=st.sidebar.multiselect(
        "Date de début égale ou inferieur à",
        options=df_encyclopedie["annee_debut"].unique(),
        default=[],
    )


    fin=st.sidebar.multiselect(
            "Date de fin égale ou superieur à",
            options=df_encyclopedie["annee_fin"].unique(),
            default=[],
        )
    

    ville=st.sidebar.multiselect(
            "Ville d'édition",
            options=df_encyclopedie["ville_edition"].unique(),
            default=[],
        )
    
    pays=st.sidebar.multiselect(
            "Pays d'édition",
            options=df_encyclopedie["pays_edition"].unique(),
            default=[],
        )


    orga=st.sidebar.multiselect(
            "Organisme de financement",
            options=df_encyclopedie["organisme_financement"].unique(),
            default=[],
        )





    conditions = []

    if titre:
        conditions.append(f"titre==@titre")
    if volume:
        conditions.append(f"nbr_volumes==@volume")
    if table_aut:
        conditions.append(f"table_auteurs_autrices==@table_aut")
    if table:
        conditions.append(f"table_articles==@table")
    if text_pre:
        conditions.append(f"texte_presentation==@textpre")
    if langue:
        conditions.append(f"langue==@langue")

    if debut:
        conditions.append(f"annee_debut==@debut")
    if fin:
        conditions.append(f"annee_fin==@fin")
    if ville:
        conditions.append(f"ville_edition==@ville")


    if pays:
        conditions.append(f"pays_edition==@pays")
    if orga:
        conditions.append(f"organisme_financement==@orga")

    # Utilisez la condition construite pour filtrer le DataFrame
    if conditions:
        query = " & ".join(conditions)
        df_selection = df_encyclopedie.query(query)
    else:
        # Si rien n'est sélectionné, affichez tout le DataFrame
        df_selection = df_encyclopedie

        



    if not df_selection.empty:

        total_nbr_lignes = df_selection.shape[0]
        debut_moyen = float(df_selection['annee_debut'].mean())
        fin_moyen = float(df_selection['annee_debut'].mean())



        total1,total2,total3=st.columns(3,gap='large')
        with total1:
            st.info("Nombre d'encyclopedie",icon="📌")
            st.metric(label="",value=f"{total_nbr_lignes:,.0f}")

        with total2:
            st.info('Date de début moyenne', icon="📌")
            st.metric(label="",value=f"{debut_moyen:,.0f}")

        with total3:
            st.info('Date de fin moyenne',icon="📌")
            st.metric(label="",value=f"{fin_moyen:,.0f}")

        
        

        st.markdown("""---""")


    if not df_selection.empty: 
        with st.expander("Filter par collonnes"):
            showData=st.multiselect('Filter: ',df_selection.columns,default=["titre","sous_titre","nbr_colonnes","nbr_pages","nbr_volumes","table_articles","texte_presentation","num_edition","annee_debut", "annee_fin", "ville_edition", "pays_edition", "langue", "organisme_edition", "responsable_edition", "organisme_financement", "responsable_financement", "public_cible"])
            
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

