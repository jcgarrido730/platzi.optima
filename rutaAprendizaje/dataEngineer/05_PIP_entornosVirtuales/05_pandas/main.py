import utilidades 
import poblacion
import graficos 
import pandas as pd 

def opciones_menu():
  print('1. grafico_barras_por_pais')
  print('2. grafico_torta_porcentaje')
  print('0. salir')
  print('')
  return input('Seleccione una opcion: ')

def grafico_barras_por_pais():
  df = pd.read_csv('poblacion.csv')
  var_pais = input('Ingresar el pais: ')
  df = df[df['Country'] == var_pais]
  resultado = df.values

  if len(resultado) > 0:
    etiquetas, valores = utilidades.obtener_poblacion(resultado)
    graficos.crear_grafico_barras(etiquetas, valores, var_pais)

def grafico_torta_porcentaje():
  df = pd.read_csv('poblacion.csv')
  var_continente = input('Ingresar el continente: ')
  df = df[df['Continent'] == var_continente]
  paises = df['Country'].values
  porcentajes  = df['World Population Percentage'].values 
  graficos.crear_grafico_torta(paises, porcentajes, var_continente)

#este if le indica al archivo main.py que si es ejecutado desde la terminal entonces ejecute el método programa(). Si es ejecutado desde otro archivo el método programa() no se va a ejecutar 
if __name__ == '__main__':
  var_opcion = opciones_menu()
  if var_opcion == '1':
    grafico_barras_por_pais()
  elif var_opcion == '2':
    grafico_torta_porcentaje()
  elif var_opcion == '0':
    print('salir del programa')
  else: 
    print('Opcion no valida.')
  