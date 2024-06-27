from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from streamlit_echarts import st_pyecharts
from query import get_repartition_elements_citee_par_encyclopedie

def bar_label():
    # Récupérer les valeurs depuis la fonction get_repartition_elements_citee_par_encyclopedie
    repartition = get_repartition_elements_citee_par_encyclopedie()
    
    # Créer le graphique à barres
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(list(repartition.keys()))  # Les noms des encyclopédies seront sur l'axe des abscisses
        .add_yaxis("Articles avec ouvrage cité", [item['articles_with_ouvrage_citee'] for item in repartition.values()], stack="stack1")  # Ajouter les données pour chaque encyclopédie
        .add_yaxis("Articles avec personne citée", [item['articles_with_personne_citee'] for item in repartition.values()], stack="stack1")
        .add_yaxis("Articles avec renvoi d'article", [item['articles_with_renvoi_article'] for item in repartition.values()], stack="stack1")
        .add_yaxis("Articles avec une revue citée", [item['articles_with_revue'] for item in repartition.values()], stack="stack1")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Répartition des articles par encyclopédie"),  # Titre du graphique
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-45)),  # Rotation des libellés sur l'axe des abscisses
            legend_opts=opts.LegendOpts(orient="vertical", pos_top="5%", pos_right="2%"),  # Position de la légende
            datazoom_opts=opts.DataZoomOpts(type_="inside"),  # Zoom pour faciliter la visualisation
        )
    )

    # Affichage du graphique dans Streamlit
    st_pyecharts(c, key="unique_key")  # Passer une clé unique à la fonction st_pyecharts
