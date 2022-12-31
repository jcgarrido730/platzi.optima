conjunto_paises = {'argentina', 'uruguay', 'ecuador', 'colombia', 'argentina'}
print('conjunto_paises = ', conjunto_paises)
print('tipo de dato: ', type(conjunto_paises))

conjunto_numeros = {1,2,3,4,5,6,7,8,9,0}
print('conjunto_numeros = ', conjunto_numeros)
print('tipo de dato: ', type(conjunto_numeros))

conjunto_tiposDato = {1,2,3,4.1,'cadena',False}
print('conjunto_tiposDato = ', conjunto_tiposDato)
print('tipo de dato: ', type(conjunto_tiposDato))

conjunto_desdeCadena = set('Hooola')
print('conjunto_desdeCadena = ', conjunto_desdeCadena)
print('tipo de dato: ', type(conjunto_desdeCadena))

conjunto_desdeTupla = set(('abc', 'cbv', 'as', 'abc', 'ab', 'cba'))
print('conjunto_desdeTupla = ', conjunto_desdeTupla)
print('tipo de dato: ', type(conjunto_desdeTupla))

lista_numeros = [1,2,3,1,2,3,4]
conjunto_numeros = set(lista_numeros)
print('conjunto_numeros = ', conjunto_numeros)

lista_numerosUnicos = list(conjunto_numeros)
print('lista_numerosUnicos = ', lista_numerosUnicos)
