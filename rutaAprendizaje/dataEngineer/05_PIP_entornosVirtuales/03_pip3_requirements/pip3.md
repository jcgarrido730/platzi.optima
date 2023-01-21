# Usando entornos virtuales en Python

## Verificar donde esta python y pip3
```
$ which python3
$ which pip3
```

## Si estas en linux o wsl debes instalar
```
$ sudo apt install -y python3-venv
```

## Poner cada proyecto en su propio ambiente, entrar en cada carpeta
```
$ python3 -m venv env
```

## Activar el ambiente
```
$ source env/bin/activate
```

## Salir del ambiente virtual
```
$ deactivate
```

## Podemos instalar las librerias necesarias en el ambiente virtual como por ejemplo
```
$ pip3 install matplotlib==3.5.0
```

## Verificar las instalaciones
```
$ pip3 freeze
```