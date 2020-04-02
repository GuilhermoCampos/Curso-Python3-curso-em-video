# Aprimorar o ex093 para que funcione com vários jogadores,
# incluindo um sistema de vizualização de detalhes
# de aproveitamento de cada jogador
jogadores = list()
jogador = dict()
partidas = list()
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    jogador['partidas'] = int(input(f'Nº de partidas de {jogador["nome"]}: '))
    for c in range(0, jogador['partidas']):
        gols = int(input(f'Gols feitos na partida {c}: '))
        partidas.append(gols)
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    jogadores.append(jogador.copy())
    jogador.clear()
    partidas.clear()
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar not in "SN":
        while continuar not in "SN":
            print('ERRO! Digite apenas Sim ou Não')
            continuar = str(input('Deseja Continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-='*62)
print(f'{"COD"}', f'{"Nome":<15}', f'{"Gols":<15}', f'Total')
print('-'*42)
for k, v in enumerate(jogadores):
        print(f' {k}  {v["nome"]:<14}  {v["gols"]} {v["total"]:>7}')
print('-'*42)
while True:
    dados = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if dados == 999:
        break
    else:
        print(f'Levantamento do jogador {jogadores[dados]["nome"]}:')
        for p, g in enumerate(jogadores[dados]['gols']):
            print(f'→ Na partida {p} fez {g} gols.')
