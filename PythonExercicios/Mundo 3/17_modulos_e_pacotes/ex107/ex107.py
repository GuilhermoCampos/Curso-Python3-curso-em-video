# Crie um módulo chamado moeda.py que tenha as funções 
# incorporadas aumentar(), diminuir(), doro() e metade.
# Faça também um programa que importe esses módulo e
# use algumas dessas funções
import moeda
# from ex107 import moeda

num = float(input('Digite um valor: '))

print(f'O dobro do valor {num} é {moeda.dobro(num)}')
print(f'A metade do valor {num} é {moeda.metade(num)}')
print(f'O valor {num} aumentado em 10% é {moeda.aumentar(num, 10)}')
print(f'O valor {num} diminuido em 10% é {moeda.diminuir(num, 10)}')
