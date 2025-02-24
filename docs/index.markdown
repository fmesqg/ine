---
layout: home
---
# TODO

É _checkar_ os RSSs, _innit_?

[aqui]({{ site.url }}/ine/feed.xml)

## Análises
{% for analysis in site.analyses limit:20 %}

[{{ analysis.title }}]({{ analysis.url }})

{% endfor %}