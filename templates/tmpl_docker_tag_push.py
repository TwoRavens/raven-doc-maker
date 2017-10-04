"""
Last minute script using serious hack
"""
import os

COMMAND_INFO = [\{% for tpair in TAG_PAIRS %}
    ('pull image {{ tpair[0] }}', 'docker pull {{ tpair[0] }}'),
    ('tag image  as "{{ tpair[0] }}"', 'docker tag {{ tpair[0] }} {{ tpair[1] }}'),
    ('push image {{ tpair[1] }}', 'docker push {{ tpair[1] }}'),
{% endfor %}]


def run_single_command(desc, cmd, cnt=None):
    print('---')
    if cnt:
        print('(%d) -> %s' % (cnt, desc))
    else:
        print('-> %s' % desc)
    os.system(cmd)

def run_docker_commands():
    cnt = 0
    for cpair in COMMAND_INFO:
        cnt += 1
        desc, cmd = cpair
        run_single_command(desc, cmd, cnt)

if __name__ == '__main__':
    run_docker_commands()
