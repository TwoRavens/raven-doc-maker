"""
Create kubernetes files based on templates
"""
from os.path import abspath, dirname, isfile, join
from jinja2 import Template
import sys

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

def make_template(template_dict, template_name):
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
    rendered_filepath = join(BASE_DIR, template_name)
    open(rendered_filepath, 'w').write(content)
    print('template written: %s' % rendered_filepath)


if __name__ == '__main__':
    make_template(dict(eval_id='eval-2ravens-isi'),
                  'tworavens_isi_same_node.yml')
