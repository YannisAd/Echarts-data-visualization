import pymysql
from Constants import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER

def get_data_from_db():
    # Connexion à la base de données
    conn = pymysql.connect(host=DB_HOST, user=DB_NAME, password=DB_PASSWORD, db=DB_USER)
    cursor = conn.cursor()

    # Exécution de la requête avec une jointure entre les tables
    query = """
            SELECT * FROM patrimaths_articles
                LEFT JOIN patrimaths_encyclopedies ON patrimaths_articles.id = patrimaths_encyclopedies.id
                LEFT JOIN patrimaths_exemplaires ON patrimaths_articles.id = patrimaths_exemplaires.id
                LEFT JOIN patrimaths_ouvrages ON patrimaths_articles.id = patrimaths_ouvrages.id
                LEFT JOIN patrimaths_ouvrages_cites ON patrimaths_articles.id = patrimaths_ouvrages_cites.id_article
                LEFT JOIN patrimaths_personnes ON patrimaths_articles.id = patrimaths_personnes.id
                LEFT JOIN patrimaths_personnes_citees ON patrimaths_articles.id = patrimaths_personnes_citees.id_article
                LEFT JOIN patrimaths_revues ON patrimaths_articles.id = patrimaths_revues.id
                LEFT JOIN patrimaths_revues_citees ON patrimaths_articles.id = patrimaths_revues_citees.id
        """
    cursor.execute(query)

    # Récupérer les résultats
    data = cursor.fetchall()

    # Fermer la connexion
    conn.close()

    return data


data = get_data_from_db()
print(data)  