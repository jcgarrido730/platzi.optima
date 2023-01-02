# GIT

- El comando git show nos muestra los cambios que han existido sobre un archivo y es muy útil para detectar cuándo se produjeron ciertos cambios, qué se rompió y cómo lo podemos solucionar

- Si queremos ver la diferencia entre una versión y otra, no necesariamente todos los cambios desde la creación del archivo, podemos usar el comando git diff commitA commitB

- Recuerda que puedes obtener el ID de tus commits con el comando git log

# Comandos para analizar cambios en GIT

### Inicializar el repositorio
```git
    $ git init
```

### Agregar el archivo al repositorio
```git
$ git add nombre_de_archivo.ext
```

### Agregamos los cambios para el repositorio
```git
$ git commit -m "Comentario"
```

### Agregar los cambios de la carpeta en la que nos encontramos agregar todo
```git
$ git add .
```

### Visualizar cambios
```git
$ git status
```

### Histórico de cambios con detalles
```git
git log nombre_de_archivos.ext
```

### Envía a otro repositorio remoto lo que estamos haciendo
```git
$ git push
```

### Traer repositorio remoto
```git
$ git pull
```

### Listado del directorio en donde me encuentro. Es decir, como emplear dir en windows.
```git
$ ls
```

### Ubicación actual
```git
$ pwd
```

### Nuevo directorio
```git
$ mkdir
```

### Crear archivo vacío
```git
$ touch archivo.ext: 
```

### Muestra el contenido del archivo
```git
$ cat archivo.ext
```

### Historial de comandos utilizados durante esa sesión
```git
$ history
```

### Eliminación de archivo
```git
$ rm archivo.ext
```

### Ayuda sobre el comando
```git
$ --help
```

### Traer cambios realizados
```git
$ git checkout
```

### Se utiliza para devolver el archivo que se tiene en ram. Cuando escribimos git add, lo devuelve a estado natural mientras está en staging.
```git
$ git rm --cached archivo.ext
```

### Muestra la lista de configuración de git
```git
$ git config --list
```

### Rutas de acceso a la configuración de git
```git
$ git config --list --show-origin
```

### Muestra la historia del archivo
```git
$ git log archivo.ext
```
