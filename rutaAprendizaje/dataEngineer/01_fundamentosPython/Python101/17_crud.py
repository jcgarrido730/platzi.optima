#crud
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
print('lista_numeros: ', lista_numeros)
print('lista_numeros[0]: ', lista_numeros[0])
lista_numeros[-1] = 10
print('lista_numeros: ', lista_numeros)

lista_numeros.append(11)
print('adicionar el 11 al final de lista_numeros: ', lista_numeros)

lista_numeros.insert(0, -1)
print('inserta -1 al inicio de lista_numeros: ', lista_numeros)

lista_numeros.insert(1, 0)
print('inserta el 0 en la posicion 1 de lista_numeros: ', lista_numeros)

lista_texto = ['texto4', 'texto1', 'texto2', 'texto3']
print('lista_texto: ', lista_texto)

nueva_lista = lista_numeros + lista_texto
print('nueva_lista: ', nueva_lista)

print('posicion del elemento texto1 en nueva_lista: ', nueva_lista.index('texto1'))

nueva_lista.remove('texto4')
print('removiendo texto4 de la lista, nueva_lista: ', nueva_lista)

var_ult_lista = nueva_lista.pop()
print('removiendo el ultimo de la lista con pop(): ', var_ult_lista)
print('nueva_lista: ', nueva_lista)

var_primero_lista = nueva_lista.pop(0)
print('removiendo el primero de la lista con pop(0): ', var_primero_lista)
print('nueva_lista: ', nueva_lista)

nueva_lista.reverse()
print('Recorre la lista en sentido inverso: ', nueva_lista)

#genera error al intentar ordenar lista de elementos con diferentes tipos de datos
nueva_lista.sort()
print('Lista ordenada: ', nueva_lista)
