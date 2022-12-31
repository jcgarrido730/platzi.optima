#hacer transformaciones a una lista de elementos
#la salida es la misma cantidad de elemento pero transformados

numeros = [1, 2, 3, 4, 5]
transformacion_numeros = []

for elemento in numeros:
  transformacion_numeros.append(elemento * 2)

print('lista numeros original: ', numeros)
print('lista numeros transformada: ', transformacion_numeros)

#map(func lambda, lista) => retorna una referencia, toca pasarlo a lista
transformacion_map = list(map(lambda i : i * 2, numeros))
print('lista numeros transformacion_map: ', transformacion_map)

#map que recibe 2 parametros
numeros2 = [6, 7, 8]
print('lista numeros : ', numeros)
print('lista numeros2: ', numeros2)

resultado = list(map(lambda x, y : x + y, numeros, numeros2))
print('resultado     : ', resultado)
