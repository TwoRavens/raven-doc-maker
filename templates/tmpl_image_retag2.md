
# Retag the pulled docker images for use in this repo
{% for tpair in TAG_PAIRS %}
### Image {{ loop.index }}

```
# pull image
docker pull {{ tpair[0] }}

# tag image
docker tag {{ tpair[0] }} {{ tpair[1] }}

# push image
docker push {{ tpair[1] }}
```
{% endfor %}
