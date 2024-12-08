import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor

import pandas
import requests


def get_meta(response):
    try:
        root = ET.fromstring(response.text)
        indicator = root.find("indicator")
        data = {
            # "extraction_date": root.find('extraction_date').text,
            # "language": root.find('language').text,
            # "indicator_id": indicator.attrib['id'],
            "theme": indicator.find('theme').text,
            "subtheme": indicator.find('subtheme').text,
            # "keywords": indicator.find('keywords').text,
            "varcd": indicator.find("varcd").text,
            "title": indicator.find("title").text,
            "last_update": indicator.find("dates/last_update").text,
            "geo_lastlevel": indicator.find("geo_lastlevel").text,
            "last_period_available": indicator.find("dates/last_period_available").text,
            "periodicity": indicator.find("periodicity").text.strip(),
            "update_type": indicator.find("update_type").text,
            # "description": indicator.find('description').text.strip(),
            # "source": indicator.find("source").text,
            # "bdd_url": indicator.find('html/bdd_url').text,
            # "metainfo_url": indicator.find('html/metainfo_url').text,
            # "json_dataset": indicator.find('json/json_dataset').text.strip(),
            # "json_metainfo": indicator.find('json/json_metainfo').text.strip()
        }
        return data
    except Exception:
        return None


def fetch_data(i):
    url = "https://www.ine.pt/ine/xml_indic.jsp?opc=1&varcd={}&lang=PT"
    try:
        return requests.get(url.format(str(i).zfill(7)))

    except requests.RequestException:
        return None


indicator_ids = range(1, 15000)

with ThreadPoolExecutor(max_workers=50) as executor:
    results = list(executor.map(fetch_data, indicator_ids))

inds = [
    m
    for result in results
    if result is not None and ((m := get_meta(result)) is not None)
]

df = pandas.DataFrame.from_records(inds)
df.to_csv("indicadores_todos.csv", index=False)
df.to_excel("indicadores_todos.xlsx", index=False)
