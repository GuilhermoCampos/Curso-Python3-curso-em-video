# Programa que tem uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador
# e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum
# dado não tenha sido informado corretamente.


def ficha(jogador='<Desconhecido>', gols=0):
    print(f'O {jogador} fez {gols} gols no campeonato.')


# Programa Principal
nome = str(input('Nome: ')).strip().capitalize()
gol = str(input('Gols: '))
if nome == '' and gol == '' or nome == '' and gol.isnumeric() is False:
    ficha()
elif nome == '' and gol.isnumeric():
    gol = int(gol)
    ficha(gols=gol)
elif gol == '' or gol.isnumeric() is False:
    ficha(jogador=nome)
elif gol.isnumeric():
    gol = int(gol)
    ficha(nome, gol)
