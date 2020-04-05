n = int(input('Digite o número do qual quer seu fatorial: '))
c1 = n + 1
f = 1
for c in range(0, n):
    print('{}'.format(c1), end='')
    print(' x ' if c1 > 2 else ' = ', end='')
    #if c1 > 0:
    c1 -= 1
    f *= c1
print(f)