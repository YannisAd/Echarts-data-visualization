import json
from pyecharts import options as opts
from pyecharts.charts import Sankey
from Constants import DB_folder
from streamlit_echarts import st_echarts


def render_article_sankey():
    # Charger les données du fichier renvoi_2.json
    with open(DB_folder + "renvoi_2.json", "r") as f:
        articles_with_renvois = json.load(f)

    # Créer des ensembles distincts de tous les titres d'articles et de tous les renvois
    all_titles = set(article["titre"] for article in articles_with_renvois)
    all_renvois = set(renvoi for article in articles_with_renvois for renvoi in article["renvois"])

    # Créer les listes de liens pour le diagramme Sankey
    links = []
    for article in articles_with_renvois:
        for renvoi in article["renvois"]:
            links.append({"source": article["titre"], "target": renvoi, "value": article["nombre_de_fois_citee"]})

    # Créer les nœuds pour le diagramme Sankey
    nodes = [{"name": title} for title in all_titles] + [{"name": renvoi} for renvoi in all_renvois]

    # Créer les niveaux pour le diagramme Sankey
    levels = [{"depth": depth, "itemStyle": {"color": f"#{depth%256:02x}{(depth*2)%256:02x}{(depth*3)%256:02x}"}} for depth in range(len(all_titles) + len(all_renvois))]

    option = {
        "title": {"text": "Sankey Diagram"},
        "tooltip": {"trigger": "item", "triggerOn": "mousemove"},
        "series": [
            {
                "type": "sankey",
                "data": nodes,
                "links": links,
                "emphasis": {"focus": "adjacency"},
                "levels": levels,
                "lineStyle": {"curveness": 0.5},
            }
        ],
    }

    # Afficher le diagramme Sankey
    st_echarts(option, height="500px")

