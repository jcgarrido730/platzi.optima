var_contador = 0
while var_contador < 10:
  print(var_contador)
  var_contador += 1

var_contador = 0
while var_contador < 20:
  print(var_contador)
  var_contador += 1
  if var_contador == 13:
    print('break')
    break

var_contador = 0
while var_contador < 20:
  var_contador += 1
  if var_contador < 17:
    print('esta linea si se imprime')
    continue
    print('esta linea no se imprime')
  print(var_contador)
  
