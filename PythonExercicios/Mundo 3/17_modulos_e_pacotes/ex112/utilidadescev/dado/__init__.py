def  leiadinheiro(texto):
    """
    Função que verifica se o dado inserido é monetário
    :param texto: texto que será mostrado na introdução do dado
    :return: o valor em float
    """
    while True:
        invalido = False
        dinheiro = str(input(texto)).replace(',', '.')
        for c in range(0, len(dinheiro)):
            if dinheiro[c] not in '0123456789.,':
               invalido = True
        if dinheiro == '':
            invalido = True
        if invalido is False:
            break
        elif invalido:
            print(f'\033[31mERRO o preço "{dinheiro}" é inválido.\033[m')
    dinheiro = float(dinheiro)
    return dinheiro
