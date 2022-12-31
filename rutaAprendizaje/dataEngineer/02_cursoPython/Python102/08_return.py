def funcion_imprimir():
  print('hola')

def funcion_imprimir2(p_parametro):
  print('parametro: ', p_parametro)

funcion_imprimir()
funcion_imprimir2('cadena de texto enviada como parametro')

a = 10
b = 90 
c = 0

def suma(a, b):
  c = a + b
  return c 

c = suma(a, b)
funcion_imprimir2('suma {} + {} = {}'.format(a, b, c))

def sumatoria(p_inicio, p_fin):
  sumatoria = 0
  for x in range(p_inicio, p_fin+1):
    sumatoria += x
  return sumatoria
  
inicio = 1 
fin = 5 
resultado = sumatoria(inicio, fin)


funcion_imprimir2('sumatoria entre los numeros {} y {} = {}'.format(inicio, fin, resultado))