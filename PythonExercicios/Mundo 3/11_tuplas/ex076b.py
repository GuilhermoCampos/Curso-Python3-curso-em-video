lista = ('Lápis', 1.50, 'Caderno', 8, 'Lápiseira', 5, 'Caneta', 2,
         'Borracha', 0.50, 'Tesoura', 2.50, 'Cola', 1, 'Mochila',
         50, 'Estojo', 10, 'Lápis de cor', 20, 'Corretivo', 1.50)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<45}', end='')
    elif pos % 1 == 0:
        print(f'R${lista[pos]:>8.2f}')
