num = [int(input('Digite um número na posição 0: ')),
       int(input('Digite um número na posição 1: ')),
       int(input('Digite um número na posição 2: ')),
       int(input('Digite um número na posição 3: ')),
       int(input('Digite um número na posição 4: '))]
maior = max(num)
menor = min(num)
indexmaior = indexmenor = 0
print(f'Você digitou os números: {num}')
print(f'O Maior número é {max(num)} e está nas posições: ', end='')
for p, n in enumerate(num):
    if maior == n:
        indexmaior = num.index(maior, p)
        print(indexmaior, end=' ')
print(f'\nO menor número é {menor} e está nas posições: ', end='')
for p, n in enumerate(num):
    if menor == n:
        indexmenor = num.index(menor, p)
        print(indexmenor, end=' ')
