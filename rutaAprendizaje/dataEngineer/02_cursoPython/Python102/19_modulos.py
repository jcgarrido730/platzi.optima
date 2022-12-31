import sys 
print('sys.path: ', sys.path)

#expresiones regulares
import re
texto = 'c4d3n4 d3 t3xt0 c0n v0c4l3s c0m0 núm3r0s y solo números: 123 4567'

#encuentra todo lo que sea un número + varias coincidencias
resultado = re.findall('[0-9]+', texto)
print('resultado: ', resultado)

#manejo de hora y fecha
import time
var_timestamp = time.time()
var_fecha_local = time.localtime()
var_formato_fecha = time.asctime(var_fecha_local)

print('var_timestamp: ', var_timestamp)
print('var_fecha_local: ', var_fecha_local)
print('var_formato_fecha: ', var_formato_fecha)

#colecciones utilidad para manejar listas
import collections
numeros = [1,1,2,3,5,2,2,5,7,9,0]
contador = collections.Counter(numeros)
print('repeticiones: ', contador)