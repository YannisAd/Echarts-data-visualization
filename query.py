from SPARQLWrapper import SPARQLWrapper, JSON
import json
import pandas as pd 
from Constants import *
from Sparql_query import *

def query_sparql(query, db_name):
    sparql = SPARQLWrapper(SPARQL_ENDPOINT_ACCESS)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    # Enregistrer les résultats dans un fichier JSON et dans le dossier ressources 
    with open(f"{DB_folder}/{db_name}.json", "w") as f:
        json.dump(results, f)

    return results



def create_local_DB():
    query_sparql(All_Personne_Query, 'personne')
    query_sparql(All_Article_Query, 'article')
    query_sparql(All_litteral_Article, 'complete_article')
    query_sparql(All_Encyclopedie_Query, 'encyclopedie')
    query_sparql(Article_Renvoi, 'renvoi')

 

def count_articles_with_attributes():
    

    # Connexion à l'endpoint SPARQL
    sparql = SPARQLWrapper(SPARQL_ENDPOINT_ACCESS)
    sparql.setQuery(Repartition_Elements_citee)
    sparql.setReturnFormat(JSON)

    # Exécution de la requête
    results = sparql.query().convert()

    # Récupération des valeurs de retour
    total_articles = int(results['results']['bindings'][0]['total_articles']['value'])
    articles_with_ouvrage_citee = int(results['results']['bindings'][0]['articles_with_ouvrage_citee']['value'])
    articles_with_personne_citee = int(results['results']['bindings'][0]['articles_with_personne_citee']['value'])
    articles_with_renvoi_article = int(results['results']['bindings'][0]['articles_with_renvoi_article']['value'])
    articles_with_revue = int(results['results']['bindings'][0]['articles_with_revue']['value'])

    # Retour des valeurs
    return total_articles, articles_with_ouvrage_citee, articles_with_personne_citee, articles_with_renvoi_article, articles_with_revue







def get_repartition_elements_citee_par_encyclopedie():
    # Connexion à l'endpoint SPARQL
    sparql = SPARQLWrapper(SPARQL_ENDPOINT_ACCESS)
    sparql.setQuery(Repartition_Elements_citee_par_encyclopedie)
    sparql.setReturnFormat(JSON)

    # Exécution de la requête
    results = sparql.query().convert()

    # Initialisation du dictionnaire de répartition
    repartition = {}

    # Récupération des résultats
    for result in results['results']['bindings']:
        # Vérification de la présence de la clé 'encyclopedie_nom'
        if 'encyclopedie_nom' in result:
            encyclopedie_nom = result['encyclopedie_nom']['value']
            total_articles = int(result['total_articles']['value'])
            articles_with_ouvrage_citee = int(result['articles_with_ouvrage_citee']['value'])
            articles_with_personne_citee = int(result['articles_with_personne_citee']['value'])
            articles_with_renvoi_article = int(result['articles_with_renvoi_article']['value'])
            articles_with_revue = int(result['articles_with_revue']['value'])

            # Ajout des résultats au dictionnaire de répartition
            repartition[encyclopedie_nom] = {
                'total_articles': total_articles,
                'articles_with_ouvrage_citee': articles_with_ouvrage_citee,
                'articles_with_personne_citee': articles_with_personne_citee,
                'articles_with_renvoi_article': articles_with_renvoi_article,
                'articles_with_revue': articles_with_revue
            }

    return repartition





def get_most_cited_people_by_encyclopedia():
    # Requête SPARQL
    sparql = SPARQLWrapper(SPARQL_ENDPOINT_ACCESS)
    sparql.setQuery(Cited_Person_count_by_encyclopedia)

    # Format des résultats
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    # Traitement des résultats
    most_cited_people = {}
    for result in results['results']['bindings']:
        encyclopedie_nom = result['encyclopedie_nom']['value']
        personne_nom = result['personne_nom']['value']
        nombre_de_citations_personne = int(result['nombre_de_citations_personne']['value'])
        nombre_de_citations_auteur = int(result['nombre_de_citations_auteur']['value'])

        # Vérifier si l'encyclopédie existe déjà dans le dictionnaire
        if encyclopedie_nom in most_cited_people:
            most_cited_people[encyclopedie_nom].append((personne_nom, nombre_de_citations_personne, nombre_de_citations_auteur))
        else:
            most_cited_people[encyclopedie_nom] = [(personne_nom, nombre_de_citations_personne, nombre_de_citations_auteur)]

    return most_cited_people





def get_articles_with_renvois():
    # Initialisation de l'endpoint SPARQL
    sparql = SPARQLWrapper(SPARQL_ENDPOINT_ACCESS)

    # Requête SPARQL
    sparql.setQuery(Article_Renvoi)

    # Format des résultats en JSON
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    articles = []
    for result in results["results"]["bindings"]:
        article = {
            "titre": result["titre"]["value"],
            "encyclopedie": result["encyclopedie_nom"]["value"],
            "renvois": result.get("renvois", {"value": ""})["value"]  # Assurez-vous que la clé existe
        }
        articles.append(article)

    return articles














def parse_renvoi_json():
    sparql = SPARQLWrapper(SPARQL_ENDPOINT_ACCESS)

    # Requête SPARQL
    sparql.setQuery(Article_Renvoi)

    # Format des résultats en JSON
    sparql.setReturnFormat(JSON)
    renvoi_json = sparql.query().convert()

    parsed_data = []

    # Parcours des résultats SPARQL
    for result in renvoi_json["results"]["bindings"]:
        article = {
            "titre": result["titre"]["value"],
            "encyclopedie": result.get("encyclopedie_nom", {"value": "Inconnu"})["value"],
            "renvois": [],
            "nombre_de_fois_citee": 0,
            "nombre_de_citations": 0
        }

        if "renvois" in result:
            renvois_value = result["renvois"]["value"]
            renvois_list = renvois_value.split(" ; ")
            article["renvois"] = renvois_list
            article["nombre_de_citations"] = len(renvois_list)

        parsed_data.append(article)

    # Parcours du JSON pour calculer nombre_de_fois_citee
    for article in parsed_data:
        for other_article in parsed_data:
            if other_article["encyclopedie"] == article["encyclopedie"] and article["titre"] in other_article["renvois"]:
                article["nombre_de_fois_citee"] += 1

    # Écriture des données dans le fichier JSON
    with open(DB_folder + "renvoi_2.json", "w") as f:
        json.dump(parsed_data, f, indent=4)

    













# Vérifier si le script est exécuté en tant que script principal
if __name__ == "__main__":
    # Appel de la fonction create_local_DB()
    create_local_DB()
