# TA3 - Submission Component 2: Docker Images

The images used for this test may be found at the following locations:

## TA3 Images
{% for img_name in TA3_IMAGE_NAMES %}
 - {{ img_name }}{% endfor %}

## TA2 Image

 - {{ TA2_IMAGE_NAME}}

## pull commands

```
# TA3 Images
{% for img_name in TA3_IMAGE_NAMES %}
docker pull {{ img_name }}{% endfor %}

# TA2 Image
docker pull {{ TA2_IMAGE_NAME}}
```
