# GitHub

### Configurar llave pública y privada:
```
# Este proceso pide clave de GitHub
$ ssh-keygen -t rsa -b 4096 -C "jcgarrido@gmail.com"

# -t: especifica el algoritmo que se va a usar -> rsa
# -b: complejidad de la llave -> 4096
# -C: a qué correo electrónico va a estar asociada esta llave

# se recomienda dejar la ruta predeterminada en donde almacena la llave 
# Opcional colocar una contraseña adicional de texto a la llave publica y privada 

# Validar que este funcionando el agente ssh y agregar llave privada al sistema (Linux / Windows)
$ eval $(ssh-agent -s)
$ ssh-add ~/.ssh/id_rsa

# copiar el contenido del archivo $ruta/del_sistema/.ss/id_rsa_pub y pegarlo en GitHub

profile > settings > SSH and GPG Keys > New SSH key
```

### Para subir los cambios que tengo en el repositorio local:
```
# asegurarse de estar ubicados en la rama que tiene los cambios
$ git status 
$ git remote -v
# git remote add origin git@github.com:jcgarrido730/nombre.repositorio.git
$ git push origin nombre_rama
$ git status
```

### Para descargar los cambios de un repositorio remoto:
```
# asegurarse de estar ubicados en el repositorio en donde queremos descargar los cambios
$ git pull origin nombre_rama
```
