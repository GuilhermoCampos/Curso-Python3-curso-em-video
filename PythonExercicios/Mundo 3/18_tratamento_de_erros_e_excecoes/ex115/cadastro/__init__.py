import time
lista = list()


def iniciarMenu():
    while True:
        escolha = 0
        print('-' * 60)
        print(f'{"Menu Principal":^60}')
        print('-' * 60)
        print('\033[33m1\033[m - \033[34m Ver pessoas cadastradas\033[m')
        print('\033[33m2\033[m - \033[34m Cadastrar nova Pessoa\033[m')
        print('\033[33m3\033[m - \033[34m Sair do Sistema\033[m')
        print('-' * 60)
        escolha = menuOpcao('Sua Opção')
        if escolha == 1:
            listar()
        elif escolha == 2:
            cadastrar()
        elif escolha == 3:
            print('-' * 60)
            print(f'{"Saindo do sistema... Até logo":^60}')
            print('-' * 60)
            time.sleep(2)
            break


def cadastrar():
    pessoa = dict()
    while True:
        try:
            nome = str(input('Nome: '))
        except:
            ('\033[31mNão foi possivel adicionar o nome, tente novamente!\033[m')
            continue
        else:
            print('\033[32mNome adicionado com sucesso!\033[m')
            break
    while True:
        try:
            idade = int(input('Idade: '))
        except:
            ('\033[31mNão foi possivel adicionar a idade, tente novamente!\033[m')
            continue
        else:
            print('\033[32mIdade adicionada com sucesso!\033[m')
            break
    pessoa['nome'] = nome
    pessoa['idade'] = idade
    lista.append(pessoa.copy())
    pessoa.clear()
    return lista


def listar():
    print('-' * 60)
    print(f'{"Nome":<37}{"idade":<8}')
    print('-' * 60)
    for c in lista:
        print(f'{c["nome"]:<37}{c["idade"]:>3}{"anos":>5}')
    if len(lista) == 0:
        print(f'\033[31m{"Lista Vazia":^45}\033[m')
    print('-' * 60)
    input('Enter para continuar')


def menuOpcao(msg):
    while True:
        try:
            num = int(input(f'\033[32m{msg}: \033[m'))
        except:
            print('\033[31mERRO: Por favor insira uma opção válida!\033[m')
        else:
            if 0 < num < 4:
                return num
            else:
                print('\033[31mERRO: Por favor insira uma opção válida!\033[m')
                continue