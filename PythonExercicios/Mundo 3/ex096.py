# Programa com função área, que recebe as dimensões de um terreno retangular (largura e compriento)
# e mostra a área do terreno


def area(comp, larg):
    a = comp * larg
    print(f'A área de {comp}m x {larg}m é de {a}m².')

print('Controle de terrenos')
print('-'*20)
c = float(input('Largura (m): '))
b = float(input('Comprimento (m):  '))
area(c, b)
