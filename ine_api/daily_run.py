import xml.etree.ElementTree as ET
from datetime import datetime
import yaml
import pandas as pd
import requests


def get_metadata(response):
    try:
        root = ET.fromstring(response.text)
        indicator = root.find("indicator")
        return (
            indicator.find("varcd").text,
            {
                "theme": indicator.find("theme").text,
                "subtheme": indicator.find("subtheme").text,
                "keywords": indicator.find("keywords").text,
                "title": indicator.find("title").text,
                "last_update": indicator.find("dates/last_update").text,
                "geo_lastlevel": indicator.find("geo_lastlevel").text,
                "last_period_available": indicator.find(
                    "dates/last_period_available"
                ).text,
                "periodicity": indicator.find("periodicity").text.strip(),
                "update_type": indicator.find("update_type").text,
                "description": indicator.find("description").text.strip(),
                "json_dataset": indicator.find("json/json_dataset").text.strip(),
                "json_metainfo": indicator.find("json/json_metainfo").text.strip(),
            },
        )
    except Exception:
        return None


def fetch_data(i):
    url = "https://www.ine.pt/ine/xml_indic.jsp?opc=1&varcd={}&lang=PT"
    try:
        return requests.get(url.format(str(i).zfill(7)))

    except requests.RequestException:
        return None


def write_daily_update_to_yaml(var_cods_updated, date):
    data = {"date": day, "vars_updated": []}
    code_to_pt = {"N": "Novo", "A": "Atualizado", "D": "Disponível"}

    def write_md(json_entry: dict):
        return f"""* [{json_entry["title"]}]({json_entry["url"]})
  * [Metainfo]({json_entry["url_meta"]})
  * Nível geográfico: {json_entry["geo_lastlevel"]}
  * Tema: {json_entry["theme"]}
  * Subtema: {json_entry["subtheme"]}
  * Descrição: {json_entry["description"]}
  * Último _update_: {json_entry["last_update"]}
  * Tipo de _update_: {code_to_pt.get(json_entry["update_type"], json_entry["update_type"])}

"""

    for var_cod in var_cods_updated:
        json = get_metadata(fetch_data(var_cod))
        if json:
            entry = {
                "var_cod": var_cod,
                "title": json[1].get("title"),
                "theme": json[1].get("theme"),
                "subtheme": json[1].get("subtheme"),
                "description": json[1].get("description"),
                "update_type": json[1].get("update_type"),
                "geo_lastlevel": json[1].get("geo_lastlevel"),
                "last_update": json[1].get("last_update"),
                "url": f"https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod={str(var_cod).zfill(7)}&contexto=bd&selTab=tab2",
                "url_meta": f"https://www.ine.pt/bddXplorer/htdocs/minfo.jsp?var_cd={str(var_cod).zfill(7)}&lingua=PT",
            }
            data["vars_updated"].append(entry)

    if data["vars_updated"]:
        with open(f"docs/_ine_updates/{date}.md", "w") as file:
            # --- around the yaml needed for jekyll
            file.write("---\n")
            yaml.dump(data, file, default_flow_style=False, allow_unicode=True)
            file.write("---\n")
            [file.write(write_md(x)) for x in data["vars_updated"]]
        print(f"YAML file '{date}.yaml' written successfully.")
    print(f"Checked {date} successfully.")


def get_indicador_df():
    headers = {
        "Host": "smi.ine.pt",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Referer": "https://smi.ine.pt/Indicador?clear=True",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Sec-GPC": "1",
        "Priority": "u=0, i",
    }
    x = requests.get("https://smi.ine.pt/Indicador/Exportacao?tipo=1", headers=headers)
    root = ET.fromstring(x.text)
    lst = [
        [z.text for z in x.findall("Coluna")][:6]
        for a in root.findall("ResultadosPesquisa")
        for x in a.findall("Resultado")
    ]
    return pd.DataFrame.from_records(
        lst,
        columns=[
            "cod_smi",
            "description",
            "portal",
            "var_cod",
            "x",
            "last_update",
        ],
    )


if __name__ == "__main__":
    try:
        df = get_indicador_df()
    except Exception:
        print("error getching indicator data")
    else:
        for day in [datetime.today().strftime("%Y-%m-%d")]:
        # for day in [f"2025-01-{str(day).zfill(2)}" for day in range(1, 24)]: # retro-trick
            ddmmyyyy_day = datetime.strptime(day, "%Y-%m-%d").strftime("%d-%m-%Y")
            df["last_update_datetime"] = pd.to_datetime(
                df["last_update"], format="%d-%m-%Y"
            )

            updated_yesterday = df.loc[df["last_update"] == ddmmyyyy_day]
            write_daily_update_to_yaml(
                [var_cod for var_cod in updated_yesterday["var_cod"]],
                date=day,
            )
