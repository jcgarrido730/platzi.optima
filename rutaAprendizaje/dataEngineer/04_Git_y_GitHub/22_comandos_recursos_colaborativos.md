# Comandos y recursos colaborativos en Git y GitHub

A continuación veremos una lista de comandos colaborativos para facilitar el trabajo remoto en GitHub:
```
$ git comando-a-usar --help: muestra como funciona el comando.

$ git shortlog -sn: muestra cuantos commit han hecho cada miembro del equipo.

$ git shortlog -sn --all: muestra cuantos commit han hecho cada miembro del equipo, hasta los que han sido eliminados.

$ git shortlog -sn --all --no-merge: muestra cuantos commit ha hecho cada miembro, quitando los eliminados sin los merges.

$ git blame ARCHIVO.ext: muestra quien hizo cada cosa línea por línea.

$ git blame ARCHIVO.ext -L #linea_inicial,#linea_final -c: muestra quien hizo cada cosa línea por línea, indicándole desde qué línea ver. Ejemplo: -L 35,50

$ git branch: se muestran las ramas locales.

$ git branch -r: se muestran todas las ramas remotas.

$ git branch -a: se muestran todas las ramas, tanto locales como remotas.
```
