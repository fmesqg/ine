from .get_metainfo import get_metainfo_df

df = get_metainfo_df()
df.sort_values(by=["last_update"], inplace=True, ascending=False)
df.to_excel(
    "indicadores_principais.xlsx",
    index=False,
)
df.to_csv(
    "indicadores_principais.csv",
    index=False,
)