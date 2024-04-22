from query import count_articles_with_attributes
from pyecharts import options as opts
from pyecharts.charts import Pie
from streamlit_echarts import st_pyecharts
from query import count_articles_with_attributes

pie_counter = 0



def pie() :

    global pie_counter
    pie_counter += 1
    unique_key = f"pie_{pie_counter}"

    

    # Récupérer les valeurs depuis la fonction count_articles_with_attributes
    total_article, ouvrage_citee_count, personne_citee_count, renvoi_article_count, revue_citee_count = count_articles_with_attributes()
    
    # Créer le graphique en secteurs (pie chart)
    c = (
        Pie()
        .add(
            "",
            [
                ["Avec ouvrage cité", ouvrage_citee_count],
                ["Avec personne citée", personne_citee_count],
                ["Avec renvoi d'article", renvoi_article_count],
                ["Avec une revue citée", revue_citee_count],
                
            ],
            radius=["30%", "75%"],  # Paramètres de rayon pour donner l'impression d'une coupe en secteurs
            center=["70%", "50%"],  # Position du graphique dans l'espace
            rosetype="radius"  # Type de rosace pour une meilleure visualisation
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Répartition des articles"),
            legend_opts=opts.LegendOpts(
                orient="vertical",  # Orienté verticalement pour une meilleure disposition
                pos_top="15%",  # Position par rapport au haut de la fenêtre
                pos_left="2%"  # Position par rapport à la gauche de la fenêtre
            ),
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))  # Format d'étiquetage des secteurs
    )


    # Affichage du graphique dans Streamlit
# Votre code pour créer le graphique pie avec la clé unique
    st_pyecharts(c, key=unique_key)