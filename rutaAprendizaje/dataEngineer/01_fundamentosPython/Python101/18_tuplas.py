#tuplas: estructura de datos que no permite hacer modificaciones
tupla_numeros = (1, 2, 3, 4, 5)
print('tupla_numeros: ', tupla_numeros)
print(type(tupla_numeros))

tupla_nombres = ('ana', 'veronica', 'marcela', 'ana')
print('tupla_nombres: ', tupla_nombres)
print(type(tupla_nombres))

#al igual que las listas puedo acceder a las posiciones con el []
print('tupla_numeros[0]: ', tupla_numeros[0])
print('tupla_numeros[-1]: ', tupla_numeros[-1])

print('tupla_nombres.index('"veronica"'): ', tupla_nombres.index('veronica'))
print('tupla_nombres.count('"ana"'): ', tupla_nombres.count('ana'))

#momdificar una tupla, se copian los valores a una lista, se modifica la lista y se vuelve y se crea la tupla
nueva_lista = list(tupla_nombres)
print('nueva_lista: ', nueva_lista)
print(type(nueva_lista))

nueva_lista[0] = 'Liliana'
print('nueva_lista: ', nueva_lista)

nueva_tupla = tuple(nueva_lista)
print('nueva_tupla: ', nueva_tupla)
print(type(nueva_tupla))
