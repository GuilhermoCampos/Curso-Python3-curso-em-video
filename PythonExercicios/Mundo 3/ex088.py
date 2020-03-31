from random import randint
from time import sleep
total = list()
jogo = list()
print('-'*42)
print(f'{"JOGA NA MEGA SENA":^42}')
print('-'*42)
quant = int(input('Quantos jogos você quer que eu sorteie?: '))
print('-='*5, f' SORTEANDO {quant} JOGOS ', '=-'*5)
for c in range(0, quant):
    while len(jogo) != 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    total.append(jogo[:])
    jogo.clear()
for n, j in enumerate(total):
    print(f'Jogo {n+1}: {j}')
    sleep(1)
print('-='*6, '< BOA SORTE! >', '=-'*6)
