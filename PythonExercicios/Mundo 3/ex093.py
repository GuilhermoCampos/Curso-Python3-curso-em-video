# Um programa que gerencia o aproveitamento de um jogador de futebol.
# O program lê o nome do jogador e quantas partidas ele jogou.
# Depois lê a quantiade de gols feitos em cada partida. no final
# tudo isso deve ser guardado em um dicionário, incluindo o total de gols
# feitos durante o campeonato.
jogador = dict()
partidas = list()
tot = 0
jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
jogador['partidas'] = int(input('Nº de partidas: '))
for c in range(0, jogador['partidas']):
    gols = int(input(f'Gols feitos na patida {c}: '))
    partidas.append(gols)
    tot += gols
jogador['gols'] = partidas; jogador['total'] = tot
print('-='*62)
print(jogador)
print('-='*62)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*62)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]}.')
for p, g in enumerate(jogador['gols']):
    print(f'→ Na partida {p}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
