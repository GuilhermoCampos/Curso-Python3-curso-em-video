from random import randint
from time import sleep
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
pos = 1
for item in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f'{pos}º lugar {item} com {jogadores[item]}')
    sleep(1)
    pos += 1
