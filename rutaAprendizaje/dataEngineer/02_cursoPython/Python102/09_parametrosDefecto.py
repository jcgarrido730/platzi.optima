def funcion_volumen(alto=0, ancho=0, profundidad=0):
  return alto * ancho * profundidad

def retornoMultiplesValores(parametro1='parametro1', parametro2='parametro2', parametro3='parametro3'):
  return parametro1, parametro2, parametro3

volumen = funcion_volumen()
print('el volumen es: ', volumen)

volumen = funcion_volumen(1, 1, 1)
print('el volumen es: ', volumen)

volumen = funcion_volumen(ancho=10)
print('el volumen es: ', volumen)

resultado = retornoMultiplesValores(parametro3='otro valor')
print('retorna una tupla con los multiples valores: ', resultado)

print('resultado[0]: ', resultado[0])
print('resultado[1]: ', resultado[1])
print('resultado[2]: ', resultado[2])


var1, var2, var3 = retornoMultiplesValores(parametro3='otro valor')
print('var1 = ', var1)
print('var2 = ', var2)
print('var3 = ', var3)
