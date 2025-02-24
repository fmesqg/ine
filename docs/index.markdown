---
layout: home
---
# WIP

[RSS aqui]({{ site.url }}/ine/feed.xml)

## Análises
{% for analysis in site.analyses limit:20 %}

[{{ analysis.title }}]({{ analysis.baseurl }}{{ analysis.url | relative_url }})

{% endfor %}