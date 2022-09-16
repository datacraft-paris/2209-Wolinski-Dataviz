# coding: utf-8

# Surfaces brûlées par an
(px.strip(data_frame=bdiff,
               x="Année",
               y="Surface brûlée (ha)",
               hover_name="Commune",
               title="Surfaces brûlées par an en ha")
 .add_hline(y=1000)
)
