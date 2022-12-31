#https://pythongeeks.org/switch-in-python/
#Example on implementing switch case using the dictionary:
def vowel(num):
    switch={
      1:'a',
      2:'e',
      3:'i',
      4:'o',
      5:'u'
      }
    return switch.get(num, "Invalid input")
print('llamdo funcion vocal(1) ', vowel(1))
print('llamdo funcion vocal(2) ', vowel(2))
print('llamdo funcion vocal(3) ', vowel(3))
print('llamdo funcion vocal(4) ', vowel(4))
print('llamdo funcion vocal(5) ', vowel(5))
print('llamdo funcion vocal(0) ', vowel(0))
