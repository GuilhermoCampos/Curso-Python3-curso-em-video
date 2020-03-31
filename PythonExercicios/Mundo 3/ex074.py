from random import randint
sort = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os números sorteados foram: ', end='')
maior = menor = cont = 0
for sorteados in sort:
    print(sorteados, end=' ')
print(f'\nO maior número foi {max(sort)}')
print(f'O menor número foi {min(sort)}')
#for maiormenor in sort:
#    if cont == 0 or menor > sort[cont]:
#        menor = sort[cont]
#    if cont == 0 or maior < sort[cont]:
#        maior = sort[cont]
#    cont += 1
#print('\n', f'O maior número foi {maior}')
#print(f' O menor número foi {menor}')
