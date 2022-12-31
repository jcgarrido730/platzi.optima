import utilidades 
import poblacion
import graficos 

def opciones_menu():
  print('1. grafico_barras_por_pais')
  print('2. grafico_torta_porcentaje')
  print('0. salir')
  print('')
  return input('Seleccione una opcion: ')

def grafico_barras_por_pais():
  datos = poblacion.leer_csv('./app_poblacion/poblacion.csv')
  var_pais = input('Ingresar el pais: ')
  resultado = utilidades.poblacion_por_pais(datos, var_pais)

  if len(resultado) > 0:
    var_pais = resultado[0]
    etiquetas, valores = utilidades.obtener_poblacion(var_pais)
    graficos.crear_grafico_barras(etiquetas, valores)

def grafico_torta_porcentaje():
  datos = poblacion.leer_csv('./app_poblacion/poblacion.csv')
  datos = list(filter(lambda item : item['Continent'] == 'South America', datos))
  paises = list(map(lambda x : x['Country'], datos))
  porcentajes = list(map(lambda x : x['World Population Percentage'], datos))
  graficos.crear_grafico_torta(paises, porcentajes)


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
  