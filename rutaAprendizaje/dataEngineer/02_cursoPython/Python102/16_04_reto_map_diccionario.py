items = [
  {
    'producto' : 'camisa',
    'precio' : 80
  },
  {
    'producto' : 'pantalon',
    'precio' : 100
  },
  {
    'producto' : 'pantaloneta',
    'precio' : 50
  }
]

print('items: ', items)
precios = list(map(lambda item : item['precio'], items))
print('precios: ', precios)

def agregar_impuestos(item):
  copia_item = item.copy()
  copia_item['impuesto'] = item['precio'] * .19
  return copia_item

nuevo_items = list(map(agregar_impuestos, items))
print('nuevo_items: ', nuevo_items)

print('***NO CAMBIA LA lista de items: ', items)

#Se realiza una copia del diccionario y se modifica la copia
