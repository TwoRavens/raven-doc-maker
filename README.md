This repository contains the TA3 submission for TwoRavens and ISI.

Within the repository are the 3 components according to the TA3 Submission Guide.

### Submission Component 1: meta.json file

The **component-1 directory** of this repository contains the [meta.json file](https://gitlab.datadrivendiscovery.org/tworavens/ISI-TwoRavens/blob/master/component-1/meta.json)

### Submission Component 2: Docker images

The **component-2 directory** contains a [list of docker images](https://gitlab.datadrivendiscovery.org/tworavens/ISI-TwoRavens/blob/master/component-2/docker_images.md) as well as their pull commands.

### Submission Component 3: Kubernetes config file

The **component-3 directory** contains the [Kubernetes config file](https://gitlab.datadrivendiscovery.org/tworavens/ISI-TwoRavens/blob/master/component-3/tworavens_isi_same_node.yml).
This config file contains references to the images listed in Component 2.

Note: As specified in the submission guide, the file contains Jinja style template references to `{{ eval_id }}`.
In addition, there is a similar reference for the **CONFIG_JSON_PATH** environment variable value, referenced as: `{{ CONFIG_JSON_PATH }}`


### Note on the ta3_search command

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
