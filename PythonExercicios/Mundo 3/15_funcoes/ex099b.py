from time import sleep


def maior(*num):
    mai = pos = 0
    print('-=' * 30)
    print('Analizando os valores passados...')
    for c in num:
        print(c, end=' ', flush=True)
        sleep(0.5)
        if c > mai or pos == 0:
            mai = c
        pos += 1
    sleep(2)
    sleep(1)
    print(f'Foram informados {len(num)} valores ao todo.')
    sleep(2)
    print(f'O maior valor informado foi {mai}')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
sleep(1)
maior(4, 7, 0)
sleep(1)
maior(1, 2)
sleep(1)
maior(6)
sleep(1)
maior()
