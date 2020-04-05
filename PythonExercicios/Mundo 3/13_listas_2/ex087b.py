matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = sh3 = mv2 = 0
for h in range(0, 3):
    for v in range(0, 3):
        matriz[h][v] = int(input(f'Digite um valor para [{h}, {v}]: '))
        if matriz[h][v] % 2 == 0:
            spar += matriz[h][v]
        if v == 0 or matriz[1][v] > mv2:
            mv2 = matriz[1][v]
    sh3 += matriz[h][2]
for hori in range(0, 3):
    for vert in range(0, 3):
        print(f'[{matriz[hori][vert]:^5}]', end='')
    print()
print(f'A soma de todos os valores pares digitados é {spar}')
print(f'A soma dos valores da terceira coluna é {sh3}')
print(f'O Maior valor da segunda linha é {mv2}')