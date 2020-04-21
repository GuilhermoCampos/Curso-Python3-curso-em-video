def leiaInt(msg):
    while True:
        try:
            num = int(input(f'{msg}'))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, Digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar este número\033[m')
            return 0
        else:
            return num


def linha(tam):
    lin = '-' * tam
    print(lin)


def cabecalho(txt):
    print(f'{txt:^60}')


def menu(lista):
    linha(60)
    cabecalho('Menu Principal')
    linha(60)
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    linha(60)
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc

