# Programa que tem uma função chamada maior(), que recebe vários parâmetros com valores inteiros,
# deve analizar todos os valores e dizer qual deles é o maior
from time import sleep


def maior(*num):
    mai = pos = 0
    print('-=' * 30)
    print('Analizando os valores passados...')
    for c in num:
        print(c, end=' ')
        sleep(0.5)
    sleep(1)
    print(f'Foram informados {len(num)} valores ao todo.')
    for c in range(0, len(num)):
        if num[c] > mai or pos == 0:
            mai = num[c]
        pos += 1
    sleep(2)
    print(f'O maior valor informado foi {mai}')


maior(2, 9, 4, 5, 7, 1)
sleep(1)
maior(4, 7, 0)
sleep(1)
maior(1, 2)
sleep(1)
maior(6)
sleep(1)
maior()
