import streamlit as st
import pandas as pd
import json

# Requête SPARQL pour récupérer tous les articles avec leurs informations

def Exploration():
    # Appel de la fonction query_sparql avec la requête All_Article_Query
    with open('./ressources/complete_article.json', "r") as f:
        results = json.load(f)

    # Accéder aux données JSON retournées
    bindings = results["results"]["bindings"]

    # Créer une liste pour chaque champ
    article = []
    encyclopedie = []
    volume = []
    titre = []
    nbr_colonne = []
    complement_titre = []
    num_page_debut = []
    num_page_fin = []
    signataire = []
    themes = []
    ref_histoire = []
    revue_citee = []

    for item in bindings:
        article.append(item["article"]["value"])
        encyclopedie.append(item.get("encyclopedie", {}).get("value", None))
        volume.append(item.get("volume", {}).get("value", None))
        titre.append(item["titre"]["value"])
        nbr_colonne.append(item.get("nbr_colonne", {}).get("value", None))
        complement_titre.append(item.get("complement_titre", {}).get("value", None))
        num_page_debut.append(item.get("num_page_debut", {}).get("value", None))
        num_page_fin.append(item.get("num_page_fin", {}).get("value", None))
        signataire.append(item.get("signataire", {}).get("value", None))
        themes.append(item.get("themes", {}).get("value", None))
        ref_histoire.append(item.get("ref_histoire", {}).get("value", None))
        revue_citee.append(item.get("revue_citee", {}).get("value", None))

    # Créer un DataFrame pandas avec les données extraites
    df_results = pd.DataFrame({
        "Titre": titre,
        "Encyclopedie": encyclopedie,
        "Volume": volume,
       
        "Nombre de Colonnes": nbr_colonne,
        "Complément de Titre": complement_titre,
        "Numéro de Page de Début": num_page_debut,
        "Numéro de Page de Fin": num_page_fin,
        "Signataire": signataire,
        "Thèmes": themes,
        "Référence à l'Histoire": ref_histoire,
        "Revue Citée": revue_citee
    })

    # Remplacer les valeurs None par des chaînes vides dans le DataFrame
    df_results = df_results.fillna('')

    # Filtrer par colonnes
    if not df_results.empty:
        with st.sidebar:
            filters = {}
            for col in df_results.columns:
                if col != "Titre":
                    filters[col] = st.multiselect(f'{col}:', [''] + df_results[col].unique())

        # Appliquer les filtres
        df_filtered = df_results
        for col, vals in filters.items():
            if vals and '' not in vals:
                df_filtered = df_filtered[df_filtered[col].isin(vals)]

        # Afficher le tableau filtré
        st.dataframe(df_filtered, use_container_width=True)

        # Convertir le DataFrame en CSV avec encodage UTF-8
        csv_data = df_filtered.to_csv(index=False).encode('utf-8')

        # Ajouter un bouton de téléchargement en CSV
        st.download_button(
            label="Télécharger en CSV (UTF-8)",
            data=csv_data,
            key="download-csv-article",
            on_click=None,  # Laisser "None" pour le téléchargement immédiat
            help="Téléchargez le tableau au format CSV (UTF-8).",
            mime="text/csv"  # Spécifiez le type MIME du fichier
        )

        if not filters:
            st.warning("Sélectionnez au moins un champ à filtrer.")
    else:
        st.warning("Aucun élément trouvé avec la sélection actuelle.")

# Vérifier si le script est exécuté en tant que script principal
if __name__ == "__main__":
    # Appel de votre fonction Exploration()
    Exploration()
