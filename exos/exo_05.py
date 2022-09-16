# coding: utf-8

# Surface brûlée par an en Méditerrannée par rapport à l'ensemble de la France
df = (promethee.groupby("Année")["Surface parcourue (ha)"].sum()
      .div(bdiff.groupby("Année")["Surface brûlée (ha)"].sum())
      .drop(2022)
      .rename("Surface brûlée en Méditerrannée")
     )

(px.bar(data_frame=df,
        title="% de surface brûlée en Méditerrannée",
        labels={"value":"", "variable":""})
 .update_layout(yaxis_tickformat=".0%")
)
