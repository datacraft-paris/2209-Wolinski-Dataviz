# coding: utf-8

def display_year1(year):
    # select year and add all labels
    df = (data1.loc[data1["Année"]==year]
          .set_index("Département")
          .reindex(codes)
          .fillna(0)
          .reset_index()
         )

    # choropleth_mapbox
    return px.choropleth_mapbox(data_frame=df,
                                geojson=departements,
                                locations='Département',
                                color="Nombre d'incendies",
                                featureidkey='properties.code',
                                color_continuous_scale="RdYlGn_r",
                                mapbox_style="carto-positron",
                                zoom=4,
                                center={"lat": 47.0, "lon": 3.0},
                                opacity=0.5,
                                labels={"Nombre d'incendies": f"Nombre d'incendies en {year}"},
                                width=700)

display_year1(2017)
