persona = {
  'nombre': 'Alan',
  'apellido': 'Brito',
  'edad': 25,
  'lenguajes_programacion': ['c', 'c++', 'java']
}
print(persona)

persona['apellido'] = 'Delgado'
print(persona)

persona['edad'] += 5
persona['lenguajes_programacion'].append('c#')
print(persona)

del persona['lenguajes_programacion']
print(persona)

persona.pop('edad')
print(persona)

print('items: ', persona.items())
print('clave: ', persona.keys())
print('values: ', persona.values())
