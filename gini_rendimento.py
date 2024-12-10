import pandas as pd
import requests

query_base = "https://www.ine.pt/ine/json_indicador/pindica.jsp?op=2"
query_meta_base = "https://www.ine.pt/ine/json_indicador/pindicaMeta.jsp?"
SPATIAL = "<*>2"  # <*>1 Continente; <*>2 RAA; <*>3 RAM;
LANG = "PT"
TEMPORAL = "S7A2022"

# Valor mediano do rendimento bruto declarado por sujeito passivo
mediano_bruto = "0012749"
# Rendimento bruto declarado por sujeito passivo
medio_bruto = "0012748"
# Coeficiente de Gini do rendimento bruto declarado por sujeito passivo
gini = "0012753"


def df_build(code) -> pd.DataFrame:
    query = f"{query_base}&varcd={code}&Dim1={TEMPORAL}&Dim2={SPATIAL}&lang={LANG}"
    raw_data = requests.get(query)
    dados = raw_data.json()[0]["Dados"]
    x = []
    for year, data in dados.items():
        for obs_dict in data:
            if valor := obs_dict.get("valor", None):
                x.append(
                    (year, obs_dict.get("geocod"), obs_dict["geodsg"], float(valor))
                )

    return (
        pd.DataFrame.from_records(x, columns=["year", "geocod", "zone", "val"])
        .set_index("geocod")
        .drop(["year"], axis=1)
    )


df_gini = df_build(gini).rename(columns={"val": "gini"})
df_mediano = df_build(mediano_bruto).rename(columns={"val": "rendimento_bruto_mediano"})
df_medio = df_build(medio_bruto).rename(columns={"val": "rendimento_bruto_medio"})

df = (
    df_gini.join(df_medio, how="outer", rsuffix="rm")
    .join(df_mediano, how="outer", rsuffix="rmm")
    .drop(axis=1, labels=["zonerm", "zonermm"])
    .dropna()
)

df.to_excel("raa_gini_rendimento.xlsx")
