import pandas as pd

# Charger les fichiers CSV
df_article = pd.read_csv('/article.csv', sep=';', encoding='utf-8')
df_ouvrage_cite = pd.read_csv('/ouvrage_cite.csv', sep=';', encoding='utf-8')

# Fusionner les deux dataframes sur la colonne 'id_article'
merged_df = pd.merge(df_article, df_ouvrage_cite, how='left', left_on='id', right_on='id_article')

# Créer un dictionnaire pour stocker les colonnes 'id_ouvrage' pour chaque 'id_article'
id_ouvrage_dict = {}
for index, row in merged_df.iterrows():
    id_article = row['id']
    id_ouvrage = row['id_ouvrage']
    if pd.notnull(id_ouvrage):
        if id_article not in id_ouvrage_dict:
            id_ouvrage_dict[id_article] = [id_ouvrage]
        else:
            id_ouvrage_dict[id_article].append(id_ouvrage)

# Ajouter les colonnes ouvrage_cite1, ouvrage_cite2, ... au dataframe
for id_article, id_ouvrages in id_ouvrage_dict.items():
    for i, id_ouvrage in enumerate(id_ouvrages):
        column_name = f'ouvrage_cite{i+1}'
        df_article.loc[df_article['id'] == id_article, column_name] = id_ouvrage

# Sauvegarder le dataframe modifié dans un nouveau fichier CSV
df_article.to_csv('article_modifie.csv', sep=';', encoding='utf-8', index=False)
