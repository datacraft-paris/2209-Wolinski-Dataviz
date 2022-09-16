# coding: utf-8

# Surface brûlée par an
mean_ = bdiff.groupby("Année")["Surface brûlée (ha)"].sum().mean()

df = (bdiff.groupby("Année")["Surface brûlée (ha)"]
      .sum()
      .rename("Surface brûlée par an")
     )

(px.bar(data_frame=df,
        title="Surface brûlée par an en ha",
        labels={"value":"", "variable":""})
 .add_hline(y=mean_)
)
