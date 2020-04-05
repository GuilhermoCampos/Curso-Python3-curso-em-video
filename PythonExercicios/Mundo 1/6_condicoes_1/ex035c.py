print('-=-'*20, '\n                Analisador de Triangulos\n', '-=-'*20)
n1 = float(input('Primeiro seguimento: '))
n2 = float(input('Segundo seguimento: '))
n3 = float(input('Terceiro seguimento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print('Os seguimentos acima PODEM formar um triangulo!')
else:
    print('Os seguimentos acima NÃO formam um triangulo!')
