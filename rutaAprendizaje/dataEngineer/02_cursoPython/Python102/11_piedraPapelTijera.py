import random

opciones = ('piedra', 'papel', 'tijera')

def elegir_opcion():
  user_option = input('piedra, papel, tijera => ')
  if not user_option in opciones:
    print('Opcion no valida')
    #continue 
    return None, None
    
  user_option = user_option.lower()
  computer_option = random.choice(opciones)
  
  print('Opcion del usuario: ', user_option)
  print('Opcion de la computadora: ', computer_option)
  return user_option, computer_option

def reglas_juego(p_user_option, p_computer_option, p_contador_usuario, p_contador_computadora, p_empate):
  if p_user_option == p_computer_option:
    print('Hay un empate')
    p_empate += 1
  elif p_user_option == 'piedra':
    if p_computer_option == 'tijera':
      print('La Piedra le gana a la Tijera')
      print('Gana el usuario')
      p_contador_usuario += 1
    else:
      print('El Papel le gana a la Piedra')
      print('Gana el computador')
      p_contador_computadora += 1
  elif p_user_option == 'papel':
      if p_computer_option == 'piedra':
        print('El Papel le gana a la Piedra')
        print('Gana el usuario')
        p_contador_usuario += 1
      else:
        print('La Tijera le gana al Papel')
        print('Gana el computador')
        p_contador_computadora += 1
  elif p_user_option == 'tijera':
    if p_computer_option == 'papel':
      print('La Tijera le gana al Papel')
      print('Gana el usuario')
      p_contador_usuario += 1
    else:
      print('La Piedra le gana a la Tijera')
      print('Gana el computador')
      p_contador_computadora += 1
  return p_contador_usuario, p_contador_computadora, p_empate

def resultado_final(p_contador_usuario, p_contador_computadora, p_ronda, p_contador_empate):
  if p_contador_computadora == 2:
    print('')
    print('***********************************************')
    print('* Gana la computadora                         *')
    print('*                                             *')
    print('* Rondas: ',  p_ronda, '                                 *')
    print('* Empates: ', p_contador_empate, '                                 *')
    print('* Marcador final: Usuario ', p_contador_usuario, '|', p_contador_computadora, ' Computadora *')
    print('***********************************************')
    return False
    
  if p_contador_usuario == 2:
    print('')
    print('***********************************************')
    print('* Gana el usuario                             *')
    print('*                                             *')
    print('* Rondas: ',  p_ronda, '                                 *')
    print('* Empates: ', p_contador_empate, '                                 *')
    print('* Marcador final: Usuario ', p_contador_usuario, '|', p_contador_computadora, ' Computadora *')
    print('***********************************************')
    return False
  return True
  
def main():
  ronda = 0
  contador_usuario = 0
  contador_computadora = 0
  contador_empate = 0
  continua = True
  
  while continua:
    ronda += 1
    print('')
    print('**********')
    print('Ronda', ronda)
    print('Marcador: Usuario ', contador_usuario, '|', contador_computadora, ' Computadora', )
  
    user_option, computer_option = elegir_opcion()
    contador_usuario, contador_computadora, contador_empate = reglas_juego(user_option, computer_option, contador_usuario, contador_computadora, contador_empate)
    continua = resultado_final(contador_usuario, contador_computadora, ronda, contador_empate)

  return 
  
main()
