from kube_formatter import make_template, BASE_DIR
from template_vals import *
from os.path import abspath, dirname, isfile, join

PROJECT_DIR = join(BASE_DIR, 'project-output', 'isi_tworavens')

def make_isi_project():

    kube_file_name = 'tworavens_isi_same_node.yml'

    deploy_dict = ISI_DEPLOY_DICT
    deploy_dict['kube_file_name'] = kube_file_name
    deploy_dict['TA2_IMAGE_NAME'] = deploy_dict[ISI_TA2_IMAGE_KEY]
    deploy_dict['TA3_IMAGE_NAMES'] = \
        [ISI_DEPLOY_DICT[k] for k in TA3_IMAGE_NAME_KEYS]

    for k, v in deploy_dict.items():
        print (k, v)

    # deploy pod.yml
    #
    make_template(deploy_dict,
                  'tmpl_tworavens_isi_same_node.yml',
                  join(PROJECT_DIR, kube_file_name))

    # readme
    #
    make_template(deploy_dict,
                  'tmpl_README.md',
                  join(PROJECT_DIR, 'README.md'))

    # retag list for local testing
    tag_info = {'TAG_PAIRS' : get_isi_tag_pairs(),
                'blah' : 'hi'}
    #print('tag_info', tag_info)

    make_template(tag_info,
                  'tmpl_image_retag2.md',
                  join(PROJECT_DIR, 'dev_notes/image_retag.md'))

    make_template(tag_info,
                  'tmpl_docker_tag_push.py',
                  join(PROJECT_DIR, 'dev_notes/docker_tag_push.py'))

if __name__ == '__main__':
    make_isi_project()
