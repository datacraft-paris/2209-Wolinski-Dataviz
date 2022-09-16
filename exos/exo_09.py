# coding: utf-8

# load correspondance-code-insee-code-postal.csv
insee = pd.read_csv("data/correspondance-code-insee-code-postal.csv",
                   sep=";",
                   usecols=["Code INSEE", "Code Département", "geo_point_2d"])

insee = (insee.assign(**insee.geo_point_2d
                      .str
                      .extract(r"(?P<lat>.*), (?P<lon>.*)")
                      .astype(float))
        )

data3 = pd.merge(bdiff, insee, on="Code INSEE")

def display_year3(year):

    df = data3.loc[data3["Année"]==year]

    return px.scatter_mapbox(data_frame=df,
                             lat="lat",
                             lon="lon",
                             hover_name="Commune",
                             size="Surface brûlée (ha)",
                             color="Surface brûlée (ha)",
                             color_continuous_scale="amp",
                             mapbox_style="carto-positron",
                             zoom=4,
                             center={"lat": 47.0, "lon": 3.0},
                             labels={"Surface brûlée (ha)": f"Surface brûlée (ha) en {year}"},
                             width=700)

display_year3(2017)
