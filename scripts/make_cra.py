from kube_formatter import make_template, BASE_DIR
from template_vals import *
from os.path import abspath, dirname, isdir, isfile, join
import os

PROJECT_DIR = join(BASE_DIR, 'project-output', 'cra_tworavens')
PROJECT_DEV_NOTE_DIR = join(PROJECT_DIR, 'dev_notes')
if not isdir(PROJECT_DEV_NOTE_DIR):
    os.makedirs(PROJECT_DEV_NOTE_DIR)

def make_cra_project():

    kube_file_name = 'tworavens_cra_same_node.yml'

    deploy_dict = CRA_DEPLOY_DICT
    deploy_dict['kube_file_name'] = kube_file_name
    deploy_dict['TA2_IMAGE_NAME'] = deploy_dict[CRA_TA2_IMAGE_KEY]
    deploy_dict['TA3_IMAGE_NAMES'] = \
        [CRA_DEPLOY_DICT[k] for k in TA3_IMAGE_NAME_KEYS]

    # deploy pod.yml
    #
    make_template(deploy_dict,
                  'tmpl_tworavens_cra_same_node.yml',
                  join(PROJECT_DIR, kube_file_name))

    # readme
    #
    make_template(deploy_dict,
                  'tmpl_README.md',
                  join(PROJECT_DIR, 'README.md'))

    # retag list for local testing
    tag_info = {'TAG_PAIRS' : get_cra_tag_pairs()}

    make_template(tag_info,
                  'tmpl_image_retag2.md',
                  join(PROJECT_DEV_NOTE_DIR, 'image_retag.md'))

    make_template(tag_info,
                  'tmpl_docker_tag_push.py',
                  join(PROJECT_DEV_NOTE_DIR, 'docker_tag_push.py'))


if __name__ == '__main__':
    make_cra_project()
