mi_archivo = open('./archivo_texto.txt')
print('mi_archivo.read(): ')
print(mi_archivo.read())
mi_archivo.close()

mi_archivo = open('./archivo_texto.txt')
print('mi_archivo.readline(): ')
print(mi_archivo.readline())
print(mi_archivo.readline())
print(mi_archivo.readline())
print(mi_archivo.readline())
mi_archivo.close()

#with open('') as : no es necesario cerrar el archivo close()
print('with open(./archivo_texto.txt) as mi_archivo: ')
with open('./archivo_texto.txt') as mi_archivo:
  for linea in mi_archivo:
    print(linea)
