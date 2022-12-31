conjunto_a = {'col', 'mex', 'bol'}
conjunto_b = {'pe', 'bol'}

#union
print('union')
conjunto_c = conjunto_a.union(conjunto_b)
print('conjunto_a.union(conjunto_b) = ', conjunto_c)
print('conjunto_a | conjunto_b = ', conjunto_a | conjunto_b)

#interseccion 
print('interseccion ')
conjunto_d = conjunto_a.intersection(conjunto_b)
print('conjunto_a.intersection(conjunto_b) = ', conjunto_d)
print('conjunto_a & conjunto_b = ', conjunto_a & conjunto_b)

#diferencia: deja los elementos del primer conjunto removiendo los elementos del segundo conjunto. Similar a una resta. 
#a - b: Quitar los elementos de b en a
print('diferencia ')
conjunto_e = conjunto_a.difference(conjunto_b)
print('conjunto_a.difference(conjunto_b) = ', conjunto_e)
print('conjunto_a - conjunto_b = ', conjunto_a - conjunto_b)

#diferencia simetrica: es hacer una union sin los elementos que coinciden en comun.
print('diferencia simetrica')
conjunto_f = conjunto_a.symmetric_difference(conjunto_b)
print('conjunto_a.symmetric_difference(conjunto_f) = ', conjunto_f)
print('conjunto_a ^ conjunto_b = ', conjunto_a ^ conjunto_b)
