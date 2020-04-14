def aumentar(num=0, por=0):
    res = num + (num * (por/100))
    return res


def diminuir(num=0, por=0):
    res = num - (num * (por/100))
    return res


def dobro(num=0):
    res = num*2
    return res


def metade(num=0):
    res = num/2
    return res


def moeda(valor=0, moeda='R$'):
    return f'{moeda} {valor:.2f}'.replace('.', ',')
