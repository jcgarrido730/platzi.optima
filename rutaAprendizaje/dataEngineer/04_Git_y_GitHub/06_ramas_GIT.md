# Ramas en GIT
Las ramas (branches) son la forma de hacer cambios en nuestro proyecto sin afectar el flujo de trabajo de la rama principal. Esto porque queremos trabajar una parte muy específica de la aplicación o simplemente experimentar.

La cabecera o HEAD representan la rama y el commit de esa rama donde estamos trabajando. 
Por defecto, esta cabecera aparecerá en el último commit de nuestra rama principal. Pero podemos cambiarlo al crear una rama (```git branch rama```, ```git checkout -b rama```) o movernos en el tiempo a cualquier otro commit de cualquier otra rama con los comandos (```git reset id-commit```, ```git checkout rama-o-id-commit```).

### Generar una nueva rama
```
$ git branch nombre_rama
```

### Saltar de una rama a otra
```
$ git checkout nombre_rama
```

### Genera una rama y nos mueve a ella
```
$ git checkout -b nombre_rama
```

### Regresar a un commit en específico, sin importar la rama. Se elimina el historial de los commit posteriores al id seleccionado
```
$ git reset id-commit
```

### Regresar a un commit en específico, sin importar la rama. No elimina los commit posteriores al id seleccionado
```
$ git checkout rama-o-id-commit
```
