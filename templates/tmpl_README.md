# TA3 Submission: TwoRavens and ISI

This repository contains the TA3 submission for TwoRavens and ISI.

## Submission components

Within the repository are the 3 components according to the TA3 Submission Guide.

### Component 1: meta.json file

The `meta.json` file is at the top level of this repository: [meta.json file]({{ REPO_FILE_URL }}/meta.json)


### Component 2: Docker images

The following docker images may be found in this repository:

- TA3 Images
{% for img_name in TA3_IMAGE_NAMES %}
  - {{ img_name }}{% endfor %}

- TA2 Image

  - {{ TA2_IMAGE_NAME}}

- Pull commands

    ```
    # TA3 Images
    {% for img_name in TA3_IMAGE_NAMES %}
    docker pull {{ img_name }}{% endfor %}

    # TA2 Image
    docker pull {{ TA2_IMAGE_NAME}}
    ```

### Component 3: Kubernetes config file

The Kubernetes config file, [{{ kube_file_name }}]({{ REPO_FILE_URL }}/{{ kube_file_name }}) maybe found at the top level of this repository.

This config file contains references to the images listed in Component 2.

Note: As specified in the submission guide, the file contains Jinja style template references to the following variables:
  - `{{ eval_id }}`
  - `{{ CONFIG_JSON_PATH }}` in the form:
      ```
      env:
        - name: CONFIG_JSON_PATH
          value: "{{ CONFIG_JSON_PATH }}"
      ```

---

## ta3_search command

The ta3_search command to load a config file may be executed against the running `ta3-main` container.

The format for the command is:

#### Docker version

In this example, the container name is `ta3-main` which is also the reference in the kubernetes configuration file:

```
docker exec -ti ta3-main /bin/bash -c 'ta3_search $CONFIG_JSON_PATH'
```

#### Kubectl version

In this example, the pod name* is `raven-pod1` and the container name is `ta3-main`.  
(It is assumed that the pod name will change based on the eval_id.)

```
kubectl exec  -ti raven-pod1 --container ta3-main -- /bin/bash -c 'ta3_search $CONFIG_JSON_PATH'
```

Note: the '-ti' is not needed but gives better formatted output if the config has issues such as inaccessible paths.
