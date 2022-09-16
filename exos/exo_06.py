# coding: utf-8

# Surface brûlée par année, par département
df = (bdiff.groupby(["Année", "Département", "Commune"], as_index=False)["Surface brûlée (ha)"]
      .sum()
     )

(px.treemap(data_frame=df,
           values="Surface brûlée (ha)",
           path=["Année", "Département"],
           title="Surface brûlée par année et par département en ha")
).show()

# Surface brûlée par année, par commune
df = (bdiff.groupby(["Année"], as_index=False)
      .apply(lambda g: g.nlargest(10, "Surface brûlée (ha)"))
      .groupby(["Année", "Département", "Commune"], as_index=False)["Surface brûlée (ha)"]
      .sum()
     )

px.treemap(data_frame=df,
           values="Surface brûlée (ha)",
           path=["Année", "Commune"],
           title="Surface brûlée par année et par commune en ha")
