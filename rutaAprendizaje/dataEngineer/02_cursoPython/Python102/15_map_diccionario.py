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
  item['impuesto'] = item['precio'] * .19
  return item

nuevo_items = list(map(agregar_impuestos, items))
print('nuevo_items: ', nuevo_items)

print('***error con lista de items: ', items)

#esta implementación tiene un problema porque el map modifica la lista original y eso puede causar errores
