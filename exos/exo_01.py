# coding: utf-8

# Nombre d'incendies par an
df = (bdiff.groupby("Année")
      .size()
      .rename("Nombre d'incendies")
     )

px.bar(data_frame=df,
       title="Nombre d'incendies par an",
       labels={"value":"", "variable":""})
