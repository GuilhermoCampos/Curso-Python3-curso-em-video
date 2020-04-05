from random import randint
from time import sleep
posi = list()
maior = 0
jogadores = dict()
jogadores['jogador1'] = randint(1, 6)
jogadores['jogador2'] = randint(1, 6)
jogadores['jogador3'] = randint(1, 6)
jogadores['Jogador4'] = randint(1, 6)
print('Valoes sorteados:')
for j, p in jogadores.items():
    print(f'O {j} tirou {p}')
    sleep(1)
print('Ranking dos Jogadores: ')
for c in jogadores:
    posi.append(jogadores[c])
posi.sort(reverse=True)
pos = 0
for c in jogadores.values():
    if c == posi[pos]:
        print(c)
    pos += 1
print(posi)
