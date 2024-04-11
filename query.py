from SPARQLWrapper import SPARQLWrapper, JSON
import json

def query_sparql(query, db_name):
    sparql = SPARQLWrapper("http://testyannis.henripoincare.fr/PatriMaths_encyclopedie/")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    # Enregistrer les résultats dans un fichier JSON et dans le dossier ressources 
    with open(f"ressources/{db_name}.json", "w") as f:
        json.dump(results, f)

    return results

All_Personne_Query = """
    PREFIX PMe: <urn:absolute:PatriMaths_Ontology_encyclopedie>
    SELECT ?nom_complet ?prenom ?nom_de_famille ?sexe ?date_naissance ?ville_naissance ?date_mort ?ville_mort
    WHERE {
        ?personne a PMe:PatriMaths_Ontology_encyclopediePersonne .
        ?personne PMe:PatriMaths_Ontology_encyclopediea_pour_nom_complet ?nom_complet .
        ?personne PMe:PatriMaths_Ontology_encyclopediea_pour_prenom ?prenom .
        ?personne PMe:PatriMaths_Ontology_encyclopediea_pour_nom_de_famille ?nom_de_famille .
        ?personne PMe:PatriMaths_Ontology_encyclopediea_pour_sexe ?sexe .
        ?personne PMe:PatriMaths_Ontology_encyclopediea_pour_date_de_naissance ?date_naissance .
        ?personne PMe:PatriMaths_Ontology_encyclopediea_pour_ville_de_naissance ?ville_naissance .
        OPTIONAL { ?personne PMe:PatriMaths_Ontology_encyclopediea_pour_date_de_mort ?date_mort }
        OPTIONAL { ?personne PMe:PatriMaths_Ontology_encyclopediea_pour_ville_de_mort ?ville_mort }
    }
"""

All_Article_Query = """
    PREFIX PMe: <urn:absolute:PatriMaths_Ontology_encyclopedie>

    SELECT ?article ?encyclopedie ?volume ?titre ?nbr_colonne ?complement_titre ?num_page_debut ?num_page_fin ?signataire ?themes ?designant ?renvoi ?ref_non_math ?ref_histoire ?symbole_math ?figure ?commentaire ?personne_citee ?ouvrage_citee ?revue_citee
    WHERE {
        ?article a PMe:PatriMaths_Ontology_encyclopedieArticle_encyclopedie .
        OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopedieest_publie_dans_le_support_imprime ?encyclopedie }
        OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediese_trouve_au_volume_numero ?volume }
        ?article PMe:PatriMaths_Ontology_encyclopediea_pour_titre-article ?titre .
        OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediea_pour_complement_de_titre-article ?complement_titre }
        OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediecommence_a_la_page_numero ?num_page_debut }
        OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediefini_a_la_page_numero ?num_page_fin }
        OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediea_pour_nombre_de_colonne-article ?nbr_colonne }
        OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediea_pour_signataire-Article ?signataire }
        OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopedieconcerne_le_theme-article ?themes }
        OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopedieest_inclus_dans_le_designant ?designant }
        OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediecontient_un_renvoi_a ?renvoi }
        OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediea_une_reference_non_mathematique ?ref_non_math }
        OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediea_une_reference_a_l_histoire ?ref_histoire }
        OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediecontient_au_moins_un_symbole_mathematique ?symbole_math }
        OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediecontient_au_moins_une_figure ?figure }
        OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediea_comme_commentaire ?commentaire }
        OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediecite_la_personne ?personne_citee }
        OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediecite_l_ouvrage ?ouvrage_citee }
        OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediecite_un_article_contenu_dans_le_periodique ?revue_citee }
    }
"""


All_llitteral_Article = """
PREFIX PMe: <urn:absolute:PatriMaths_Ontology_encyclopedie>
PREFIX foaf: <http://xmlns.com/foaf/0.1>

SELECT ?article ?encyclopedie ?volume ?titre ?nbr_colonne ?complement_titre ?num_page_debut ?num_page_fin 
       ?signataire_nom ?themes_label ?designant ?renvoi_titre ?ref_non_math ?ref_histoire ?symbole_math ?figure 
       ?commentaire ?personne_citee_nom ?ouvrage_citee ?revue_citee
WHERE {
    ?article a PMe:PatriMaths_Ontology_encyclopedieArticle_encyclopedie .
    OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopedieest_publie_dans_le_support_imprime ?encyclopedie }
    OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediese_trouve_au_volume_numero ?volume }
    ?article PMe:PatriMaths_Ontology_encyclopediea_pour_titre-article ?titre .
    OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediea_pour_complement_de_titre-article ?complement_titre }
    OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediecommence_a_la_page_numero ?num_page_debut }
    OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediefini_a_la_page_numero ?num_page_fin }
    OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediea_pour_nombre_de_colonne-article ?nbr_colonne }
    OPTIONAL { 
        ?article PMe:PatriMaths_Ontology_encyclopediea_pour_signataire-Article ?signataire .
        ?signataire PMe:PatriMaths_Ontology_encyclopediea_pour_nom_complet ?signataire_nom
    }
    OPTIONAL { 
        ?article PMe:PatriMaths_Ontology_encyclopedieconcerne_le_theme-article ?themes .
        ?themes foaf:theme ?themes_label
    }
    OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopedieest_inclus_dans_le_designant ?designant }
    OPTIONAL { 
        ?article PMe:PatriMaths_Ontology_encyclopediecontient_un_renvoi_a ?renvoi .
        ?renvoi PMe:PatriMaths_Ontology_encyclopediea_pour_titre-article ?renvoi_titre
    }
    OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediea_une_reference_non_mathematique ?ref_non_math }
    OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediea_une_reference_a_l_histoire ?ref_histoire }
    OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediecontient_au_moins_un_symbole_mathematique ?symbole_math }
    OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediecontient_au_moins_une_figure ?figure }
    OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediea_comme_commentaire ?commentaire }
    OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediecite_la_personne ?personne_citee }
    OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediecite_l_ouvrage ?ouvrage_citee }
    OPTIONAL { ?article PMe:PatriMaths_Ontology_encyclopediecite_un_article_contenu_dans_le_periodique ?revue_citee }
}

"""

All_Encyclopedie_Query = """
    PREFIX PMe: <urn:absolute:PatriMaths_Ontology_encyclopedie>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>

    SELECT ?titre ?sous_titre ?nbr_volume ?nbr_page ?nbr_colonne ?table_auth ?table_art ?text_pres ?num_edit ?annee_publi ?anne_fin ?ville_publi ?pays_publi ?langue ?editeur ?responsable_edit ?Orga_finance ?public_cible 
    WHERE {
        ?encyclopedie a foaf:Document .
        
        ?encyclopedie PMe:PatriMaths_Ontology_encyclopediea_pour_titre-support_imprime ?titre .
        OPTIONAL { ?encyclopedie PMe:PatriMaths_Ontology_encyclopediea_pour_sous_titre ?sous_titre }
        OPTIONAL { ?encyclopedie PMe:PatriMaths_Ontology_encyclopediea_pour_nombre_de_volume-support_imprime ?nbr_volume }
        OPTIONAL { ?encyclopedie PMe:PatriMaths_Ontology_encyclopediea_pour_nombre_de_page-support_imprime ?nbr_page }
        OPTIONAL { ?encyclopedie PMe:PatriMaths_Ontology_encyclopediea_pour_nombre_colonne_par_page ?nbr_colonne }
        OPTIONAL { ?encyclopedie PMe:PatriMaths_Ontology_encyclopediecontient_au_moins_une_table_des_auteurs_autrices ?table_auth }
        OPTIONAL { ?encyclopedie PMe:PatriMaths_Ontology_encyclopediecontient_au_moins_une_table_des_articles ?table_art }
        OPTIONAL { ?encyclopedie PMe:PatriMaths_Ontology_encyclopediecontient_au_moins_un_texte_de_presentation ?text_pres }
        OPTIONAL { ?encyclopedie PMe:PatriMaths_Ontology_encyclopediea_pour_numero_d_edition ?num_edit }
        OPTIONAL { ?encyclopedie PMe:PatriMaths_Ontology_encyclopedieest_publie_la_premiere_fois_en ?annee_publi }
        OPTIONAL { ?encyclopedie PMe:PatriMaths_Ontology_encyclopedieest_publie_jusqu_en ?anne_fin }
        OPTIONAL { ?encyclopedie PMe:PatriMaths_Ontology_encyclopediea_pour_ville_de_publication ?ville_publi }
        OPTIONAL { ?encyclopedie PMe:PatriMaths_Ontology_encyclopediea_pour_pays_de_publication ?pays_publi }
        OPTIONAL { ?encyclopedie PMe:PatriMaths_Ontology_encyclopediea_pour_langue ?langue }
        OPTIONAL { ?encyclopedie PMe:PatriMaths_Ontology_encyclopedieest_publie_par ?editeur }
        OPTIONAL { ?encyclopedie PMe:PatriMaths_Ontology_encyclopediea_pour_responsable_editorial ?responsable_edit }
        OPTIONAL { ?encyclopedie PMe:PatriMaths_Ontology_encyclopedieest_finance_par ?Orga_finance }
        OPTIONAL { ?encyclopedie PMe:PatriMaths_Ontology_encyclopedieest_dedie_a ?public_cible }
    }
"""

def create_local_DB():
    query_sparql(All_Personne_Query, 'personne')
    query_sparql(All_Article_Query, 'article')
    query_sparql(All_Article_Query, 'complete_article')

    query_sparql(All_Encyclopedie_Query, 'encyclopedie')

# Vérifier si le script est exécuté en tant que script principal
if __name__ == "__main__":
    # Appel de la fonction create_local_DB()
    create_local_DB()
