matz = list()
colv = list()
colh = list()
sopar = soma3 = mai2 = 0
for v in range(0, 3):
    for h in range(0, 3):
        colh.append(int(input(f'Digite um valor para [{v}, {h}]: ')))
    colv.append(colh[:])
    colh.clear()
    matz.append(colv[:])
    colv.clear()
for pos, m in enumerate(matz):
    for pos1, cv in enumerate(m):
        for pos2, ch in enumerate(cv):
            print(f'[ {ch} ]', end='')
            if ch % 2 == 0:
                sopar += ch
            if pos2 == 2:
                soma3 += ch
            if pos == 1:
                if pos2 == 0 or ch > mai2:
                    mai2 = ch
        print('\n', end='')
print(f'A soma dos números pares é {sopar}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {mai2}')
