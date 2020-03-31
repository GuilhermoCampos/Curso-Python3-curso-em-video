from random import randint
from time import sleep
computador = randint(1, 3)
print('\033[7;30m', '=-=' * 20,
      '\033[m\n\033[7;30m |                          Jokenpô                         | \033[m',
      '\n\033[7;30m', '\033[7;30m-=-' * 20, '\033[m')
jogador = str(input('Por Favor escolha entre: "Pedra, Papel e Tesoura" e digite a sua escolha: ')).lower().strip()
print('Analizando...')
sleep(2)
if computador == 1 and jogador == 'pedra':
    print('Empate os dois Escolhem PEDRA!')
elif computador == 1 and jogador == 'papel':
    print('Jogador Vence!! computador escolheu PEDRA!')
elif computador == 1 and jogador == 'tesoura':
    print('Computador Vence!! Computador escolheu PEDRA!')
elif computador == 2 and jogador == 'pedra':
    print('Computador Vence!! Computador escolheu PAPEL!')
elif computador == 2 and jogador == 'papel':
    print('Empate os dois Escolhem PAPEL!')
elif computador == 2 and jogador == 'tesoura':
    print('Jogador Vence!! Computador escolheu PAPEL!')
elif computador == 3 and jogador == 'pedra':
    print('Jogador Vence!! Computador escolheu TESOURA!')
elif computador == 3 and jogador == 'papel':
    print('Computador Vence!! Computador escolheu TESOURA!')
elif computador == 3 and jogador == 'tesoura':
    print('Empate os dois escolhem TESOURA!')
else:
    print('Você digitou errado! Tente novamente!')
