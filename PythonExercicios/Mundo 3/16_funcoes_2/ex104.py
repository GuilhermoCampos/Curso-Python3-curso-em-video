# Programa que tenha uma função leiaInt(), que vai funcionar de forma semelhante à função
# input() do pythonm só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n=leiaInt('Digite um n')


def leiaint(texto):
    while True:
        n = str(input(texto))
        num = n.isnumeric()
        if num is False:
            print('\033[31mERRO! digite um número inteiro válido!\033[m')
        elif num:
            return n


# Programa Principal
numero = leiaint('Digite: ')
print(f'Você digitou o número {numero}')
