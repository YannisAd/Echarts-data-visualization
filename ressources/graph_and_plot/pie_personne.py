from streamlit_echarts import st_pyecharts
from pyecharts.charts import Bar, Pie
from pyecharts import options as opts
from Query import get_most_cited_people_by_encyclopedia

def display_most_cited_people_chart():
    pie_data = []

    # Obtenir les données des personnes les plus citées par encyclopédie
    most_cited_people_by_encyclopedia = get_most_cited_people_by_encyclopedia()

    for encyclopedie_nom, personnes in most_cited_people_by_encyclopedia.items():
        bar_chart = Bar()

        # Sélectionner les 20 personnes les plus citées pour le graphique à barres
        personnes_bar_chart = sorted(personnes, key=lambda x: x[1], reverse=True)[:20]

        # Ajouter les données pour le graphique à barres
        bar_chart.add_xaxis([entry[0] for entry in personnes_bar_chart])
        bar_chart.add_yaxis(
            series_name="En tant que personne",
            y_axis=[entry[1] for entry in personnes_bar_chart],
            itemstyle_opts=opts.ItemStyleOpts(color="#5470C6"),  # Couleur pour les citations en tant que personne
        )
        bar_chart.add_yaxis(
            series_name="En tant qu'auteur",
            y_axis=[entry[2] for entry in personnes_bar_chart],
            itemstyle_opts=opts.ItemStyleOpts(color="#91CC75"),  # Couleur pour les citations en tant qu'auteur
        )
        bar_chart.set_global_opts(
            title_opts=opts.TitleOpts(title=f"Répartition des citations dans {encyclopedie_nom}"),
            xaxis_opts=opts.AxisOpts(name="Personnes"),
            yaxis_opts=opts.AxisOpts(name="Nombre de citations"),
            legend_opts=opts.LegendOpts(
                orient="vertical",
                pos_top="15%",
                pos_left="0%",
            ),
        )

        # Afficher le graphique à barres pour chaque encyclopédie
        st_pyecharts(bar_chart)

        # Ajouter les données pour le graphique pie
        pie_data.extend(personnes)

    # Trier les données pour le graphique circulaire
    pie_data_sorted = sorted(pie_data, key=lambda x: x[1] + x[2], reverse=True)

    # Sélectionner les 15 personnes les plus citées pour le graphique circulaire
    top_10_personnes = pie_data_sorted[:10]

    # Créer le graphique pie pour la répartition des 15 personnes les plus citées
    pie = (
        Pie()
        .add(
            series_name="Répartition des personnes les plus citées",
            data_pair=[(entry[0], entry[1] + entry[2]) for entry in top_10_personnes],
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Répartition des personnes les plus citées (sans distinction)"),
            legend_opts=opts.LegendOpts(
                orient="vertical",
                pos_top="15%",
                pos_left="0%",
            ),
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )

    # Afficher le graphique pie avec les 15 personnes les plus citées
    st_pyecharts(pie)

