num = int(input('Digite um número: '))
divisor = 1
testador = 0
for c in range(0, num, 1):
    primo = num / divisor
    divisor += 1
    if primo % 1 == 0:
        print('\033[33m{}\033[m'.format(divisor-1), end=' ')
        testador += 1
    else:
        print('\033[31m{}\033[m'.format(divisor-1), end=' ')
print('\nO Número {} foi divisivel {} vezes'.format(num, testador))
if testador == 2:
    print('O Número {} é Primo!'.format(num))
else:
    print('O Número {} não é Primo!'.format(num, testador))
