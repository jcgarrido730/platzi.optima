print('manejo de errores')
division = lambda x, y : x / y


try:
  resultado = division(1, 0)
  
  assert 1 != 1, '1 no es diferente de 1'
  
  numero = 10
  if numero % 2 == 0:
    raise Exception('el numero es par')
    
except AssertionError as error:
  print('error personalizado: AssertionError. Mensaje de error: [', error, ']')
  
except ZeroDivisionError as error:
  print('error personalizado: division entre cero. Mensaje de error: [', error, ']')
  
except Exception as error:
  print('error personalizado. Mensaje de error: [', error, ']')
  
print('continuacion del programa')
