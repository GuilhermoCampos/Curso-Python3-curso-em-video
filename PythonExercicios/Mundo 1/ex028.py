from random import randint
from time import sleep
a = randint(0, 5)
n = int(input('Estou pensando em um número inteiro de 0 a 5, tente adivinhar qual é: '))
print('-----Verificando-----')
sleep(2)
if a == n:
    print('Parabéns você adivinhou!! :D')
else:
    print('Que pena! O Computador vence! ele pensou em {}'.format(a))
