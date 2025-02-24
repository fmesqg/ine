from ine_api import get_df

params_base = {
    "Dim2": "<*>2",  # <*>1 Continente; <*>2 RAA; <*>3 RAM;
    "lang": "PT",
    "Dim1": "S7A2022",
}
params_rendimento_mediano_bruto = {
    **params_base,
    "varcd": "0012749",
}
params_rendimento_medio_bruto = {
    **params_base,
    "varcd": "0012748",
}

params_gini = {
    **params_base,
    "varcd": "0012753",
}


df_gini = (
    get_df(params_gini).rename(columns={"valor": "gini"}).set_index("geocod")
)
df_mediano = (
    get_df(params_rendimento_mediano_bruto)
    .rename(columns={"valor": "rendimento_bruto_mediano"})
    .set_index("geocod")
)
df_medio = (
    get_df(params_rendimento_medio_bruto)
    .rename(columns={"valor": "rendimento_bruto_medio"})
    .set_index("geocod")
)

df = (
    df_gini[["geodsg", "gini"]]
    .join(
        df_medio[["rendimento_bruto_medio"]],
        how="outer",
    )
    .join(df_mediano[["rendimento_bruto_mediano"]], how="outer")
)
df.to_excel("raa_gini_rendimento.xlsx")
