num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print(' O Numero {} foi divisível {} vezes'.format(c, tot))
if tot == 2:
    print('E Por isso ele É PRIMO!')
else:
    print('E Por isso ele NÃO É PRIMO!')
