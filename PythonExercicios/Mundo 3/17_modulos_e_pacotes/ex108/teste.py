# Adapte o código do ex107, criando uma função adicional
# chamada moeda() que consiga mostrar os valores como um 
# valor monetário formatado

import moeda

num = float(input('Digite um valor: '))

print(f'O dobro do valor {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'A metade do valor {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O valor {moeda.moeda(num)} aumentado em 10% é {moeda.moeda(moeda.aumentar(num, 10))}')
print(f'O valor {moeda.moeda(num)} diminuido em 10% é {moeda.moeda(moeda.diminuir(num, 10))}')
3