Regex
=====

## Presentación

Las Expresiones Regulares son una herramienta de búsqueda y manipulación de cadenas de caracteres increíblemente potente presente en **todos** los lenguajes de programación. Este curso busca llevar al alumno a entenderlas y darles un uso correcto dentro de sus diferentes aplicaciones.

Algunos puntos de este temario asumen un uso intermedio de la CLI, por lo que se recomienda el curso de "Línea de Comandos".

## Temario

1. Qué es y para qué sirven las expresiones regulares, por ejemplo `/^([a-z\.\+]{4,30})@([a-z\.]+)\.([\w]{2,5})$/`
1. Notas sobre el curso
1. El caracter `.` e introducción a los caracteres especiales y su escapado
1. Los delimitadores numéricos: `+`, `*`, `?`
1. Los contadores `{1,4}`
1. Las clases predefinidas `\w`, `\d`, `\s` …
1. Las clases construidas `[a-zA-Z0-9]`
1. Not `^`, su uso y sus peligros
1. El caso de `?` como delimitador
1. Principio (`$`) y final de línea (`^`)
1. Expresiones comunes:
  1. mails
  1. teléfonos
  1. logs
  1. nombres
  1. locaciones
    1. [what three words](https://what3words.com/)
1. Búsqueda y reemplazo
1. Procesadores de texto
1. `grep` y `find` desde consola
1. Regex en
  1. PHP
  1. Javascript
  1. Python
  1. Perl (aunque se burlen)


Apuntes:
=====
* https://regex101.com/
* https://elcodigoascii.com.ar/

## El caso de (?) como delimitador
El ? indica al patrón que encuentre las coincidencias de manera rápida (o greedy); es decir, devolviendo el resultado más pequeño que haga match hasta donde se encuentra el delimitador, y esto lo haga tantas veces como sea posible dentro de la cadena.

## Not (^), su uso y sus peligros
Este caracter nos permite negar una clase o construir “anticlases”, vamos a llamarlo así, que es: toda la serie de caracteres que no queremos que entren en nuestro resultado de búsqueda.
Para esto definimos una clase, por ejemplo: [ 0-9 ], y la negamos [ ^0-9 ] para buscar todos los caracteres que coincidan con cualquier caracter que no sea 0,1,2,3,4,5,6,7,8 ó 9

## Principio (^) y final de linea ($)
Estos dos caracteres indican en qué posición de la línea debe hacerse la búsqueda:
el ^ se utiliza para indicar el principio de línea
el $ se utiliza para indicar final de línea

^ ------------- $
