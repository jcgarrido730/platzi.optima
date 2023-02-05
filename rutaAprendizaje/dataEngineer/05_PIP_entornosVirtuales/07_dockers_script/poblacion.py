import csv 

def leer_csv(ruta):
  with open(ruta, 'r') as archivo_csv:
    lector = csv.reader(archivo_csv, delimiter = ',')
    cabecera = next(lector)
    datos = []
    for linea in lector:
      iterable = zip(cabecera, linea)
      diccionario_paises = {key : value for key, value in iterable}
      datos.append(diccionario_paises)
    return datos

if __name__== '__main__':
  datos = leer_csv('poblacion.csv')
  print(datos[0])
  print('')
  print(datos[1])
  #print(datos)
