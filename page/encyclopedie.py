import streamlit as st
import pandas as pd
import json
from st_keyup import st_keyup
from Constants import DB_folder

# Fonction pour afficher les données des encyclopédies
def Encyclopedie():
    # Accéder aux données JSON retournées
    with open(DB_folder + 'encyclopedie.json', "r") as f:
        data = json.load(f)

    # Remplacer les valeurs "NULL" par une chaîne vide
    for item in data["results"]["bindings"]:
        for key, value in item.items():
            if value["value"] == "NULL":
                item[key]["value"] = ""

    bindings = data["results"]["bindings"]

    # Créer une liste pour chaque champ
    titre = []
    sous_titre = []
    nbr_volume = []
    nbr_page = []
    nbr_colonne = []
    table_auth = []
    table_art = []
    text_pres = []
    num_edit = []
    annee_publi = []
    anne_fin = []
    ville_publi = []
    pays_publi = []
    editeur = []
    responsable_edit = []
    Orga_finance = []
    public_cible = []

    for item in bindings:
        titre.append(item["titre"]["value"])
        sous_titre.append(item.get("sous_titre", {}).get("value", ""))
        nbr_volume.append(item.get("nbr_volume", {}).get("value", ""))
        nbr_page.append(item.get("nbr_page", {}).get("value", ""))
        nbr_colonne.append(item.get("nbr_colonne", {}).get("value", ""))
        table_auth.append(item.get("table_auth", {}).get("value", ""))
        table_art.append(item.get("table_art", {}).get("value", ""))
        text_pres.append(item.get("text_pres", {}).get("value", ""))
        num_edit.append(item.get("num_edit", {}).get("value", ""))
        annee_publi.append(item.get("annee_publi", {}).get("value", ""))
        anne_fin.append(item.get("anne_fin", {}).get("value", ""))
        ville_publi.append(item.get("ville_publi", {}).get("value", ""))
        pays_publi.append(item.get("pays_publi", {}).get("value", ""))
        editeur.append(item.get("editeur", {}).get("value", ""))
        responsable_edit.append(item.get("responsable_edit", {}).get("value", ""))
        Orga_finance.append(item.get("Orga_finance", {}).get("value", ""))
        public_cible.append(item.get("public_cible", {}).get("value", ""))

    # Créer un DataFrame pandas avec les données extraites
    df_results = pd.DataFrame({
        "Titre": titre,
        "Sous-titre": sous_titre,
        "Nombre de Volumes": nbr_volume,
        "Nombre de Pages": nbr_page,
        "Nombre de Colonnes": nbr_colonne,
        "Table des Auteurs": table_auth,
        "Table des Articles": table_art,
        "Texte de Présentation": text_pres,
        "Numéro d'Édition": num_edit,
        "Année de Publication": annee_publi,
        "Année de Fin": anne_fin,
        "Ville de Publication": ville_publi,
        "Pays de Publication": pays_publi,
        "Éditeur": editeur,
        "Responsable de l'Édition": responsable_edit,
        "Organisation Financière": Orga_finance,
        "Public Cible": public_cible
    })

    # Ajouter la barre de recherche en temps réel
    search_value = st_keyup("Rechercher", key="search")

    # Filtrer les données en fonction de la recherche
    if search_value:
        df_results = df_results[df_results.apply(lambda row: row.astype(str).str.contains(search_value, case=False).any(), axis=1)]

    # Afficher les données filtrées
    if not df_results.empty:
        with st.sidebar:
            filters = {}
            for col in df_results.columns:
                if col != "Titre":
                    unique_values = df_results[col].unique()
                    # Enlever les éléments vides des choix de filtre
                    unique_values = [value for value in unique_values if value != ""]
                    filters[col] = st.multiselect(f'{col}:', unique_values)

        # Appliquer les filtres
        for col, vals in filters.items():
            if vals:
                df_results = df_results[df_results[col].apply(lambda x: any(val in x for val in vals))]

        st.dataframe(df_results, use_container_width=True)

        # Convertir le DataFrame en CSV avec encodage UTF-8
        csv_data = df_results.to_csv(index=False).encode('utf-8')

        # Ajouter un bouton de téléchargement en CSV
        st.download_button(
            label="Télécharger en CSV (UTF-8)",
            data=csv_data,
            file_name='encyclopedia_data.csv',  # Nom du fichier à télécharger
            mime="text/csv",  # Spécifiez le type MIME du fichier
            help="Téléchargez les données au format CSV (UTF-8)."
        )
    else:
        st.warning("Aucun élément trouvé avec la sélection actuelle.")

# Vérifier si le script est exécuté en tant que script principal
if __name__ == "__main__":
    Encyclopedie()
