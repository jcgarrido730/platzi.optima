user_option = input('Piedra, Papel, Tijera => ').lower()
computer_option = 'Piedra'.lower()

if user_option == computer_option:
  print('Hay un empate')
elif user_option == 'piedra':
  if computer_option == 'tijera':
    print('La Piedra le gana a la Tijera')
    print('Gana el usuario')
  else:
    print('El Papel le gana a la Piedra')
    print('Gana el computador')
elif user_option == 'papel':
    if computer_option == 'piedra':
      print('El Papel le gana a la Piedra')
      print('Gana el usuario')
    else:
      print('La Tijera le gana al Papel')
      print('Gana el computador')
elif user_option == 'tijera':
  if computer_option == 'papel':
    print('La Tijera le gana al Papel')
    print('Gana el usuario')
  else:
    print('La Piedra le gana a la Tijera')
    print('Gana el computador')
    