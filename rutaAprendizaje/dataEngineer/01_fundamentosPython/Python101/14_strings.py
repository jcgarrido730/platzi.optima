var_texto = 'Ella sabe programar en Python'
if 'JavaScript' in var_texto:
  print('JavaScript')
else:
  print('Python')

var_len = len(var_texto)
print('tamaño del string = ', var_len)

print('Texto original: ', var_texto)
print('Todo en mayusculas: ', var_texto.upper())
print('Todo en minusculas: ', var_texto.lower())
print('Repeticion palabra Ella: ', var_texto.count('Ella'))
print('MAYUSCULA <-> minuscula', var_texto.swapcase())
print('Comienza con Ella: ', var_texto.startswith('Ella'))
print('Finaliza con JavaScript: ', var_texto.endswith('JavaScript'))
print('Reemplazar: ', var_texto.replace('Python', 'C++'))
print('Capitalize: ', var_texto.capitalize())
print('Primera En Mayuscula: ', var_texto.title())
print('311 Es digito: ', "311".isdigit())
print('311.01 Es digito: ', "311.01".isdigit())
print('311,01 Es digito: ', "311,01".isdigit())
