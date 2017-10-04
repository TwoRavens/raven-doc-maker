"""
Create kubernetes files based on templates
"""
from os.path import abspath, dirname, isfile, join
from jinja2 import Template
import sys
from template_vals import *

"""
from jinja2 import Template
c =  'evalId: {{ eval_id }}'
t = Template(c)
info = dict(eval_id='frog')
t.render(info)
t.render(eval_id='frog')
"""


BASE_DIR = dirname(dirname(abspath(__file__)))
TEMPLATE_DIR = join(BASE_DIR, 'templates')

def make_template(template_dict, template_name, rendered_filename):
    """Make a simple template and write it to the main directory"""
    assert template_dict, 'template_dict cannot be None'

    # open template
    #
    template_path = join(TEMPLATE_DIR, template_name)
    assert isfile(template_path), 'template not found: %s' % template_path

    template = Template(open(template_path, 'r').read())

    # create content
    #
    content = template.render(template_dict)

    # write file out
    #
    rendered_filepath = join(BASE_DIR, rendered_filename)
    open(rendered_filepath, 'w').write(content)
    print('template written: %s' % rendered_filepath)


if __name__ == '__main__':
    make_template(DEPLOY_DICT,
                  'tmpl_tworavens_isi_same_node.yml',
                  'component-3/tworavens_isi_same_node.yml')

    make_template(MINIKUBE_DICT,
                  'tmpl_tworavens_isi_same_node.yml',
                  'test-minikube/tworavens_isi_test_node.yml')

    name_info = {'TA3_IMAGE_NAMES' : TA3_IMAGE_NAMES,
                 'TA2_IMAGE_NAME' : ISI_IMAGE_NAME}

    make_template(name_info,
                  'tmpl_image_list.md',
                  'component-2/image_list.md')
