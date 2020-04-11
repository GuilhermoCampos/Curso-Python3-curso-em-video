def ficha(jog='<Desconhecido>', gol=0):
    print(f'Jogador {jog} fez {gol} gols no campeonato.')


# Programa Principal
n = str(input('Nome: '))
g = str(input('Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
