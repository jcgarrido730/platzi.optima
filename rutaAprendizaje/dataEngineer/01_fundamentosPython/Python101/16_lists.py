lista_numeros = [1, 2, 3, 4, 5]
print('lista_numeros: ', lista_numeros)
print('tipo de dato lista_numeros: ', type(lista_numeros))

lista_datos = [10, 10.1, True, 'Lista de datos']
print('lista_datos: ', lista_datos)
print('tipo de dato lista_datos: ', type(lista_datos))

print('primer valor de la lista de numeros: ', lista_numeros[0])
print('primer valor de la lista de datos: ', lista_datos[0])

lista_datos[len(lista_datos)-1] = 'texto'
print('lista_datos actualizada: ', lista_datos)

print('slicing lista_numeros: ', lista_numeros[:2])

print('True es elemento de la lista: ', True in lista_datos)

print('Texto es elemento de la lista: ', 'Texto' in lista_datos)
