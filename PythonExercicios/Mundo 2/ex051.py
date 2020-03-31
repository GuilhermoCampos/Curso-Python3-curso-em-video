print('{}\n {:^25}\n {}\n'.format('='*25, '10 TERMOS DE UMA PA', '='*25), end=' ')
primeiro = int(input('Primeiro Termo: '))
razao = int(input(' Razão: '))
acumulador = 0
for c in range(0, 10):
    print(primeiro + acumulador, '=> ', end='')
    acumulador += razao
print('ACABOU')
