def incremento(x):
  return x + 1

resultado1 = incremento(10)
print('resultado1: ', resultado1)

incremento2 = lambda x : x + 1 

resultado2 = incremento2(20)
print('resultado2: ', resultado2)

nombre_complento = lambda nombre, apellido : f'Hola {nombre.title()} {apellido.title()}'
saludo = nombre_complento('alan', 'brito delgado')
print('saludo: ', saludo)
