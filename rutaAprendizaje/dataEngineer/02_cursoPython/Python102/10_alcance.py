precio = 100 #alcance global

def incremento():
  precio = 0 #alcance local
  precio += 10
  resultado = precio #alcance local
  return resultado

print('precio: ', precio)
precio2 = incremento()
print('precio2: ', precio2)

#esto genera un error porque la variable resultado no esta en el alcance global del programa
#print('resultado: ', resultado)
