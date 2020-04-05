num = []
for c in range(0, 5):
    num.append(int(input(f'Digite u número na {c}ª posição :')))
maior = max(num)
menor = min(num)
print(f'Você digitou os números: {num}')
print(f'O Maior número é {maior} e está nas posições: ', end='')
for p, n in enumerate(num):
    if maior == n:
        print(p, end=' ')
print(f'\nO menor número é {menor} e está nas posições: ', end='')
for p, n in enumerate(num):
    if menor == n:
        print(p, end=' ')
