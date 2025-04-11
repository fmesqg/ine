# INE API

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

## email

```{text}
Caro/a Utilizador/a,
Francisco

Agradecemos o seu pedido n.º PED-684641526.

No seguimento do esclarecimento efetuado, informamos:

Com a sinalética <*> na dim2 exemplo: Dim2=<*>??????? , retorna o DataSet com todos os dados que estejam incluídos naquela geografia indicada.

Aproveito para adicionar um esclarecimento que pode ser útil.

Caso pretenda mais que um período de cada vez. Usando para isso o separador "," exemplo: Dim1=S7A2021,S7A2021 ou todos os disponíveis Dim1=T

https://www.ine.pt/ine/json_indicador/pindica.jsp?op=2&varcd=0012757&Dim1=S7A2021,S7A2022&Dim2=<*>2004203&lang=PT

https://www.ine.pt/ine/json_indicador/pindica.jsp?op=2&varcd=0012757&Dim1=T&Dim2=<*>2004203&lang=PT

Colocamo-nos ao V. dispor para eventuais esclarecimentos.
Com os nossos cumprimentos, 

Apoio ao Utilizador

```
