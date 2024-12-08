# INE

WIP.
Take a look at `ine_api_showcase.ipynb` for a hands-on HOWTO.

Existem mais de 14 000 indicadores (2024-12-08). Existe também uma lista de cerca de 300 [principais indicadores](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_princindic), curada pelo próprio INE. O módulo `smi` trata de atualizar a lista dos principais indicadores e criar uma spreadsheet/csv com os últimos updates.

## URLs

- [__Instruções INE__](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_api&INST=322751522&xlang=pt)
- [__Lista indicadores__](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_base_dados&contexto=bd&selTab=tab2&xlang=pt)
- [__Sistema de Metainformação__](https://smi.ine.pt/)

## INE API HOWTO

### Descrição (XML)

- __<https://www.ine.pt/ine/xml_indic.jsp?opc=3>__ : indicadores principais
- __...?opc=1&varcd={varcd_cod}__ : único indicador
  - __eg: <https://www.ine.pt/ine/xml_indic.jsp?opc=1&varcd=0012757>__

### Extração

#### Dados

```{text}
{host_url}/ine/json_indicador/pindica.jsp?op=2&varcd={varcd_cod}&Dim1={dim1_cod}&Dim2={dim2_cod}&Dim??={dim??_cod}&lang={lang}
```

#### Metainfo

```{text}
{host_url}/ine/json_indicador/pindicaMeta.jsp?varcd={varcd_cod}&lang={lang}
```

## PDFs do INE com instruções

- [API - Catálogo de Indicadores do INE na Base de Dados](https://www.ine.pt/ngt_server/attachfileu.jsp?look_parentBoui=322788851&att_display=n&att_download=y)

- [Dados de Indicadores – Base de Dados](https://www.ine.pt/ngt_server/attachfileu.jsp?look_parentBoui=322762582&att_display=n&att_download=y)
