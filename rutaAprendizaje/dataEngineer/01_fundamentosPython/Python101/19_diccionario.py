diccionario = {}
print(type(diccionario))

diccionario = {
  'nombre':'Alan',
  'apellido':'Brito',
  'ocupacion':'empleado'
}
print('diccionario: ', diccionario)
print('numero elementos del diccionario: ', len(diccionario))

print('posicion - valor ocupacion: ', diccionario['ocupacion'])
print('.get - valor ocupacion: ', diccionario.get('ocupacion'))
print('.get - valor ocupacion: ', diccionario.get('oupacion'))

print('nombre esta en el diccionario: ', 'nombre' in diccionario)
print('segundoApellido esta en el diccionario: ', 'segundoApellido' in diccionario)