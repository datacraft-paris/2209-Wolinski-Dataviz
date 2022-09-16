# coding: utf-8

data5 = (pd.merge(swi, swi_gps[["NUMERO", "code_departement"]], on="NUMERO")
         .set_index("DATE")
         .groupby(["Code Département", pd.Grouper(freq="A")])["SWI_UNIF_MENS3"]
         .mean()
         .reset_index()
        )

def display_year5(year):
    # select year and add all labels
    df = (data5.loc[data5["DATE"].dt.year==year]
         )

    # choropleth_mapbox
    return px.choropleth_mapbox(data_frame=df,
                                geojson=departements,
                                locations='code_departement',
                                color="SWI_UNIF_MENS3",
                                featureidkey='properties.code',
                                color_continuous_scale="RdYlGn",
                                mapbox_style="carto-positron",
                                zoom=4,
                                center={"lat": 47.0, "lon": 3.0},
                                opacity=0.5,
                                labels={"SWI_UNIF_MENS3": f"Moyenne SWI en {year}"},
                                width=700)

display_year5(2006)
