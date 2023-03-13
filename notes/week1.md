# Containers

## Run containers in background

```sh
docker container run --rm -p 4567:4567 -d backend-flask
```

## Return Container ID

```sh
CONTAINER_ID=$(docker run --rm -p 4567:4567 -d backend-flask)
```

## Get Container Images or Running Container Ids
```sh
docker ps
docker images
```

## Send Curl to Test Server
```sh
curl -X GET http://localhost:4567/api/activities/home -H "Accept: application/json" -H "Content-Type: application/json"
```

## Check Container Logs
```sh
docker logs CONTAINER_ID -f
docker logs backend-flask -f
docker logs $CONTAINER_ID -f
```

## Debugging adjacent containers with other containers
```sh
docker run --rm -it curlimages/curl "-X GET http://localhost:4567/api/activities/home -H \"Accept: application/json\" -H \"Content-Type: application/json\""
```

busybosy is often used for debugging since it install a bunch of thing

```sh
docker run --rm -it busybosy
```

## Gain Access to a Container
```sh
docker exec CONTAINER_ID -it /bin/bash
You can just right click a container and see logs in VSCode with Docker extension
```

## Delete an Image
```sh
docker image rm backend-flask --force
docker rmi backend-flask is the legacy syntax, you might see this is old docker tutorials and articles.
```

There are some cases where you need to use the --force

## Overriding Ports
```sh
FLASK_ENV=production PORT=8080 docker run -p 4567:4567 -it backend-flask
```

Look at Dockerfile to see how ${PORT} is interpolated