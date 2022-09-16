# coding: utf-8

# Comparaison du nombre d'incendies par an
df = (pd.concat([bdiff.groupby("Année").size(),
                 promethee.groupby("Année").size()],
                axis=1)
      .rename(columns={0:"BDIFF", 1:"Prométhée"})
     )

px.bar(data_frame=df,
       y=["BDIFF", "Prométhée"],
       barmode="group",
       title="Nombre d'incendies par an",
       labels={"value":"", "variable":""})
