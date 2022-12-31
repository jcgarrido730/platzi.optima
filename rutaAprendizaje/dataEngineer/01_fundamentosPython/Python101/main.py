import random

opciones = ('piedra', 'papel', 'tijera')
ronda = 1
contador_usuario = 0
contador_computadora = 0

while True:

  print('')
  print('**********')
  print('Ronda', ronda)
  print('Marcador: Usuario ', contador_usuario, '|', contador_computadora, ' Computadora', )
  
  user_option = input('piedra, papel, tijera => ')
  if not user_option in opciones:
    print('Opcion no valida')
    continue 
    
  user_option = user_option.lower()
  computer_option = random.choice(opciones)
  
  print('Opcion del usuario: ', user_option)
  print('Opcion de la computadora: ', computer_option)
  
  if user_option == computer_option:
    print('Hay un empate')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('La Piedra le gana a la Tijera')
      print('Gana el usuario')
      contador_usuario += 1
    else:
      print('El Papel le gana a la Piedra')
      print('Gana el computador')
      contador_computadora += 1
  elif user_option == 'papel':
      if computer_option == 'piedra':
        print('El Papel le gana a la Piedra')
        print('Gana el usuario')
        contador_usuario += 1
      else:
        print('La Tijera le gana al Papel')
        print('Gana el computador')
        contador_computadora += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('La Tijera le gana al Papel')
      print('Gana el usuario')
      contador_usuario += 1
    else:
      print('La Piedra le gana a la Tijera')
      print('Gana el computador')
      contador_computadora += 1

  if contador_computadora == 2:
    print('')
    print('***********************************************')
    print('* Gana la computadora                         *')
    print('*                                             *')
    print('* Marcador final: Usuario ', contador_usuario, '|', contador_computadora, ' Computadora *')
    print('***********************************************')
    break

  if contador_usuario == 2:
    print('')
    print('***********************************************')
    print('* Gana el usuario                             *')
    print('*                                             *')
    print('* Marcador final: Usuario ', contador_usuario, '|', contador_computadora, ' Computadora *')
    print('***********************************************')
    break
    
  ronda += 1
      