n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
if n1 > n2 > n3:
    print('O maior numero é {}, e o menor é {}'.format(n1, n3))
if n2 > n3 > n1:
    print('O maior número é {}, e o menor é {}'.format(n2, n1))
if n3 > n1 > n2:
    print('O maior número é {}, e o menor é {}'.format(n3, n2))
if n1 > n3 > n2:
    print('O maior número é {}, e o menor é {}'.format(n1, n2))
if n2 > n1 > n3:
    print('O maior número é {}, e o menor é {}'.format(n2, n3))
if n3 > n2 > n1:
    print('O maior número é {}, e o menor é {}'.format(n3, n1))
