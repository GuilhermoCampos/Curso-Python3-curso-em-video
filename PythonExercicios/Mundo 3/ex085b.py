num = [[], []]
for c in range(0, 7):
    valor = int(input(f'Digite o {c+1}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    if valor % 2 != 0:
        num[1].append(valor)
num[0].sort(), num[1].sort()
print(f'Os números PARES foram: {num[0]}')
print(f'Os números IMPARES foram: {num[1]}')
