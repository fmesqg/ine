from datetime import datetime, timedelta
import xml.etree.ElementTree as ET

import pandas as pd
import requests


def get_varcd_to_last_update() -> dict:
    xml = requests.get("https://www.ine.pt/ine/xml_indic.jsp?opc=3&lang=PT")
    root = ET.fromstring(xml.text)
    return {
        indicator.find("varcd").text: {
            "last_update": indicator.find("dates/last_update").text,
            "title": indicator.find("title").text,
            "geo_lastlevel": indicator.find("geo_lastlevel").text,
            "last_period_available": indicator.find("dates/last_period_available").text,
            "periodicity": indicator.find("periodicity").text.strip(),
            "update_type": indicator.find("update_type").text,
        }
        for indicator in root.findall("indicator")
    }


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
                # "source": indicator.find("source").text,
                # "bdd_url": indicator.find('html/bdd_url').text,
                # "metainfo_url": indicator.find('html/metainfo_url').text,
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


if __name__ == "__main__":
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
        "Cookie": "ASP.NET_SessionId=c11mbqnr1exxc5e4ckivlslu",  # Be cautious with session cookies
    }
    x = requests.get("https://smi.ine.pt/Indicador/Exportacao?tipo=1", headers=headers)
    root = ET.fromstring(x.text)
    lst = [
        [z.text for z in x.findall("Coluna")][:6]
        for a in root.findall("ResultadosPesquisa")
        for x in a.findall("Resultado")
    ]
    df = pd.DataFrame.from_records(
        lst, columns=["cod_smi", "description", "portal", "var_cod", "x", "last_update"]
    )
    df["last_update"] = pd.to_datetime(df["last_update"], format="%d-%m-%Y")
    df["var_cod"] = pd.to_numeric(df["var_cod"])
    df.set_index("var_cod")
    df.sort_values(by=["last_update"], inplace=True, ascending=False)
    updated_yesterday = df.loc[
        df["last_update"] >= datetime.today() - timedelta(days=2), "description"
    ]
    for varcod, desc in updated_yesterday.items():
        print(varcod, desc)
