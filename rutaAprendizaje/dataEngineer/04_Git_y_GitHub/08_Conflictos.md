# Conflictos
Siempre debemos crear un nuevo commit para aplicar los cambios del merge. Si Git puede resolver el conflicto, hará commit automáticamente. En caso de no poder resolverlo, debemos solucionarlo manualmente y luego hacer el commit.

Los archivos con conflictos por el comando ```git merge``` entran en un nuevo estado que conocemos como ```Unmerged```. Funcionan muy parecido a los archivos en estado ```Unstaged```, algo así como un estado intermedio entre ```Untracked``` y ```Unstaged```. Solo debemos ejecutar ```git add``` para pasarlos al área de staging y ```git commit -m "comentario"``` para aplicar los cambios en el repositorio.

## Cómo revertir un merge
Si nos hemos equivocado y queremos cancelar el merge, debemos usar el siguiente comando:
```
$ git merge --abort
```
