for i in range(1, 5):
  print('i: ', i)

mi_iterable = iter(range(1, 5))
print('mi_iterable: ', mi_iterable)

print('primera iteración: ', next(mi_iterable))
print('segunda iteración: ', next(mi_iterable))
print('tercera iteración: ', next(mi_iterable))
print('cuarta iteración: ', next(mi_iterable))

#llega al limite y geera error
print('quinta iteración: ', next(mi_iterable))
