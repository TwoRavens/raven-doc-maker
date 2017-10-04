# TA3 Submission: TwoRavens and CRA

This repository contains the TA3 submission for TwoRavens and Charles River Associates.

## Submission components

Within the repository are the 3 components according to the TA3 Submission Guide.

### Component 1: meta.json file

The `meta.json` file is at the top level of this repository: [meta.json file](https://gitlab.datadrivendiscovery.org/cTA2TA3/CRA_TwoRavens/blob/master/meta.json)


### Component 2: Docker images

The following docker images may be found in this repository:

- TA3 Images

  - registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/tworavens/nginx:latest
  - registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/tworavens:latest
  - registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/tworavens/rook-service:latest

- TA2 Image

  - registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/eve/docker-images:latest

- Pull commands

    ```
    # TA3 Images
    
    docker pull registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/tworavens/nginx:latest
    docker pull registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/tworavens:latest
    docker pull registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/tworavens/rook-service:latest

    # TA2 Image
    docker pull registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/eve/docker-images:latest
    ```

### Component 3: Kubernetes config file

The Kubernetes config file, [tworavens_cra_same_node.yml](https://gitlab.datadrivendiscovery.org/cTA2TA3/CRA_TwoRavens/blob/master/tworavens_cra_same_node.yml) maybe found at the top level of this repository.

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