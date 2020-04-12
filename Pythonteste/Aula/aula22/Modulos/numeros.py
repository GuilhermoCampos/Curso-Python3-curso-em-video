from uteis import numeros
from time import sleep
num = int(input('Digite um número: '))
fat = numeros.fatorial(num)
print(f'O Fatorial de {num} é {fat}')
print(f'O doro de {num} é {numeros.dobro(num)}')
sleep(5)
