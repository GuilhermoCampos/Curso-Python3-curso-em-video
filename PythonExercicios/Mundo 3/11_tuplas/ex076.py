lista = ('Lápis', 1.50, 'Caderno', 8, 'Lápiseira', 5, 'Caneta', 2,
         'Borracha', 0.50, 'Tesoura', 2.50, 'Cola', 1, 'Mochila',
         50, 'Estojo', 10, 'Lápis de cor', 20, 'Corretivo', 1.50)
print('-'*59)
print(f'{"Tabela de Preços":^59}')
print('-'*59)
cont = 0
listas = len(lista) // 2
for c in range(0, listas):
    print(f'{lista[cont]:.<50}', end ='')
    cont += 1
    print(f'RS{lista[cont]:>7.2f}')
    cont += 1
print('-'*59)
