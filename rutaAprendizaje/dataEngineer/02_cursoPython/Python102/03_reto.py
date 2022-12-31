def message_creator(text):
   # Escribe tu solución 👇
   salida = {
    'computadora':'Con mi computadora puedo programar usando Python', 
    'celular':'En mi celular puedo aprender usando la app de Platzi', 
    'cable':'¡Hay un cable en mi bota!' 
  }
  
   if not text in salida:
     return 'Artículo no encontrado'
   return salida[text]

text = 'computadora'
response = message_creator(text)
print(response)
