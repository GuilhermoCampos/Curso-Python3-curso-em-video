total = int(input('Valor a ser sacado: R$'))
valor = 100
ced = 0
while True:
    if total >= valor:
        total -= valor
        ced += 1
    else:
        if ced > 0:
            print(f'São {ced} cédulas de R${valor}')
        if total < 100:
            valor = 50
        if total < 50:
            valor = 20
        if total < 20:
            valor = 10
        if total < 10:
            valor = 5
        if valor <= 5:
            valor = 1
        ced = 0
        if total == 0:
            break
