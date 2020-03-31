nome = str(input('Digite o seu nome completo: ')).strip().split()
print('Muito Prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
