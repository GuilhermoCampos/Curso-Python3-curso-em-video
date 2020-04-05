from math import factorial
num = int(input('Digite o número ao qual deseja sua fatorial: '))
total = factorial(num)
ac = 0
print('Calculando {}! = {} '.format(num, num), end='')
for c in range(0, num - 1):
    ac += 1
    print('x {} '.format(num - ac), end='')
print('= {}'.format(total), end='')
