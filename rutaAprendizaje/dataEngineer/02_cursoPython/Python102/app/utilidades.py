def obtener_poblacion():
  llave = ['col', 'bol']
  valor = [300, 400]
  return llave, valor

def poblacion_por_pais(p_datos, p_pais):
  resultado = list(filter(lambda item : item['Pais'] == p_pais, p_datos))
  return resultado