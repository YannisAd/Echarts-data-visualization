import pymysql
import os
from Constants import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER, DB_folder
from datetime import datetime, timedelta



# Fonction pour télécharger la base de données
def download_database():
    try:
        # Connexion à la base de données
        conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_NAME)
        cursor = conn.cursor()

        # Chemin complet du fichier de sauvegarde
        backup_file = os.path.join(DB_folder, f"backup_{datetime.now().strftime('%Y-%m-%d')}.sql")

        # Exécution de la commande pour sauvegarder la base de données
        backup_command = f"mysqldump -u {DB_USER} -p{DB_PASSWORD} {DB_NAME} > {backup_file}"
        os.system(backup_command)

        # Fermeture de la connexion
        conn.close()

        print(f"La sauvegarde de la base de données a été effectuée avec succès dans {backup_file}.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la sauvegarde de la base de données : {str(e)}")

# Appel de la fonction pour télécharger la base de données
download_database()
