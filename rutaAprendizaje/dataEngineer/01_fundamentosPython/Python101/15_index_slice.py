var_texto = 'Ella sabe Python'

#index
print('Texto original: ', var_texto)
print('Posicion 0 del texto: ', var_texto[0])
print('Posicion 1 del texto: ', var_texto[1])
print('Posicion 2 del texto: ', var_texto[2])
print('Posicion 3 del texto: ', var_texto[3])
print('Ultima letra del texto: ', var_texto[len(var_texto)-1])
print('Penultima letra del texto: ', var_texto[-2])

#slicing
print('slicing 0:5 ', {var_texto[0:5]})
print('slicing 0:10 ', {var_texto[0:10]})
print('slicing :10 ', {var_texto[:10]})
print('slicing 5:len ', {var_texto[5:len(var_texto)]})
print('slicing 5:final ', {var_texto[5:]})
print('slicing de inicio hasta el final: ', {var_texto[:]})
print('slicing con 1 salto: ', {var_texto[10:16:1]})
print('slicing con 2 saltos: ', {var_texto[10:16:2]})
print('slicing de inicio a fin con 2 saltos: ', {var_texto[::2]})
