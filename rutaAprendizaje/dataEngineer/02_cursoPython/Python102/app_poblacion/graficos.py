import matplotlib.pyplot as plt

def crear_grafico_barras(etiquetas, valores):
  figura, ax = plt.subplots()
  ax.bar(etiquetas, valores)
  plt.show()

def crear_grafico_torta(etiquetas, valores):
  figura, ax = plt.subplots()
  ax.pie(valores, labels=etiquetas)
  ax.axis('equal')
  plt.show()
  
if __name__ == '__main__':
  etiquetas = ['a', 'b', 'c']
  valores = [10, 70, 20]
  #crear_grafico_barras(etiquetas, valores)
  crear_grafico_torta(etiquetas, valores)
  