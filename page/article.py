import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize





df_article=pd.read_excel("data.xlsx", sheet_name='articles') #, sheet_name='Sheet1'

df_article["theme"] = df_article[["theme1", "theme2", "theme3", "theme4", "theme5", "theme6", "theme7", "theme8", "theme9", "theme10"]].apply(lambda x: ' , '.join(x.dropna().astype(str)), axis=1)

df_article["renvoi"] = df_article[["renvoi1", "theme2", "theme3", "theme4", "theme5", "theme6", "theme7", "theme8", "theme9", "renvoi10"]].apply(lambda x: ' , '.join(x.dropna().astype(str)), axis=1)


def Article():

    
    titre=st.sidebar.multiselect(
        "Nom de l'article",
        options=df_article["nom"].unique(),
        default=[],
    )
    
    signataire=st.sidebar.multiselect(
        "Signataire",  44
        options=df_article["signataire"].unique(),
        default=[],
    )
    encyclopedie=st.sidebar.multiselect(
        "Encyclopedie",
        options=df_article["encyclopedie"].unique(),
        default=[],
    )
    volume=st.sidebar.multiselect(
        "Volume",
        options=df_article["volume"].unique(),
        default=[],
    )
    theme=st.sidebar.multiselect(
        "Thème",
        options=df_article["theme1"].unique(),
        default=[],
    )
    renvoi=st.sidebar.multiselect(
        "Renvoi",
        options=df_article["renvoi1"].unique(),
        default=[],
    )

    col_math=st.sidebar.multiselect(
        "Nombre de colonne mathématique",
        options=df_article["nbr_colonnes_math"].unique(),
        default=[],
    )

    



    conditions = []

    if signataire:
        conditions.append(f"signataire==@signataire")
    if encyclopedie:
        conditions.append(f"encyclopedie==@encyclopedie")
    if volume:
        conditions.append(f"volume==@volume")
    if theme:
        conditions.append(f"theme==@theme" or "theme2==@theme"or "theme3==@theme" or "theme4==@theme" or "theme5==@theme" or "theme6==@theme")
    if renvoi:
        conditions.append(f"renvoi==@renvoi" or "renvoi2==@renvoi"or "renvoi3==@renvoi" or "renvoi4==@renvoi" or "renvoi5==@renvoi" or "renvoi6==@renvoi"or "renvoi7==@renvoi" or "renvoi8==@renvoi" or "renvoi9==@renvoi" or "renvoi10==@renvoi")
    if col_math:
        conditions.append(f"nbr_colonnes_math==@col_math")
    if titre:
        conditions.append(f"nom==@titre")
    

    # Utilisez la condition construite pour filtrer le DataFrame
    if conditions:
        query = " & ".join(conditions)
        df_selection = df_article.query(query)
    else:
        # Si rien n'est sélectionné, affichez tout le DataFrame
        df_selection = df_article

        



    if not df_selection.empty:

        total_nbr_lignes = df_selection.shape[0]
        encyclopedie_mode = df_selection['encyclopedie'].mode().iloc[0]
        nbr_colonnes_mean = float(df_selection['nbr_colonnes'].mean())
        theme = df_selection['theme1'].mode().iloc[0]


        total1,total2,total3,total4=st.columns(4,gap='large')
        with total1:
            st.info("Nombre d'article",icon="📌")
            st.metric(label="",value=f"{total_nbr_lignes:,.0f}")

        with total2:
            st.info('Encyclopédie la plus représentée', icon="📌")
            st.text(encyclopedie_mode)

        with total3:
            st.info('Nombre de colonne moyen',icon="📌")
            st.metric(label="",value=f"{nbr_colonnes_mean:,.0f}")

        
        with total4:
            st.info('Thème le plus présent',icon="📌")
            st.text(theme)

        st.markdown("""---""")


    
    if not df_selection.empty: 
        with st.expander("Filter par collonnes"):
            showData=st.multiselect('Filter: ',df_selection.columns,default=["encyclopedie","volume","nom","complement_nom","signataire","num_page_debut","num_page_fin","nbr_colonnes","theme","designant","renvoi", "commentaire"])
            
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
            help="Téléchargez le tableau au format CSV.",
            mime="text/csv"  # Spécifiez le type MIME du fichier
        )

        if not showData:
             st.warning("Sélectionnez au moins un champ à afficher.")

        

    else:
        st.warning("Aucun élément trouvé avec la sélection actuelle.")

    


    if not df_selection.empty:
        # Séparez les thèmes en une liste
        theme1_list = df_selection['theme1'].str.split(',').explode().str.strip()
        
        # Créez un DataFrame avec le décompte des thèmes
        theme_counts = theme1_list.value_counts().reset_index()
        theme_counts.columns = ['Thème', 'Nombre d\'articles']

        # Créez un graphique à barres pour représenter la proportion des thèmes en fonction du nombre d'articles
        fig = px.bar(theme_counts, x='Thème', y='Nombre d\'articles', title='Proportion des Thèmes en fonction du Nombre d\'Articles')

        # Personnalisez le graphique si nécessaire
        # fig.update_layout(barmode='group')

        # Affichez le graphique dans Streamlit
        st.plotly_chart(fig, use_container_width=True)


        if not df_selection.empty:
        # Calculez le nombre de pages par article
            if not df_selection["num_page_debut"].empty and not df_selection["num_page_fin"].empty:
                valid_pages = df_selection["num_page_fin"] >= df_selection["num_page_debut"]
                
                # Filtrer les lignes avec des pages valides
                df_valid_selection = df_selection[valid_pages]
                
                if not df_valid_selection.empty:
                    df_valid_selection['Nombre de pages'] = df_valid_selection['num_page_fin'] - df_valid_selection['num_page_debut']
                    
                    # Séparez les thèmes en une liste
                    theme1_list = df_valid_selection['theme1'].str.split(',').explode().str.strip()
                    
                    # Créez un DataFrame avec les thèmes et le nombre de pages pour chaque thème
                    theme_page_counts = df_valid_selection.groupby(theme1_list)['Nombre de pages'].mean().reset_index()
                    theme_page_counts.columns = ['Thème', 'Nombre de pages']

                    # Créez un graphique à barres pour représenter le nombre de pages en fonction du thème
                    fig = px.bar(theme_page_counts, x='Thème', y='Nombre de pages', title='Nombre de Pages par article en fonction du Thème')

                    # Personnalisez le graphique si nécessaire
                    # fig.update_layout(barmode='group')

                    # Affichez le graphique dans Streamlit
                    st.plotly_chart(fig, use_container_width=True)




