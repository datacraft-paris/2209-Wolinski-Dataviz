# coding: utf-8

data4 = (bdiff[["Département", "Année"]].drop_duplicates()
        .groupby("Département")
        .size()
        .reindex(codes)
        .fillna(0)
        .reset_index()
        .rename(columns={0:"Nombre d'années avec incendies"})
       )

# choropleth_mapbox
px.choropleth_mapbox(data_frame=data4,
                     geojson=departements,
                     locations='Département',
                     color="Nombre d'années avec incendies",
                     featureidkey='properties.code',
                     color_continuous_scale="RdYlGn_r",
                     mapbox_style="carto-positron",
                     zoom=4,
                     center={"lat": 47.0, "lon": 3.0},
                     opacity=0.5,
                     width=800
                    )
