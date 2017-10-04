
# Retag the pulled docker images for use in this repo

```{% for tc in TAG_COMMANDS %}
# tag {{ loop.index }}
{{ tc }}
{% endfor %}
```
