import modulo
print('llamdo al modulo: ', modulo.a)

import utilidades

datos = [
  {'Pais' : 'Colombia',
   'Poblacion' : 500
  },
  {'Pais' : 'Bolivia',
   'Poblacion' : 300
  }
]

def programa():
  llave, valor = utilidades.obtener_poblacion()
  print('llave, valor: ', llave, valor)
  
  
  var_pais = input('Ingresar el pais: ')
  resultado = utilidades.poblacion_por_pais(datos, var_pais)
  print('Población por pais: ', resultado)

#este if le indica al archivo main.py que si es ejecutado desde la terminal entonces ejecute el método programa(). Si es ejecutado desde otro archivo el método programa() no se va a ejecutar
if __name__ == '__main__':
  programa()
  