# Containerization with docker

## Build docker images
```
docker build -t clothing-model .
```

## Test run the image
```
docker run -it --rm -p 8080:8080 clothing-model:latest
```