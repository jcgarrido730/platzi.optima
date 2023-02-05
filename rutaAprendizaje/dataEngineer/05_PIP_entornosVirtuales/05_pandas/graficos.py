import matplotlib.pyplot as plt

def crear_grafico_barras(etiquetas, valores, pais):
  figura, ax = plt.subplots()
  ax.bar(etiquetas, valores)
  plt.savefig(f'img/grafico_barras_{pais}.png')
  plt.close()

def crear_grafico_torta(etiquetas, valores, continente):
  fig, ax = plt.subplots()
  ax.pie(valores, labels=etiquetas)
  plt.savefig(f'img/grafico_pie_{continente}.png')
  plt.close()
  
if __name__ == '__main__':
  etiquetas = ['a', 'b', 'c']
  valores = [47, 19, 91]
  crear_grafico_barras(etiquetas, valores, 'generico')
  crear_grafico_torta(etiquetas, valores, 'generico')
