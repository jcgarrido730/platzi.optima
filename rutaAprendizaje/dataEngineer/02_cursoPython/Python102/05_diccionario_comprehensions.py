import random
diccionario = {}
for i in range(1, 6): 
  diccionario[i] = i * 2

print('diccionario: ', diccionario)

#diccionario Comprehension
diccionario_v2 = {i : i * 2 for i in range(1, 6)}
print('diccionario_v2: ', diccionario_v2)


lista_paises = ['col', 'mex', 'bol', 'pe']
poblacion = {}
for pais in lista_paises:
  poblacion[pais] = random.randint(1, 100)
print('poblacion: ', poblacion)

poblacion_v2 = {pais : random.randint(1, 100) for pais in lista_paises}
print('poblacion_v2: ', poblacion_v2)

#unir 2 listas
nombres = ['veronica', 'marcela', 'pedro', 'liliana']
edades = [65, 43, 30, 85]
print('lista_con_tuplas(nombre:edad) =', list(zip(nombres, edades)))
print('tipo_dato: ', type(list(zip(nombres, edades))))

diccionario_v3 = {nombre : edad for(nombre, edad) in zip(nombres, edades)}
print('diccionario_v3: ', diccionario_v3)
print('tipo_dato: ', type(diccionario_v3))
