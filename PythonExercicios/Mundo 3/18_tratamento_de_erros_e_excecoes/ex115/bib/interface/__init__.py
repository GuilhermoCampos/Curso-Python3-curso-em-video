def leiaInt(msg):
    """
    Função que aceita apenas a entrada de números inteiros, retornando erro a todos que não sejam numeros inteiros.
    :param msg: Mensagem que será mostrada no momento da inserção de dados
    :return:Número inteiro
    """
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
    """
    Função que faz uma linha de acordo com o tamanho inserido
    :param tam: tamanho em caracteres da linha
    """
    lin = '-' * tam
    print(lin)


def cabecalho(txt):
    """
    Cabeçalho contendo o titulo do programa
    :param txt: texto titulo
    """
    print(f'{txt:^60}')


def menu(lista):
    """
    Função que mostra um menu e solicida a insersão de um número inteiro representando um item da lista.
    :param lista: lista com as opções que serão mostradas no menu
    :return: opção selecionada
    """
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

