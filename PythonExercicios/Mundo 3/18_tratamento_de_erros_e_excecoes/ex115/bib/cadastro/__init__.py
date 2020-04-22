from bib.arquivo import *


def cadastrar(path):
    """
    Função que cadastra uma pessoa no arquivo a ser salvo
    :param path: caminho do arquivo
    """
    pessoa = dict()
    while True:
        try:
            nome = str(input('Nome: '))
        except:
            print('\033[31mNão foi possivel adicionar o nome, tente novamente!\033[m')
            continue
        else:
            print('\033[32mNome adicionado com sucesso!\033[m')
            break
    while True:
        try:
            idade = int(input('Idade: '))
        except:
            print('\033[31mNão foi possivel adicionar a idade, tente novamente!\033[m')
            continue
        else:
            print('\033[32mIdade adicionada com sucesso!\033[m')
            break
    try:
        salvar(path, nome)
        salvar(path, idade)
    except:
        print('\033[31mNão foi possivel salvar os dados\033[m')
    else:
        print('\033[33mSalvo com Sucesso!\033[m')

