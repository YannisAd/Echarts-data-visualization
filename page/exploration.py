import streamlit as st
import pandas as pd
import json
from st_keyup import st_keyup
from Constants import DB_folder

# Requête SPARQL pour récupérer tous les articles avec leurs informations
def Exploration():
    # Appel de la fonction query_sparql avec la requête All_Article_Query
    with open(DB_folder+'/complete_article.json', "r") as f:
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
    personne_citee = []
    renvoi_article = []
    ouvrage_citee = []

    for item in bindings:
        article.append(item["article"]["value"])
        encyclopedie.append(item.get("encyclopedie", {}).get("value", ""))
        volume.append(item.get("volume", {}).get("value", ""))
        titre.append(item["titre"]["value"])
        nbr_colonne.append(item.get("nbr_colonne", {}).get("value", ""))
        complement_titre.append(item.get("complement_titre", {}).get("value", ""))
        num_page_debut.append(item.get("num_page_debut", {}).get("value", ""))
        num_page_fin.append(item.get("num_page_fin", {}).get("value", ""))
        
        # Convertir la valeur en une chaîne de caractères ou une chaîne vide si elle est None
        signataire_value = item.get("signataires", {}).get("value", "")
        signataire.append(signataire_value if signataire_value else "")
        
        themes_value = item.get("theme", {}).get("value", "")
        themes.append(themes_value if themes_value else "")
        
        ref_histoire_value = item.get("ref_histoire", {}).get("value", "")
        ref_histoire.append(ref_histoire_value if ref_histoire_value else "")
        
        revue_citee_value = item.get("revue_citee", {}).get("value", "")
        revue_citee.append(revue_citee_value if revue_citee_value else "")
        
        personne_citee_value = item.get("personnes_citees", {}).get("value", "")
        personne_citee.append(personne_citee_value if personne_citee_value else "")
        
        renvoi_article_value = item.get("renvois_titre", {}).get("value", "")
        renvoi_article.append(renvoi_article_value if renvoi_article_value else "")
        
        ouvrage_citee_value = item.get("ouvrages_cites", {}).get("value", "")
        ouvrage_citee.append(ouvrage_citee_value if ouvrage_citee_value else "")

    # Créer un DataFrame pandas avec les données extraites
    df_results = pd.DataFrame({
        "Titre": titre,
        "Encyclopedie": encyclopedie,
        "Volume": volume,
        "Nombre de Colonnes": nbr_colonne,
        "Complément de Titre": complement_titre,
        "Numéro de Page de Début": num_page_debut,
        "Numéro de Page de Fin": num_page_fin,
        "Signataire": [signataire_value.split(" ; ") if isinstance(signataire_value, str) else "" for signataire_value in signataire],
        "Thèmes": [themes_value.split(" ; ") if isinstance(themes_value, str) else "" for themes_value in themes],
        "Référence à l'Histoire": ref_histoire,
        "Personne citée": [personne_citee_value.split(" ; ") if isinstance(personne_citee_value, str) else "" for personne_citee_value in personne_citee],
        "Revue Citée": [revue_citee_value.split(" ; ") if isinstance(revue_citee_value, str) else "" for revue_citee_value in revue_citee],
        "Ouvrages Cités" : [ouvrage_citee_value.split(" ; ") if isinstance(ouvrage_citee_value, str) else "" for ouvrage_citee_value in ouvrage_citee],
        "Renvoi vers l'article" : [renvoi_article_value.split(" ; ") if isinstance(renvoi_article_value, str) else "" for renvoi_article_value in renvoi_article],
    })

    # Ajoutez la barre de recherche en temps réel
    search_value = st_keyup("Rechercher", key="search")

    # Vérifier si des filtres sont actifs
    filters_active = any([st.session_state.get(f"{col}_value") for col in df_results.columns if col != "Titre"])

    # Appliquer le filtre de recherche
    if search_value:
        if filters_active:
            # Si des filtres sont actifs, rechercher uniquement dans le DataFrame filtré
            df_filtered = df_results[df_results.apply(lambda row: row.astype(str).str.contains(search_value, case=False).any(), axis=1)]
        else:
            # Sinon, rechercher dans tout le DataFrame
            df_filtered = df_results[df_results.apply(lambda row: row.astype(str).str.contains(search_value, case=False).any(), axis=1)]
    else:
        # Si aucune valeur de recherche n'est fournie, afficher le DataFrame non filtré
        df_filtered = df_results

    if not df_filtered.empty:
        with st.sidebar:
            filters = {}
            for col in df_filtered.columns:
                if col != "Titre":
                    # Aplatir les listes imbriquées avant d'extraire les valeurs uniques
                    unique_values = df_filtered[col].explode().apply(pd.Series).stack().unique()
                    filters[col] = st.multiselect(f'{col}:', [''] + unique_values)

        # Appliquer les filtres
        for col, vals in filters.items():
            if vals and '' not in vals:
                df_filtered = df_filtered[df_filtered[col].apply(lambda x: any(val in x for val in vals))]

        # Afficher le tableau filtré
        st.dataframe(df_filtered, use_container_width=True)

        # Convertir le DataFrame en CSV avec encodage UTF-8
        csv_data = df_filtered.to_csv(index=False).encode('utf-8')

        # Ajouter un bouton de téléchargement en CSV
        st.download_button(
            label="Télécharger en CSV (UTF-8)",
            data=csv_data,
            file_name='data.csv',  # Nom du fichier à télécharger
            mime="text/csv",  # Spécifiez le type MIME du fichier
            help="Téléchargez le tableau au format CSV (UTF-8)."
        )

        if not filters:
            st.warning("Sélectionnez au moins un champ à filtrer.")
    else:
        st.warning("Aucun élément trouvé avec la sélection actuelle.")

# Vérifier si le script est exécuté en tant que script principal
if __name__ == "__main__":
    Exploration()
