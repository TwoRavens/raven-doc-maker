from config_fragments import RAVENS_ISI_VOLUME_MOUNTS

D3M_REGISTRY = 'registry.datadrivendiscovery.org'
TWORAVENS_REGISTRY = '%s/tworavens/tworavens' % D3M_REGISTRY

# Refers to containers in gitlab.datadrivendiscovery.org registries
#
ravens_nginx_image_key = 'ravens_nginx_image'
tworavens_image_key = 'tworavens_image'
rook_image_key = 'rook_image'
isi_ta2_image_key = 'isi_ta2_image'
cra_ta2_image_key = 'cra_ta2_image'

DEPLOY_DICT = {ravens_nginx_image_key : '%s/nginx:latest' % TWORAVENS_REGISTRY,
               tworavens_image_key : '%s/tworavens:latest' % TWORAVENS_REGISTRY,
               rook_image_key : '%s/rook-service:latest' % TWORAVENS_REGISTRY,
               # leave in for NIST
               'CONFIG_JSON_PATH' : '{{ CONFIG_JSON_PATH }}',
               'eval_id' : '{{ eval_id }}',
               # ISI specific
               isi_ta2_image_key : '%s/ta2/isi_ta2:python3' % D3M_REGISTRY,
               'RAVENS_ISI_VOLUME_MOUNTS' : RAVENS_ISI_VOLUME_MOUNTS,
               # CRA specific
               cra_ta2_image_key : '%s/eve/docker-images:latest' % D3M_REGISTRY}

# Using tags given to containers after download
#
MINIKUBE_DICT = {ravens_nginx_image_key : 'ravens_nginx:latest',
                 tworavens_image_key : 'tworavens:latest',
                 rook_image_key : 'rook:latest',
                 # Fill in
                 'CONFIG_JSON_PATH' : '/ravens_volume/config_o_196.json',
                 'eval_id' : 'ravens-eval',
                 # ISI specific
                 isi_ta2_image_key : 'isi_ta2:latest',
                 'RAVENS_ISI_VOLUME_MOUNTS' : RAVENS_ISI_VOLUME_MOUNTS,
                 # CRA specific
                 cra_ta2_image_key : 'cra_ta2:latest'}

TA3_IMAGE_NAME_KEYS = [ravens_nginx_image_key, tworavens_image_key, rook_image_key]
TA3_IMAGE_NAMES = [DEPLOY_DICT[k] for k in TA3_IMAGE_NAME_KEYS]

ISI_IMAGE_NAME = DEPLOY_DICT[isi_ta2_image_key]
CRA_IMAGE_NAME = DEPLOY_DICT[cra_ta2_image_key]

# docker pull commands
#
PULL_COMMANDS = ['docker pull %s' % (img_name)
                 for img_name in DEPLOY_DICT.values()]

# docker tag commands
#
TAG_COMMANDS = ['docker tag %s %s' % (DEPLOY_DICT[k], MINIKUBE_DICT[k])
                for k in DEPLOY_DICT]
