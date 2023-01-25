# Dockers
## Dockerfile
```
FROM python:3.8

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD bash -c "while true; do sleep 1; done"
```

## docker-compose.yml
```
services:
	app-csv:
		build:
			context: .
			dockerfile: Dockerfile
```

## Ejecutar docker
````bash
#construcción del contenedor
$ docker-compose build

#lanzar el contenedor (crear e iniciar contenedor)
$ docker-compose up -d 

#ver el estado del contenedor
$ docker-compose ps

#ingresar al ambiente
$ docker-compose exec app-csv bash

#ejecutar la aplicación
$ cd app
$ python3 main.py
$ exit

#bajar el contenedor (elimina el contenedor)
$ docker-compose down
```
