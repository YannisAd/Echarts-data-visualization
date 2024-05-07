import pandas as pd
import json
from pyecharts import options as opts
from pyecharts.charts import Graph
from Constants import *

import json
from streamlit_echarts import st_echarts

def render_heatmap_enc_and_article():
    # Charger les données depuis le fichier JSON
    with open('renvoi_2.json', 'r') as f:
        data = json.load(f)

    # Préparer les données pour le heatmap
    encyclopedies = list(set(entry["encyclopedie"] for entry in data))
    articles = list(set(entry["titre"] for entry in data))
    values = [[entry["encyclopedie"], entry["titre"], entry["nombre_de_fois_citee"]] for entry in data]

    option = {
        "tooltip": {"position": "top"},
        "grid": {"height": "50%", "top": "10%"},
        "xAxis": {"type": "category", "data": articles, "splitArea": {"show": True}},
        "yAxis": {"type": "category", "data": encyclopedies, "splitArea": {"show": True}},
        "visualMap": {
            "min": 0,
            "max": max(entry["nombre_de_fois_citee"] for entry in data),
            "calculable": True,
            "orient": "horizontal",
            "left": "center",
            "bottom": "15%",
        },
        "series": [
            {
                "name": "Heatmap",
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

