def obtener_poblacion(diccionario_paises):
  poblacion_diccionario = {
    '2022' : int(diccionario_paises[0][5]),
    '2020' : int(diccionario_paises[0][6]),
    '2015' : int(diccionario_paises[0][7]),
    '2010' : int(diccionario_paises[0][8]),
    '2000' : int(diccionario_paises[0][9]),
    '1990' : int(diccionario_paises[0][10]),
    '1980' : int(diccionario_paises[0][11]),
    '1970' : int(diccionario_paises[0][12])
  }
  etiquetas = poblacion_diccionario.keys()
  valores = poblacion_diccionario.values()
  return etiquetas, valores
  