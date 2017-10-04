from config_fragments import RAVENS_ISI_VOLUME_MOUNTS

D3M_REGISTRY = 'registry.datadrivendiscovery.org'
TWORAVENS_REGISTRY = '%s/tworavens' % D3M_REGISTRY

ISI_REGISTRY = 'registry.datadrivendiscovery.org/cta2ta3/isi_tworavens'
ISI_REPO_FILE_URL = 'https://gitlab.datadrivendiscovery.org/cTA2TA3/ISI_TwoRavens/blob/master'

# Refers to containers in gitlab.datadrivendiscovery.org registries
#
RAVENS_NGINX_IMAGE_KEY = 'ravens_nginx_image'
TWORAVENS_IMAGE_KEY = 'tworavens_image'
ROOK_IMAGE_KEY = 'rook_image'
ISI_TA2_IMAGE_KEY = 'isi_ta2_image'
CRA_TA2_IMAGE_KEY = 'cra_ta2_image'

DEPLOY_DICT = {RAVENS_NGINX_IMAGE_KEY : '%s/tworavens/nginx:latest' % TWORAVENS_REGISTRY,
               TWORAVENS_IMAGE_KEY : '%s/tworavens:latest' % TWORAVENS_REGISTRY,
               ROOK_IMAGE_KEY : '%s/tworavens/rook-service:latest' % TWORAVENS_REGISTRY,
               # leave in for NIST
               'CONFIG_JSON_PATH' : '{{ CONFIG_JSON_PATH }}',
               'eval_id' : '{{ eval_id }}',
               # ISI specific
               ISI_TA2_IMAGE_KEY : '%s/ta2/isi_ta2:python3' % D3M_REGISTRY,
               'RAVENS_ISI_VOLUME_MOUNTS' : RAVENS_ISI_VOLUME_MOUNTS,
               # CRA specific
               CRA_TA2_IMAGE_KEY : '%s/eve/docker-images:latest' % D3M_REGISTRY}

ISI_DEPLOY_DICT = {\
        RAVENS_NGINX_IMAGE_KEY : '%s/tworavens/nginx:latest' % ISI_REGISTRY,
        TWORAVENS_IMAGE_KEY : '%s/tworavens:latest' % ISI_REGISTRY,
        ROOK_IMAGE_KEY : '%s/tworavens/rook-service:latest' % ISI_REGISTRY,
        'REPO_FILE_URL' : ISI_REPO_FILE_URL,
        'IS_DEPLOY' : True,
        # leave in for NIST
        'CONFIG_JSON_PATH' : '{{ CONFIG_JSON_PATH }}',
        'eval_id' : '{{ eval_id }}',
        # ISI specific
        ISI_TA2_IMAGE_KEY : '%s/ta2/isi_ta2:python3' % ISI_REGISTRY,
       'RAVENS_ISI_VOLUME_MOUNTS' : RAVENS_ISI_VOLUME_MOUNTS,
               }

def get_isi_tag_pairs():
    #isi_dict = DEPLOY_DICT

    #for k in (TA3_IMAGE_NAME_KEYS + [ISI_TA2_IMAGE_KEY]):
    #    isi_dict[k]
    return [[DEPLOY_DICT[k], ISI_DEPLOY_DICT[k]]
            for k in TA3_IMAGE_NAME_KEYS + [ISI_TA2_IMAGE_KEY]]

    tag_commands = ['docker tag {0} {1}\n# push\ndocker push {1}'.format(\
                    DEPLOY_DICT[k], ISI_DEPLOY_DICT[k])
                    for k in (TA3_IMAGE_NAME_KEYS + [ISI_TA2_IMAGE_KEY])]

    return tag_commands



# Using tags given to containers after download
#
MINIKUBE_DICT = {RAVENS_NGINX_IMAGE_KEY : 'ravens_nginx:latest',
                 TWORAVENS_IMAGE_KEY : 'tworavens:latest',
                 ROOK_IMAGE_KEY : 'rook:latest',
                 # Fill in
                 'CONFIG_JSON_PATH' : '/ravens_volume/config_o_196.json',
                 'eval_id' : 'ravens-eval',
                 # ISI specific
                 ISI_TA2_IMAGE_KEY : 'isi_ta2:latest',
                 'RAVENS_ISI_VOLUME_MOUNTS' : RAVENS_ISI_VOLUME_MOUNTS,
                 # CRA specific
                 CRA_TA2_IMAGE_KEY : 'cra_ta2:latest'}


TA3_IMAGE_NAME_KEYS = [RAVENS_NGINX_IMAGE_KEY, TWORAVENS_IMAGE_KEY, ROOK_IMAGE_KEY]
TA3_IMAGE_NAMES = [DEPLOY_DICT[k] for k in TA3_IMAGE_NAME_KEYS]

ISI_IMAGE_NAME = DEPLOY_DICT[ISI_TA2_IMAGE_KEY]
CRA_IMAGE_NAME = DEPLOY_DICT[CRA_TA2_IMAGE_KEY]

# For testing, use the real images names
#for rave_img in TA3_IMAGE_NAME_KEYS:
#    MINIKUBE_DICT[rave_img] = DEPLOY_DICT[rave_img]
#MINIKUBE_DICT[ISI_TA2_IMAGE_KEY] = DEPLOY_DICT[ISI_TA2_IMAGE_KEY]
#MINIKUBE_DICT[CRA_TA2_IMAGE_KEY] = DEPLOY_DICT[CRA_TA2_IMAGE_KEY]

# docker pull commands
#
PULL_COMMANDS = ['docker pull %s' % (img_name)
                 for img_name in DEPLOY_DICT.values()]

# docker tag commands
#
TAG_COMMANDS = ['docker tag {0} {1}\n# push\ndocker push {1}'.format(\
                DEPLOY_DICT[k], MINIKUBE_DICT[k])
                for k in TA3_IMAGE_NAME_KEYS + [ISI_TA2_IMAGE_KEY] + [CRA_TA2_IMAGE_KEY]]
