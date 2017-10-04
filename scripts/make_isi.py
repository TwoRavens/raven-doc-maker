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
    print('tag_info', tag_info)

    make_template(tag_info,
                  'tmpl_image_retag2.md',
                  join(PROJECT_DIR, 'dev_notes/image_retag.md'))

    return
    # minikube pod.yml
    #
    make_template(MINIKUBE_DICT,
                  'tmpl_tworavens_isi_same_node.yml',
                  'test-minikube/tworavens_isi_test_node.yml')

    # image list for component-2
    #
    name_info = {'TA3_IMAGE_NAMES' : TA3_IMAGE_NAMES,
                 'TA2_IMAGE_NAME' : ISI_IMAGE_NAME}
    make_template(name_info,
                  'tmpl_image_list.md',
                  'component-2/image_list.md')

    # retag list for local testing
    tag_info = {'TAG_COMMANDS' : TAG_COMMANDS}
    make_template(tag_info,
                  'tmpl_image_retag.md',
                  'test-minikube/image_retag.md')


if __name__ == '__main__':
    make_isi_project()
