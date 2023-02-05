# requirements.txt
Archivo que gestiona todas las dependencias y en que versiones se necesitan para el proyecto.

# Generar el archivo con el siguiente comando:
```sh
$ pip3 freeze > requirements.txt
```

# Revisar lo que hay dentro del archivo
```sh
$ cat requirements.txt
```

# Instalar las dependencias necesarias configuradas en el archivo
```sh
$ pip3 install -r requirements.txt
```

# Preparar archivo para contribución
```sh
# App Project
$ git clone
$ cd dir/mi_app/
$ python3 -m venv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
$ python3 main.py
```
