# Dockers
## Dockerfile
```
FROM python:3.8

WORKDIR /web-app
COPY requirements.txt /web-app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /web-app/requirements.txt

COPY . /web-app

["uvicorn", "main:web-app", "--host", "0.0.0.0", "--port", "80"]
```

## docker-compose.yml
```
services:
	web-server:
		build:
			context: .
			dockerfile: Dockerfile
    	volumes:
    		- .:/web-app
    	ports:
			- '8080:80' 
```

## Ejecutar docker
````bash
#construcción del contenedor
$ docker-compose build

#lanzar el contenedor (crear e iniciar contenedor)
$ docker-compose up -d 

#ver el estado del contenedor
$ docker-compose ps

#ingresar al navegador
localhost
localhost/contacto
localhost/retornaHTML

#ingresar al ambiente
$ docker-compose exec web-app bash

$ cd web-app
$ exit

#bajar el contenedor (elimina el contenedor)
$ docker-compose down
```
