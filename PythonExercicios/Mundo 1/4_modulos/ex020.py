from random import sample
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))
list = [n1, n2, n3, n4]
res = sample(list, 4)
print('A Ordem do trabalho é:\n {}'.format(res))
