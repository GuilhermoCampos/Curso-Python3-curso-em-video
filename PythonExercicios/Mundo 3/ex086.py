matriz = list()
vertical = list()
horizontal = list()
for v in range(0, 3):
    for h in range(0, 3):
        horizontal.append(int(input(f'Digite um valor para [{v}, {h}]: ')))
    vertical.append(horizontal[:])
    horizontal.clear()
    matriz.append(vertical[:])
    vertical.clear()
for m in matriz:
    for t in m:
        for p in t:
            print(f'[ {p:^3} ]', end='')
        print('\n', end='')
