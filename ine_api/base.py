import pandas as pd
import requests
import seaborn as sns

query_base = "https://www.ine.pt/ine/json_indicador/pindica.jsp?op=2"


def get_df(input_dict: dict):
    query_params = "&".join([f"{k}={v}" for k, v in input_dict.items()])
    query = f"{query_base}&{query_params}"
    raw_data = requests.get(query)
    dados = raw_data.json()[0]["Dados"]
    data = []
    columns = []
    for year, year_data in dados.items():
        if not columns:
            columns = list(dict.fromkeys(key for x in year_data for key in x))
        for obs_dict in year_data:
            data.append((year,) + tuple(obs_dict.get(key, None) for key in columns))
    df = pd.DataFrame.from_records(data, columns=["ano"] + columns)
    df["valor"] = pd.to_numeric(df["valor"])
    return df


def default_plot(*, title, df: pd.DataFrame):
    df_plot = df.drop_duplicates().pivot(index="ano", columns="geodsg", values="valor")
    ax = sns.lineplot(data=df_plot, palette="tab10", linewidth=2.5)
    ax.set(title=title)
    sns.move_legend(ax, bbox_to_anchor=(1.05, 1), loc="upper left")
