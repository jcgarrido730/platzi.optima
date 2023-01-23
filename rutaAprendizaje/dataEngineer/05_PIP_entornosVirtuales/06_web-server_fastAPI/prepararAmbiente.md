# Preparar ambiente
```sh
$ python3 -m venv env
```
# Activar un entorno virtual
```sh
$ source env/bin/activate
```
# Verificar que estemos dentro del entorno virtual
```sh
$ which python3
```
# Instalar la dependencia dentro del entorno virtual
```sh
$ pip3 install requests
```
# Verificar la instalacion
```sh
$ pip3 freeze
```
# Crear el archivo para que cualquier persona pueda desplegar el proyecto
```sh
$ pip3 freeze > requirements.txt
```
# Instalar FastAPI
```sh
$ pip3 install fastapi
```
# Instalar Uvicorn
```sh
$ pip3 install "uvicorn[standard]"
```
# Subir servidor web
```sh
$ uvicorn main:app --reload
```

# Ver en el navegador web
```html
http://localhost:8000/
http://localhost:8000/contacto
http://localhost:8000/retornaHTML
```