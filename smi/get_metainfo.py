import xml.etree.ElementTree as ET

import pandas as pd
import requests


def get_metainfo_df():
    xml = requests.get("https://www.ine.pt/ine/xml_indic.jsp?opc=3&lang=PT")
    root = ET.fromstring(xml.text)
    indicator_data = []
    for indicator in root.findall("indicator"):
        data = {
            # "extraction_date": root.find('extraction_date').text,
            # "language": root.find('language').text,
            # "indicator_id": indicator.attrib['id'],
            # "theme": indicator.find('theme').text,
            # "subtheme": indicator.find('subtheme').text,
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
        indicator_data.append(data)

    df = pd.DataFrame(indicator_data)
    df["last_update"] = pd.to_datetime(df["last_update"], format="%d-%m-%Y")
    return df
