# coding: utf-8

data2 = (bdiff.groupby(["Année", "Département"])["Surface brûlée (ha)"]
        .sum()
        .reset_index()
       )

def display_year2(year):
    # select year and add all labels
    df = (data2.loc[data2["Année"]==year]
          .set_index("Département")
          .reindex(codes)
          .fillna(0)
          .reset_index()
         )

    # choropleth_mapbox
    return px.choropleth_mapbox(data_frame=df,
                                geojson=departements,
                                locations='Département',
                                color="Surface brûlée (ha)",
                                featureidkey='properties.code',
                                color_continuous_scale="RdYlGn_r",
                                mapbox_style="carto-positron",
                                zoom=4,
                                center={"lat": 47.0, "lon": 3.0},
                                opacity=0.5,
                                labels={"Surface brûlée (ha)": f"Surface brûlée (ha) en {year}"},
                                width=700)

display_year2(2006)
