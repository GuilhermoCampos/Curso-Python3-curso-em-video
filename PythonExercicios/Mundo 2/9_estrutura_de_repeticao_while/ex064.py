num = total = dig = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        total += num
        dig += 1
print('Você digitou {}, E a soma dos números digitados é {}.'.format(dig, total))
