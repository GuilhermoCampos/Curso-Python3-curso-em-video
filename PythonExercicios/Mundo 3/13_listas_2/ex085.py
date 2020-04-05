numeros = list()
pares = list()
impares = list()
for c in range(1, 8):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
pares.sort()
impares.sort()
numeros.append(pares[:])
numeros.append(impares[:])
print('Os números impares digitados foram: ', end='')
for i in impares:
    print(i, end=', ')
print('\nOs números pares digitados foram: ', end='')
for p in pares:
    print(p, end=', ')
