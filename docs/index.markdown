---
layout: home
---
# INE-helper

Trabalhar os dados do INE pode ser complexo. O objectivo deste site é que seja menos.

Todo o código pode ser encontrado em [https://github.com/fmesqg/ine](https://github.com/fmesqg/ine).


## Análises
{% assign analyses = site.analyses | sort: "date" | reverse %}
{% for analysis in analyses limit:20 %}

[{{ analysis.date | date_to_string }} - {{ analysis.title }}]({{ analysis.baseurl }}{{ analysis.url | relative_url }})

{% endfor %}

## Auto-updates
### Todos os indicadores [aqui](/assets/ine_indicadores.csv).

### RSS
- [RSS aqui]({{ site.url }}/ine/feed.xml)
- Para instruções sobre como seguir _feeds_ RSS, vê, _e.g._ [este tutorial](https://açores.net/rsss).

### Versão web
{% assign daily_updates = site.ine_updates | sort: "date" | reverse %}
{% for analysis in daily_updates limit:20 %}
* [{{ analysis.title }}]({{ analysis.baseurl }}{{ analysis.url | relative_url }})
{% endfor %}