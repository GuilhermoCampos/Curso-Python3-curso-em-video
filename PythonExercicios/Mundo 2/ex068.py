from random import randint
v = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    pi = str(input('Par ou Impar?[P/I]: '))
    if pi in 'IiPp':
        tot = computador + jogador
        if pi in "Ii":
            esc = 'Impar'
            if tot %2 == 0:
                pg = 'Perdeu'
                res = 'Par'
            elif tot %2 != 0:
                pg = 'Ganhou'
                res = 'Impar'
                v += 1
        if pi in "Pp":
            esc = 'Par'
            if tot %2 == 0:
                pg = 'Ganhou'
                res = 'Par'
                v += 1
            elif tot %2 != 0:
                res = 'Impar'
                pg = 'Perdeu'
        print(f'''O computador jogou {computador} e você jogou {jogador}, com um total de {tot}, 
Com o resultado sendo {res} e você escolhendo {esc} Você {pg}!''')
    elif pi not in "IiPp":
        print('Opção inválida!! Tente Noamente.')
    if pg == 'Perdeu':
        break
    print('Vamos Jogar Novamente!')
print(f'Game Over, você ganhou {v} vezes!')
