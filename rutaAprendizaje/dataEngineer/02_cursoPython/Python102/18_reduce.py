import functools 

numeros = [10, 7, 2, 4, 5]

def acumulador(contador, item):
  print('contador: ', contador)
  print('item: ', item)
  return contador + item 

resultado = functools.reduce(acumulador, numeros)

#reduce(func lambda, iterador(contador o acumulador), item(elemento) : salida, lista)
resultado2 = functools.reduce(lambda contador, item : contador + item, numeros)

print('reduce numeros: ', resultado2)
