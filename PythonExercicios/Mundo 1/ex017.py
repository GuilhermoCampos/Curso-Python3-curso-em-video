from math import hypot
op = float(input('Digite o Cateto Oposto: '))
ad = float(input('Digite o Cateto Adjacente: '))
print('Dado o Cateto Oposto {} e o Cateto Adjacente {} A Hipotenusa é {:.2f}'.format(op, ad, hypot(op, ad)))
