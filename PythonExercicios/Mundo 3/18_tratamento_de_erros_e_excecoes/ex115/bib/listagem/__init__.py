def interpretar(arquivo):
    """
    Funçaõ que pega uma lista retornado da função ler e a trasforma em uma lista
    que separa nome e idade da pessoa cadastrada
    :param arquivo: Arquivo a ser interpretado
    :return: lista dividida em dicionarios organizados com nome e idade.
    """
    dicionario = dict()
    lista = list()
    try:
        for c in range(0, len(arquivo), 2):
            dicionario['nome'] = arquivo[c].replace('\n', '')
            dicionario['idade'] = int(arquivo[c+1].replace('\n', ''))
            lista.append(dicionario.copy())
            dicionario.clear()
    except Exception as erro:
        print('Não foi possivel interpretar essa lista\n erro: ', end='')
        print(erro.__class__)
    else:
        return lista


def listar(lista):
    """
    Função que mostra na tela os dados de forma formatada a interface.
    :param lista: lista com dicionarios organizados em nome e idade
    """
    print('-' * 60)
    print(f'{"Nome":<37}{"idade":<8}')
    print('-' * 60)
    for c in lista:
        print(f'{c["nome"]:<37}{c["idade"]:>3}{"anos":>5}')
    if len(lista) == 0:
        print(f'\033[31m{"Lista Vazia":^45}\033[m')
    print('-' * 60)
    input('Enter para continuar')

