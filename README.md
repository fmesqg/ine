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

## Indicadores interessantes

(Note to self: opta por [sujeitos passivos](https://smi.ine.pt/Conceito/Detalhes/10864) _vs_ [agregado familiar](https://smi.ine.pt/Conceito/Detalhes/1474))

### Condições de vida e cidadania

#### Rendimentos e condições de vida

##### NUTS II

##### Município

- [Agregados fiscais (N.º) por Localização geográfica (NUTS - 2024) e Escalões de rendimento bruto declarado; Anual](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod=0012673&contexto=bd&selTab=tab2)

- [Agregados fiscais (N.º) por Localização geográfica (NUTS - 2024) e Escalões de rendimento bruto declarado deduzido do IRS Liquidado; Anual](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod=0012742&contexto=bd&selTab=tab2)

##### Freguesia

- [Desigualdade na distribuição do rendimento bruto declarado dos agregados fiscais (P80/P20 - N.º) por Localização geográfica (freg); Anual](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod=0012716&contexto=bd&selTab=tab2)
- [Desigualdade na distribuição do rendimento bruto declarado dos agregados fiscais (P90/P10 - N.º) por Localização geográfica (freg); Anual](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod=0012717&contexto=bd&selTab=tab2)

- [Distribuição do rendimento bruto declarado deduzido de IRS liquidado dos agregados fiscais (€) por Localização geográfica (NUTS - 2024) e Quintis de rendimento; Anual](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod=0012743&contexto=bd&selTab=tab2)

#### Privação

##### NUTS II

- [Taxa de privação material e social (%) por Local de residência (NUTS - 2013); Anual](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod=0011593&contexto=bd&selTab=tab2)
- [Taxa de privação material e social severa (%) por Local de residência (NUTS - 2013); Anual](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod=0011594&contexto=bd&selTab=tab2)
- [Taxa de privação severa das condições da habitação (%) por Local de residência (NUTS - 2013) e Tipologia de áreas urbanas; Anual](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod=0006259&contexto=bd&selTab=tab2)
- [Proporção da população residente (%) por Local de residência (NUTS - 2013) e Itens de privação material e social; Anual](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod=0011731&contexto=bd&selTab=tab2)

###### Habitação

- [Carga mediana das despesas em habitação (%) por Local de residência (NUTS - 2013) e Tipologia de áreas urbanas; Anual](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod=0006256&contexto=bd&selTab=tab2)
- [Taxa de sobrelotação da habitação (%) por Local de residência (NUTS - 2013) e Tipologia de áreas urbanas; Anual](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod=0006261&contexto=bd&selTab=tab2)
- [Taxa de sobrecarga das despesas em habitação (%) por Local de residência (NUTS - 2013) e Tipologia de áreas urbanas; Anual](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod=0006260&contexto=bd&selTab=tab2)

#### Pobreza e desigualdade económica (TODO)
