def funcao(a=''):
    """
    Documentaçao da função
    onde tem variavel opcional
    :return: sem retorno
    """
    global variavel
    variavel = 'Local'
    a = "nada"
    print(f'A variavel Local tem valor {variavel}')
    return variavel


help(funcao)
print('-='*10)
print(funcao.__doc__)

# Programa Principal
variavel = 'Global'
print(f'A variavel Global tem valor {variavel}')
funcao()
print(f'O local do lado de fora retorna {funcao()}')
