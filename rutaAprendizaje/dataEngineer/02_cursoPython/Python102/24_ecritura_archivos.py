#with open('') as : no es necesario cerrar el archivo close()
print('with open(./archivo_texto.txt, r+) as mi_archivo: ')
with open('./archivo_texto.txt', 'r+') as mi_archivo:
  for linea in mi_archivo:
    print(linea)
  mi_archivo.write('nueva linea\n')

#r solo lctura
#r+ lectura y escritura
#w+ sobreescribe el archivo
