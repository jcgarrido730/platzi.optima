# GIT

- El comando git show nos muestra los cambios que han existido sobre un archivo y es muy útil para detectar cuándo se produjeron ciertos cambios, qué se rompió y cómo lo podemos solucionar

- Si queremos ver la diferencia entre una versión y otra, no necesariamente todos los cambios desde la creación del archivo, podemos usar el comando git diff commitA commitB

- Recuerda que puedes obtener el ID de tus commits con el comando git log

# Comandos para analizar cambios en GIT

### Inicializar el repositorio
```
    $ git init
```

### Agregar el archivo al repositorio
```
$ git add nombre_de_archivo.ext
```

### Agregamos los cambios para el repositorio
```
$ git commit -m "Comentario"
```

### Agregar los cambios de la carpeta en la que nos encontramos agregar todo
```
$ git add .
```

### Visualizar cambios
```
$ git status
```

### Histórico de cambios con detalles
```
git log nombre_de_archivos.ext
```

### Envía a otro repositorio remoto lo que estamos haciendo
```
$ git push
```

### Traer repositorio remoto
```
$ git pull
```

### Listado del directorio en donde me encuentro. Es decir, como emplear dir en windows.
```
$ ls
```

### Ubicación actual
```
$ pwd
```

### Nuevo directorio
```
$ mkdir
```

### Crear archivo vacío
```
$ touch archivo.ext: 
```

### Muestra el contenido del archivo
```
$ cat archivo.ext
```

### Historial de comandos utilizados durante esa sesión
```
$ history
```

### Eliminación de archivo
```
$ rm archivo.ext
```

### Ayuda sobre el comando
```
$ --help
```

### Traer cambios realizados
```
$ git checkout
```

### Se utiliza para devolver el archivo que se tiene en ram. Cuando escribimos git add, lo devuelve a estado natural mientras está en staging.
```
$ git rm --cached archivo.ext
```

### Muestra la lista de configuración de git
```
$ git config --list
```

### Rutas de acceso a la configuración de git
```
$ git config --list --show-origin
```

### Muestra la historia del archivo
```
$ git log archivo.ext
```
