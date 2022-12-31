numeros = []
for elemento in range(1, 11):
  numeros.append(elemento)

print('numeros: ', numeros)


#List Comprehension
numeros_v2 = [elemento for elemento in range(1, 11)]
print('List Comprehension numeros_v2: ', numeros_v2)

numeros_v3 = [elemento * 2 for elemento in range(1, 11)]
print('List Comprehension numeros_v3: ', numeros_v3)

numeros_v4 = [elemento * 2 for elemento in range(1, 11) if elemento % 2 == 0]
print('List Comprehension numeros_v4: ', numeros_v4)