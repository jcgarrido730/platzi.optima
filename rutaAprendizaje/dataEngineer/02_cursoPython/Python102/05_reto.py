def filter_by_length(words):
  # Escribe tu solución 👇
  resultado = list(filter(lambda palabra : len(palabra) >= 4, words))
  return resultado

words = ['amor', 'sol', 'piedra', 'día']
#words = ['rosa', 'gol', 'pez', 'dia', 'gafas']
words = []
response = filter_by_length(words)
print(response)
