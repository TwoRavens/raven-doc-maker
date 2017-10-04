"""
Last minute script using serious hack
"""
import os

COMMAND_INFO = [\
    ('pull image registry.datadrivendiscovery.org/tworavens/tworavens/nginx:latest', 'docker pull registry.datadrivendiscovery.org/tworavens/tworavens/nginx:latest'),
    ('tag image  as "registry.datadrivendiscovery.org/tworavens/tworavens/nginx:latest"', 'docker tag registry.datadrivendiscovery.org/tworavens/tworavens/nginx:latest registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/tworavens/nginx:latest'),
    ('push image registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/tworavens/nginx:latest', 'docker push registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/tworavens/nginx:latest'),

    ('pull image registry.datadrivendiscovery.org/tworavens/tworavens:latest', 'docker pull registry.datadrivendiscovery.org/tworavens/tworavens:latest'),
    ('tag image  as "registry.datadrivendiscovery.org/tworavens/tworavens:latest"', 'docker tag registry.datadrivendiscovery.org/tworavens/tworavens:latest registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/tworavens:latest'),
    ('push image registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/tworavens:latest', 'docker push registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/tworavens:latest'),

    ('pull image registry.datadrivendiscovery.org/tworavens/tworavens/rook-service:latest', 'docker pull registry.datadrivendiscovery.org/tworavens/tworavens/rook-service:latest'),
    ('tag image  as "registry.datadrivendiscovery.org/tworavens/tworavens/rook-service:latest"', 'docker tag registry.datadrivendiscovery.org/tworavens/tworavens/rook-service:latest registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/tworavens/rook-service:latest'),
    ('push image registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/tworavens/rook-service:latest', 'docker push registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/tworavens/rook-service:latest'),

    ('pull image registry.datadrivendiscovery.org/eve/docker-images:latest', 'docker pull registry.datadrivendiscovery.org/eve/docker-images:latest'),
    ('tag image  as "registry.datadrivendiscovery.org/eve/docker-images:latest"', 'docker tag registry.datadrivendiscovery.org/eve/docker-images:latest registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/eve/docker-images:latest'),
    ('push image registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/eve/docker-images:latest', 'docker push registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/eve/docker-images:latest'),
]


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