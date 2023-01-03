# GIT MERGE 
El comando ```git merge``` nos permite crear un nuevo commit con la combinación de dos ramas o branches (la rama donde nos encontramos cuando ejecutamos el comando y la rama que indiquemos después del comando).

Ocurren conflictos cuando dos ramas tienen actualizaciones diferentes en ciertas líneas en los archivos.

## Para hacer el merge debo estar en la rama principal, o la rama a donde necesito subir los cambios
```
$ git status 
$ git branch
 main
 *nombre_rama

# Me cambio a la rama main o a la que necesito subir los cambios
$ git checkout main

# Estando en main subo los cambios que tiene nombre_rama
$ git merge nombre_rama
# colocar un comentario del merge
$ git status 
```
