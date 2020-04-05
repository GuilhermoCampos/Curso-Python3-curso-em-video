d = 0
co = 0
for c in range(1, 7):
    valor = int(input('Digite o {}º Valor: '.format(c)))
    if valor % 2 == 0:
        d += valor
        co += 1
print('Você informou {} números PARES e a soma foi {}'.format(co, d))
