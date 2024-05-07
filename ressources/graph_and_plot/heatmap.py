import json
from streamlit_echarts import st_echarts
from Constants import DB_folder


import json
from collections import defaultdict
from streamlit_echarts import st_echarts

def render_heatmap_enc_and_article():
    # Charger les données depuis le fichier JSON
    with open(DB_folder+'renvoi_2.json', 'r') as f:
        data = json.load(f)

    # Regrouper les données par encyclopédie
    encyclopedies_data = defaultdict(list)
    for entry in data:
        encyclopedies_data[entry["encyclopedie"]].append(entry)

    # Générer un heatmap par encyclopédie
    for encyclopedie, articles_data in encyclopedies_data.items():
        articles = list(set(entry["titre"] for entry in articles_data))
        values = [[entry["titre"], entry["nombre_de_fois_citee"]] for entry in articles_data]

        # Ajouter les articles avec un nombre de citations de 0
        for entry in articles_data:
            if entry["nombre_de_fois_citee"] == 0:
                articles.append(entry["titre"])
                values.append([entry["titre"], 0])

        option = {
            "tooltip": {"position": "top"},
            "grid": {"height": "50%", "top": "10%"},
            "xAxis": {"type": "category", "data": articles, "splitArea": {"show": True}},
            "yAxis": {"type": "category", "data": [encyclopedie], "splitArea": {"show": True}},
            "visualMap": {
                "min": 0,
                "max": max(entry["nombre_de_fois_citee"] for entry in articles_data),
                "calculable": True,
                "orient": "horizontal",
                "left": "center",
                "bottom": "15%",
            },
            "series": [
                {
                    "name": f"Heatmap - {encyclopedie}",
                    "type": "heatmap",
                    "data": values,
                    "label": {"show": True},
                    "emphasis": {
                        "itemStyle": {"shadowBlur": 10, "shadowColor": "rgba(0, 0, 0, 0.5)"}
                    },
                }
            ],
        }
        
        st_echarts(option, height="500px")
