times = ('Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Botafogo', 'Ceará-SC', 'Corinthians',
         'Coritiba', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional',
         'Palmeiras', 'Bragantino-SP', 'Santos', 'Sport-Recife', 'São Paulo', 'Vasco da Gama')
pos = 0
b = ''
print('-'*62)
print('São os 5 primeiros colocados: ', end='')
for c in range(0, 5):
    if c <= 3:
        d = True
    else:
        d = False
    print(f'{c + 1}º', times[c], end=', ' if d else '.')
print('\n', '-'*62)
print('São os 4 ultimos colocados: ', end='')
for c in range(-1, -5, -1):
    if c >= -3:
        e = True
    else:
        e = False
    print(f'{c +21}º', times[c], end=', ' if e else '.')
print('\n', '-'*62)
alfa = sorted(times)
print('Os times em ordem alfabética são: ', end=', ')
for c in alfa:
    if c <= times[18]:
        b = True
    else:
        b = False
    print(c, end=', ' if b else '.')
print('\n', '-'*62)
nome = str(input('Quer saber onde seu time está? digite o nome: ')).strip()
for c in times:
    pos += 1
    if c == nome:
        print(f'O time {c} está na posição {pos}ª')
print(f'{times.index(nome)+1}ª', nome)
