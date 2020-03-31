num = int(input('Digite o valor a ser convertido: '))
base = int(input("""Qual será a base de conversão? sendo: 
\033[34m1\033[m = binário
\033[34m2\033[m = Octal
\033[34m3\033[m = Hexadecimal
Digite: """))
bin = bin(num)
oct = oct(num)
hex = hex(num)
if base == 1:
    print('O Resultado é: {}'.format(bin))
elif base == 2:
    print('O Resultado é: {}'.format(oct))
elif base == 3:
    print('O Resultado é: {}'.format(hex))
