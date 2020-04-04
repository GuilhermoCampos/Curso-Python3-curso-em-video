# def lin():
#    print('-'*30)


# lin()
# print(f'{"Curso em Vídeo":^30}')
# lin()
# lin()
# print(f'{"Aprenda Python":^30}')
# lin()
# lin()
# print(f'{"Gustavo Guanabara":^30}')
# lin()

# def mensagem(txt):
#    print('-'*30)
#    print(f'{txt:^30}')
#    print('-'*30)


# mensagem('Curso em Video')
# mensagem('Python')
# mensagem('Gustavo Guanabara')

# def soma(a, b):
#    print(f'A = {a} B = {b}')
#    s = a + b
#    print(f'A soma de A + B = {s}')


# soma(b=4, a=5)
# soma(8, 9)
# soma(2, 1)

# def contador(*num):
#    for c in num:
#        print(c, end=' ')
#    print('Fim')


# contador(2, 1, 7)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
