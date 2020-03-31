from random import randint
from time import sleep
computador = randint(1, 3)
print('\033[7;30m{}\033[m\n\033[7;30m{:^60}\033[m\n\033[7;30m{}\033[m'.format('-=-' * 20, 'Jokenpô', '=-=' * 20))
print('Você jogará contra a máquina, não se preucupe ela já escolheu o que vai jogar')
jogador = int(input('''Escolha entre:'
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
Sua escolha: '''))
if 1 <= jogador <= 3:
    print('Prepare-se')
    sleep(0.5)
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ!!!')
    sleep(1)

    if computador == jogador:
        resultado = 'EMPATE!'
    elif computador == 1 and jogador == 2:
        resultado = 'Jogador VENCE!'
    elif computador == 2 and jogador == 1:
        resultado = 'Computador VENCE!'
    elif computador == 3 and jogador == 1:
        resultado = 'Jogador VENCE!'
    elif computador == 1 and jogador == 3:
        resultado = 'Computador VENCE!'
    elif computador == 2 and jogador == 3:
        resultado = 'Jogador VENCE!'
    elif computador == 3 and jogador == 2:
        resultado = 'Computador VENCE'

    if computador == 1:
        computador = 'Pedra'
    elif computador == 2:
        computador = 'Papel'
    elif computador == 3:
        computador = 'Tesoura'
    if jogador == 1:
        jogador = 'Pedra'
    elif jogador == 2:
        jogador = 'Papel'
    elif jogador == 3:
        jogador = 'Tesoura'
    print('{}\n' 'O Computador escolhe: {}!\n' 'O Jogador escolhe: {}!\n'
      '{}'.format('=-=' * 20, computador, jogador, '-=-' * 20))
    print(resultado)
else:
    print('Valor Inválido, Tente novamente!')