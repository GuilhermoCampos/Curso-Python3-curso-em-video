n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))
if n1 > n2 >= n3:
    ma = n1
    so = n2 + n3
elif n2 > n3 >= n1:
    ma = n2
    so = n3 + n1
elif n3 > n1 >= n2:
    ma = n3
    so = n1 + n2
elif n3 > n2 >= n1:
    ma = n3
    so = n2 + n1
elif n2 > n1 >= n3:
    ma = n2
    so = n3 + n1
elif n1 > n3 >= n2:
    ma = n1
    so = n3 + n2
if ma >= so:
    print('Essas retas não formam um triangulo!')
else:
    print('Essas retas formam um triangulo!')

