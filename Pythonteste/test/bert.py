from random import randint
from time import sleep
while True:
    itens = ('0', 'Pedra', 'Papel', 'Tesoura')
    computador = randint(1, 3)
    print('\033[7;30m{}\033[m\n\033[7;30m{:^60}\033[m\n\033[7;30m{}\033[m'.format('-=-' * 20, 'Jokenpô', '=-=' * 20))
    print('Você jogará contra a máquina, não se preucupe ela já escolheu o que vai jogar')
    jogador = int(input('Escolha entre:\n[ 1 ] Pedra\n[ 2 ] Papel\n[ 3 ] Tesoura\nSua escolha: '))
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
        print('{}\n' 'O Computador escolhe: {}!\n' 'O Jogador escolhe: {}!\n'
          '{}'.format('=-=' * 11, itens[computador], itens[jogador], '-=-' * 11))
        print(resultado)
        op = input('Quer continnar? [S/N] ')
        if op in 'Nn:':
            print('Fim .-.')
            break
    else:
        print('Valor Inválido, Tente novamente!')