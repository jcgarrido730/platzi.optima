matriz = [
  [1, 2, 3], 
  [4, 5, 6], 
  [7, 8, 9]
]

print('matriz[0]: ', matriz[0])
print('matriz[0][1]: ', matriz[0][1])

for fila in range(len(matriz)):
  for columna in range(len(matriz[fila])):
    print('matriz[', fila,'][', columna,']: ', matriz[fila][columna])
  