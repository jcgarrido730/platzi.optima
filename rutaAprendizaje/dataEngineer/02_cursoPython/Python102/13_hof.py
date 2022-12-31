#Higher Order Function (HOF): una función dentro de otra función
#Funciones de Orden Superior
#A una funcion le podemos enviar otra función y ejecutarla desde ahí

def incremento(x):
  return x + 1

def hof(x, func):
  return x + func(x)

resultado1 = hof(2, incremento)
print('resultado1: ', resultado1)


#hof version lambda
incremento2 = lambda x : x + 1
hof2 = lambda x, func : x + func(x)

resultado2 = hof2(2, incremento2)
print('resultado2: ', resultado2)

#puedo ejecutar una funcion lambda directamente sin definirla
resultado2 = hof2(2, lambda x : x + 2)
print('resultado2: ', resultado2)

resultado2 = hof2(2, lambda x : x * 2)
print('resultado2: ', resultado2)
