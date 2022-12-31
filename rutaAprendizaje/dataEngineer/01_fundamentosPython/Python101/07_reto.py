my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

for i in range(len(my_list)):
  #print('my_list[', i, ']: ', my_list[i])
  if  my_list[i] > 0:
    new_list.append(my_list[i])
print(new_list)