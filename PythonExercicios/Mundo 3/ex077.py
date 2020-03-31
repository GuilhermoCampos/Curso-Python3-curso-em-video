lis = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',
       'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
       'PROGRAMADOR', 'FUTURO')
for pal in lis:
    print(f'\nNa palavra {pal} temos: ',end='')
    if 'A' in pal:
        print('a', end=' ')
    if 'E' in pal:
        print('e', end=' ')
    if 'I' in pal:
        print('i', end=' ')
    if 'O' in pal:
        print('o', end=' ')
    if 'U' in pal:
        print('u', end=' ')
