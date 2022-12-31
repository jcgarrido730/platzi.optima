def obtener_poblacion(diccionario_paises):
  poblacion_diccionario = {
    '2022' : int(diccionario_paises['2022 Population']),
    '2020' : int(diccionario_paises['2020 Population']),
    '2015' : int(diccionario_paises['2015 Population']),
    '2010' : int(diccionario_paises['2010 Population']),
    '2000' : int(diccionario_paises['2000 Population']),
    '1990' : int(diccionario_paises['1990 Population']),
    '1980' : int(diccionario_paises['1980 Population']),
    '1970' : int(diccionario_paises['1970 Population'])
  }
  etiquetas = poblacion_diccionario.keys()
  valores = poblacion_diccionario.values()
  return etiquetas, valores

def poblacion_por_pais(p_datos, p_pais):
  resultado = list(filter(lambda item : item['Country'] == p_pais, p_datos))
  return resultado
  