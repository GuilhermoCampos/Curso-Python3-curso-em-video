import random
computador = random.randint(0, 10)
tentativas = 1
dificuldade = 'M'
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Consegue adivinhar qual foi?''')
while dificuldade not in 'SsNn':
    if tentativas == 1:
        dificuldade = str(input('Deseja jogar no modo com ajuda?: [S/N] ')).strip().upper()[0]
    else:
        dificuldade = str(input('Opção inválida por favor tente novamente: [S/N] ')).strip().upper()[0]
    if dificuldade == 'S':
        facil = True
    else:
        facil = False
    tentativas += 1
jogador = int(input('Qual o Seu palpite?: '))
while not jogador == computador:
    tentativas += 1
    if jogador < computador:
        diferenca = 'Mais'
    else:
        diferenca = 'Menos'
    if facil == True:
        jogador = int(input('{}... Tente novamente: '.format(diferenca)))
    else:
        jogador = int(input('Tente novamente: '))
if tentativas != 1:
    print('Acertou com {} tentativas, Parabéns!!!'.format(tentativas))
else:
    print('Parabéns acertou de 1º')

