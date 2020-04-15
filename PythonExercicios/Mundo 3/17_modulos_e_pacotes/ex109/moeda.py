def aumentar(num=0, por=0, form=False,):
    """
    Função que aumenta um valor de acordo com uma porcentagem
    :param num: Valor a ser aumentado
    :param por: Porcentagem do valor a ser adicionada
    :param form: Se o número vai ser formatado ou não
    :return: O valor com a porcentagem adicionada, se o param form for verdade
    o valor também será formatado em R$
    """
    res = num + (num * (por/100))
    if form:
        res = moeda(res)
    return res


def diminuir(num=0, por=0, form=False):
    """
    Função que diminui um valor de acordo com uma porcentagem
    :param num: Valor a ser diminuido
    :param por: Porcentagem do valor a ser retirada
    :param form: Se o número vai ser formatado ou não
    :return: O valor sem a porcentagem que lhe foi retirada

    """
    res = num - (num * (por/100))
    if form:
        res = moeda(res)
    return res


def dobro(num=0, form=False):
    """
    Função que retorna o dobro de um valor
    :param num: Valor a ser calculado
    :param form: se o valor será formatado ou não
    :return: Valor passado em seu dobro
    """
    res = num*2
    return res if not form else moeda(res)


def metade(num=0, form=False):
    """
     Função que retorna a metade de um valor
     :param num: Valor a ser calculado
     :param form: se o valor será formatado ou não
     :return: Valor passado em sua metade
     """
    res = num/2
    return res if form is False else moeda(res)


def moeda(valor=0.0, moeda='R$'):
    """
    Funçao que formata um valor ao formato de moeda
    :param valor: Valor a ser formatado
    :param moeda: Moeda ao qual deve ser formatado
    :return: Valor formatado na moeda desejada
    """
    return f'{moeda} {valor:.2f}'.replace('.', ',')
