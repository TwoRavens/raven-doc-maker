
# Retag the pulled docker images for use in this repo

### Image 1

```
# pull image
docker pull registry.datadrivendiscovery.org/tworavens/tworavens/nginx:latest

# tag image
docker tag registry.datadrivendiscovery.org/tworavens/tworavens/nginx:latest registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/tworavens/nginx:latest

# push image
docker push registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/tworavens/nginx:latest
```

### Image 2

```
# pull image
docker pull registry.datadrivendiscovery.org/tworavens/tworavens:latest

# tag image
docker tag registry.datadrivendiscovery.org/tworavens/tworavens:latest registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/tworavens:latest

# push image
docker push registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/tworavens:latest
```

### Image 3

```
# pull image
docker pull registry.datadrivendiscovery.org/tworavens/tworavens/rook-service:latest

# tag image
docker tag registry.datadrivendiscovery.org/tworavens/tworavens/rook-service:latest registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/tworavens/rook-service:latest

# push image
docker push registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/tworavens/rook-service:latest
```

### Image 4

```
# pull image
docker pull registry.datadrivendiscovery.org/eve/docker-images:latest

# tag image
docker tag registry.datadrivendiscovery.org/eve/docker-images:latest registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/eve/docker-images:latest

# push image
docker push registry.datadrivendiscovery.org/cta2ta3/cra_tworavens/eve/docker-images:latest
```
