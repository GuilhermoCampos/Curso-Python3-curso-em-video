num = list()
for c in range(0, 5):
    nume = (int(input('Digite um número: ')))
    if c == 0:
        num.append(nume)
    for n, p in enumerate(num):
        if nume < p:
            num.insert(n, nume)
            break
        else:
            for g in num:
                if nume > p and nume > g+1:
                    num.append(nume)
                break

print(num)
