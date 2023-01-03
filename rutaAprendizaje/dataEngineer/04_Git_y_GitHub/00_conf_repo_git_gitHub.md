[https://medium.com/tech-learn-share/initialize-git-add-remote-origin-and-to-set-default-upstream-47e5d6dd955](https://medium.com/tech-learn-share/initialize-git-add-remote-origin-and-to-set-default-upstream-47e5d6dd955)


### Configuraciones de git:
```
$ git config
$ git config --list
```

### Configuración inicial git:
```
$ git config --global user.name "Juan Carlos Garrido Sarasa"
$ git config --global user.email jcgarrido@gmail.com
$ git config --global init.defaultBranch main
```

### Si por algún motivo te equivocaste en el nombre o email que configuraste al principio, lo puedes modificar de la siguiente manera:
```
$ git config --global --replace-all user.name "Aquí va tu nombre modificado"
```

### O si lo deseas eliminar y añadir uno nuevo
```
$ git config --global --unset-all user.name
$ git config --global --add user.name "Aquí va tu nombre"
```

### Configuraciones guardadas de git
```
$ git config --list --show-origin
```

### Inicializar y conectar con repositorio remoto:
```
$ git init
$ git remote -v
$ git remote add origin git@github.com:jcgarrido730/nombre.repositorio.git
```

### Validar a que repositorio estoy conectado
```
$ git remote -v
```

### Descargar cambios del repositorio remoto
```
$ git status
$ git pull origin main
$ git status
```

_Realizar los cambios en directorios o archivos_

### Agregar y subir cambios al repositorio remoto
```
$ git status
$ git add .
$ git status
$ git commit -m "Comentario del cambio."
$ git push -u origin main
# git push -u origin main, es lo mismo que git push --set-upstream origin main
$ git status 
```

_Realizar los cambios en directorios o archivos_

### Agregar y subir mas cambios al repositorio remoto
```
$ git status
$ git add .
$ git status
$ git commit -m "Comentario del cambio."
$ git push -u origin main
# git push -u origin main, es lo mismo que git push --set-upstream origin main
$ git status
```


# Otros comandos de git:
```git log --oneline```: Te muestra el id commit y el título del commit.

```git log --decorate```: Te muestra donde se encuentra el head point en el log.

```git log --stat```: Explica el número de líneas que se cambiaron brevemente.

```git log -p```: Explica el número de líneas que se cambiaron y te muestra que se cambió en el contenido.

```git shortlog```: Indica que commits ha realizado un usuario, mostrando el usuario y el título de sus commits.

```git log --graph --oneline --decorate y git log --pretty=format:"%cn hizo un commit %h el dia %cd"```: Muestra mensajes personalizados de los commits.

```git log -3```: Limitamos el número de commits.

```git log --after="2018-1-2" ```, 

```git log --after="today"``` y 

```git log --after="2018-1-2" --before="today"```: Commits para localizar por fechas.

```git log --author="Name Author"```: Commits hechos por autor que cumplan exactamente con el nombre.

```git log --grep="INVIE"```: Busca los commits que cumplan tal cual está escrito entre las comillas.

```git log --grep="INVIE" –i```: Busca los commits que cumplan sin importar mayúsculas o minúsculas.

```git log – index.html``` Busca los commits en un archivo en específico.

```git log -S "Por contenido"```: Buscar los commits con el contenido dentro del archivo.

```git log > log.txt```: guardar los logs en un archivo txt.