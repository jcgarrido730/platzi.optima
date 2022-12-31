var_x = 3.3
print('var_x = ', var_x)

var_y = 1.1 + 2.2
print('var_y = ', var_y)

print('var_x == var_y => ', var_x == var_y)

var_y_str = format(var_y, '.2g')
print('var_y_str = ', var_y_str)
print('str(var_x) == var_y_str => ', str(var_x) == var_y_str)

print('*' * 10)
var_tolerancia = 0.00001
print('var_tolerancia => ', var_tolerancia)
print('abs(var_x - var_y) < var_tolerancia => ', abs(var_x - var_y) < var_tolerancia)
