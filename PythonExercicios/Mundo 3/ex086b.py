matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for v in range(0, 3):
    for h in range(0, 3):
        matriz[v][h] = int(input(f'Posição [{v}, {h}]: '))
for vert in range(0, 3):
    for hori in range(0, 3):
        print(f'[{matriz[vert][hori]:^5}]', end='')
    print()
