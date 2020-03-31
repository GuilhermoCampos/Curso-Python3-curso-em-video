while True:
    num = int(input('Qual número você deseja ver a tabuada?[Negativo para parar]: '))
    if num < 0:
        break
    for c in range(1, 11, 1):
        print(f'{num} x {c} = {num*c}')
    print('-'*63)
print('Fim!')
