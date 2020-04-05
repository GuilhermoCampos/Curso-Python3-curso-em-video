from time import sleep
resto1 = resto2 = resto3 = 0
print('', '-'*62, f'\n{"Caixa Eletrônico":^62}\n', '-'*62)
saque = int(input('Digite o valor a ser sacado: R$'))
n50 = (saque // 50)
n20 = ((saque % 50) // 20)
n10 = (((saque % 50) % 20) // 10)
n1 = ((((saque % 50) % 20) % 10) // 1)
if n50 >= 1:
    print(f'Total de {n50} celulas de R$50')
if n20 >= 1:
    print(f'Total de {n20:} celulas de R$20')
if n10 >= 1:
    print(f'Total de {n10:} Celulas de R$10')
if n1 >= 1:
    print(f'Total de {n1:} Celulas de R$1')
sleep(10)
