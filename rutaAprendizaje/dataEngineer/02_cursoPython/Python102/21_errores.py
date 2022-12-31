print('manejo de errores')
suma = lambda x, y: x + y

print('suma(2, 3): ', suma(2, 3))
assert suma(2, 3) == 5

numero = 10
if numero % 2 == 0:
  raise Exception('el numero es par')

print('numero: ', numero)
