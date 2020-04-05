num = (int(input('Digite um número: ')), int(input('Digite outro valor: ')),
       int(input('Digite mais um valor:')), int(input('Digite o último valor: ')))
print(f'Você digitou os números {num},')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3) + 1}ª posição')
else:
    print('O número 3 não foi digitado')
print(f'Os números pares foram: ', end='')
for par in range(0, 4):
    if num[par] % 2 == 0:
        print(num[par], end=', ')
