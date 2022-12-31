var_nombre = 'Alan'
var_apellido = 'Brito'

var_nombre_completo = var_nombre + ' ' + var_apellido
print('nombre = ', var_nombre_completo)

#uso de comillas en medio del texto
var_texto = "uso de comillas sencillas: 'texto...'"
print(var_texto)

var_texto = 'uso de comilla dobles: "texto..."'
print(var_texto)

#format
var_plantilla = 'Reemplazo de valores en un string "+", var_nombre = ' + var_nombre + ', var_apellido = ' + var_apellido
print('var_plantilla = ', var_plantilla)

var_plantilla = 'Reemplazo de valores en un string "{}", var_nombre = {}, var_apellido = {}'.format('{}', var_nombre, var_apellido)
print('var_plantilla = ', var_plantilla)

var_plantilla = f'Reemplazo de valores en un string "f", var_nombre = {var_nombre}, var_apellido = {var_apellido}'
print('var_plantilla = ', var_plantilla)
