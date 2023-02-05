import matplotlib.pyplot as plt

def generar_grafico_torta():
    etiquetas = ['A', 'B', 'C']
    valores = [200, 34, 120]
    
    fig, ax = plt.subplots()
    ax.pie(valores, labels=etiquetas)
    plt.savefig('img/grafico_pie.png')
    plt.close()