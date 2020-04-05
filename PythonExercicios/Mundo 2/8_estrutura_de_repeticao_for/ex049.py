num = int(input('Escolha um número para mostrar sua tabuada: '))
for c in range(1, 100):
    print('{} x {:2} = {:2}'.format(num, c, c * num))
