import streamlit as st
import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON
from Query import query_sparql, All_Personne_Query

def Personne():
    # Appel de la fonction query_sparql avec la requête All_Personne_Query et le nom de la base de données "personne"
    results = query_sparql(All_Personne_Query, "personne")

    # Accéder aux données JSON retournées
    bindings = results["results"]["bindings"]

    # Créer une liste pour chaque champ
    nom_complet = [item["nom_complet"]["value"] for item in bindings]
    prenom = [item["prenom"]["value"] for item in bindings]
    nom_de_famille = [item["nom_de_famille"]["value"] for item in bindings]
    sexe = [item["sexe"]["value"] for item in bindings]
    date_naissance = [item["date_naissance"]["value"] for item in bindings]
    ville_naissance = [item["ville_naissance"]["value"] for item in bindings]
    date_mort = [item["date_mort"]["value"] if "date_mort" in item else None for item in bindings]
    ville_mort = [item["ville_mort"]["value"] if "ville_mort" in item else None for item in bindings]

    # Créer un DataFrame pandas avec les données extraites
    df_results = pd.DataFrame({
        "Nom Complet": nom_complet,
        "Prénom": prenom,
        "Nom de Famille": nom_de_famille,
        "Sexe": sexe,
        "Date de Naissance": date_naissance,
        "Ville de Naissance": ville_naissance,
        "Date de Mort": date_mort,
        "Ville de Mort": ville_mort
    })

    # Filtrer par colonnes
    if not df_results.empty:
        with st.sidebar:
            filters = {}
            for col in df_results.columns:
                if col != "Nom Complet":
                    filters[col] = st.multiselect(f'{col}:', df_results[col].unique())

        # Appliquer les filtres
        df_filtered = df_results
        for col, vals in filters.items():
            if vals:
                df_filtered = df_filtered[df_filtered[col].isin(vals)]

        # Afficher le tableau filtré
        st.dataframe(df_filtered, use_container_width=True)

        # Convertir le DataFrame en CSV avec encodage UTF-8
        csv_data = df_filtered.to_csv(index=False).encode('utf-8')

        # Ajouter un bouton de téléchargement en CSV
        st.download_button(
            label="Télécharger en CSV (UTF-8)",
            data=csv_data,
            key="download-csv",
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
    # Appel de votre fonction Personne()
    Personne()
