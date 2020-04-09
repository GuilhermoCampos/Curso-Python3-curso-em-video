# Programa que tem uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e colocá-los dentro da lista e a segunda função
# vai mostrar a soma entre os valores PARES sorteados pela função anterior.
from time import sleep
from random import randint


def sorteia(num):
    print('Sorteando 5 valores da lista: ', end=' ')
    for c in range(0, 5):
        num.append(randint(1, 9))
        print(num[c], end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')


def somaPar(num):
    print(f'Somando os valores pares de {num},', end=' ')
    parsoma = 0
    for c in num:
        if c % 2 == 0:
            parsoma += c
    sleep(2)
    print(f'Temos {parsoma}')


# Programa Principal
numeros = list()
sorteia(numeros)
sleep(1)
somaPar(numeros)
