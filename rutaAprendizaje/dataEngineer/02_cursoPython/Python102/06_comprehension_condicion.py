import random
lista_paises = ['col', 'mex', 'bol', 'pe']
poblacion_v2 = {pais : random.randint(1, 100) for pais in lista_paises}
print('poblacion_v2: ', poblacion_v2)

resultado = {pais : poblacion for(pais, poblacion) in poblacion_v2.items() if poblacion > 50}
print('resultado: ', resultado)

texto = 'Cadena de texto de prueba i'
valores_unicos = {c : c.upper() for c in texto if c in 'aeiou'}
print('valores_unicos: ', valores_unicos)
