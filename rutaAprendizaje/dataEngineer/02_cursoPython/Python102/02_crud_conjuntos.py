conjunto_paises = {'argentina', 'uruguay', 'ecuador', 'colombia', 'argentina'}
print('conjunto_paises = ', conjunto_paises)
print('tipo de dato: ', type(conjunto_paises))

tamano = len(conjunto_paises)
print('tamano conjunto_paises = ', tamano)

print('colombia' in conjunto_paises)
print('peru' in conjunto_paises)

#agregar elementos
conjunto_paises.add('peru')
conjunto_paises.add('peru')

#actualizar
conjunto_paises.update({'chile', 'bolivia', 'brasil', 'chile'})
print('conjunto_paises = ', conjunto_paises)

#eliminar
conjunto_paises.remove('brasil')
#conjunto_paises.remove('venezuela')
conjunto_paises.discard('venezuela')

conjunto_paises.clear()
print('conjunto_paises = ', conjunto_paises)

tamano = len(conjunto_paises)
print('tamano conjunto_paises = ', tamano)
