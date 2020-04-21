def listar(lista):
    print('-' * 60)
    print(f'{"Nome":<37}{"idade":<8}')
    print('-' * 60)
    for c in lista:
        print(f'{c["nome"]:<37}{c["idade"]:>3}{"anos":>5}')
    if len(lista) == 0:
        print(f'\033[31m{"Lista Vazia":^45}\033[m')
    print('-' * 60)
    input('Enter para continuar')

