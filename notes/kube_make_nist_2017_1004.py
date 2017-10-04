# Replace {{ eval_id }} in the content
content = Template(content).render(eval_id=eval_id)
# Load all resources
resources = yaml.load_all(content)
    for res in resources:
    # Check resource's kind
    kind = res.get('kind')
    if kind not in kubeop.resource_kind_white_list:
        raise Exception("Unsupported kind {}".format(kind))
    # Check evalId label
    if utils.deep_get(res, 'metadata', 'labels', 'evalId') != eval_id:
        raise Exception("Incorrect metadata.labels.evalId")

    # find ta3main and ta2main containers
    pod, containers = None, []
    if kind == 'Pod':
        containers = utils.deep_get(res, 'spec', 'containers')
        pod = res
        pod['spec'].update(sec)
    elif kind == 'Deployment':
        containers = utils.deep_get(res, 'spec', 'template', 'spec', 'containers')
        pod = res['spec']['template']
        pod['spec'].update(sec)

    for c in containers:
        if c['name'] == 'ta2main':
            ta2_pod = pod
            ta2_main = c
            if utils.deep_get(pod, "metadata", "labels", "ta2main") != "yes":
                raise Exception("Error: TA2 main pod must have label 'ta2main: \"yes\"'")
        elif c['name'] == 'ta3main':
            if kind != 'Pod':
                raise Exception("Error: TA3 entry point has to be a Pod kind rather than {}".fo$
            if utils.deep_get(pod, "metadata", "labels", "ta3main") != "yes":
                raise Exception("Error: TA3 entry pod must have label 'ta3main: \"yes\"'")
            ta3_pod = pod
            ta3_main = c
    kobjs.append(res)

if not ta2_main or not ta3_main:
    raise Exception("Incorrect TA3 k8s file, ta3main or ta2main container does not exist")

if ta2_pod is not ta3_pod:
    # Ta2 and ta3 are NOT in the same pod
    # Add volumes to ta3 pod
    if not ta3_pod['spec'].get('volumes'):
        ta3_pod['spec']['volumes'] = []
    ta3_pod['spec']['volumes'].append(data_vol)

# Add volumes to ta2 pod
if not ta2_pod['spec'].get('volumes'):
    ta2_pod['spec']['volumes'] = []
ta2_pod['spec']['volumes'].extend([data_vol, shared_vol, store_vol])

# Add volume mounts to ta2 main container
if not ta2_main.get('volumeMounts'):
    ta2_main['volumeMounts'] = []
ta2_main['volumeMounts'].extend([redacted_data_mount, shared_mount])

# Add volume mounts to ta3 main container
if not ta3_main.get('volumeMounts'):
    ta3_main['volumeMounts'] = []
ta3_main['volumeMounts'].extend([redacted_data_mount])

# Add scorer container to ta2 pod
ta2_pod['spec']['containers'].append(scorer)
# Add volume mounts to scorer container
scorer['volumeMounts'].extend([data_mount, shared_mount, store_mount])
# Add volumes to ta2 pod
if not ta2_pod['spec'].get('volumes'):
    ta2_pod['spec']['volumes'] = []
ta2_pod['spec']['volumes'].extend([data_vol, shared_vol, store_vol])

# Add volume mounts to ta2 main container
if not ta2_main.get('volumeMounts'):
    ta2_main['volumeMounts'] = []
ta2_main['volumeMounts'].extend([redacted_data_mount, shared_mount])

# Add volume mounts to ta3 main container
if not ta3_main.get('volumeMounts'):
    ta3_main['volumeMounts'] = []
ta3_main['volumeMounts'].extend([redacted_data_mount])

# Add scorer container to ta2 pod
ta2_pod['spec']['containers'].append(scorer)
# Add volume mounts to scorer container
scorer['volumeMounts'].extend([data_mount, shared_mount, store_mount])

# Add environment variables and inject config file data
search_env = {
    'name': 'CONFIG_JSON_PATH',
    'value': path/to/config/file
}

ta3_main['env'].append(search_env)
ta2_main['env'].append(search_env)
