print('------- for: ')
for elementos in range(3):
  print(elementos)

print('------- rangos: ')
for elementos in range(1, 3):
  print(elementos)

print('------- rangos negativo: ')
for elementos in range(-2, 1):
  print(elementos)

print('------- lista: ')
lista_numeros = [2, 3, 5, 7, 11]
for i in range(len(lista_numeros)):
  print ('elemento de la lista [', i, ']:', lista_numeros[i])

print('-------------------------------------: ')
for i in lista_numeros:
  print(i)
print('-------------------------------------: ')

print('------- tupla: ')
tupla_numeros = (2, 3, 5, 7, 11)
for i in range(len(tupla_numeros)):
  print ('elemento de la tupla (', i, '):', tupla_numeros[i])

print('------- diccionario: ')
producto = {
  'descripcion': 'camisa',
  'talla': 'm',
  'precio': 30000,
  'inventario': 11
}
for i in producto:
  print ('elemento del diccionario {', i, '}:', producto[i])

print('------- diccionario: ')
for key, value in producto.items():
  print ('elemento del diccionario {', key, '}:', value)

print('------- lista de diccionarios: ')
lista_diccionarios = [
  {
    'descripcion': 'camisa',
    'talla': 'm',
    'precio': 30000,
    'inventario': 11
  },
  {
    'descripcion': 'pantalon',
    'talla': '36',
    'precio': 60000,
    'inventario': 13
  }
]

for elemento in lista_diccionarios:
  print('descripcion producto: ', elemento['descripcion'])
  print('talla producto: ', elemento['talla'])
  print('precio producto: ', elemento['precio'])
  print('inventario producto: ', elemento['inventario'])