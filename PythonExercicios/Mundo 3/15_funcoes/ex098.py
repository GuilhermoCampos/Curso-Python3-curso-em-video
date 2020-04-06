# Programa que tem ua função chamada contador(), que recebe três parãmetros: inicio, fim e passo.
# O programa tem que realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada.
from time import sleep


def contador(inicio, fim, passo):
    print('-=' * 30)
    final = passos = 0
    if passo == 0:
        passo = passos = 1
    if inicio > fim and passo > 0:
        passo *= -1
    elif inicio < fim and passo < 0:
        passo *= -1
    if fim > 0:
        final = fim + 1
    elif fim <= 0:
        final = fim - 1
    if passo < 0:
        passos = passo * -1
    print(f'Contagem de {inicio} até {fim} de {passos} em {passos}:')
    for c in range(inicio, final, passo):
        print(c, end=' ')
        sleep(0.5)
    print('FIM!')
    print('-=' * 30)


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Contagem personalizada!')
ini = int(input('Inicio: '))
fi = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fi, pas)
