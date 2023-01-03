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
