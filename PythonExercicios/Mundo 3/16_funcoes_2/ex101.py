# Programa que tem uma função chamada voto() que vai receber como parâmetro
# o anom de nascimento de uma pessoa, retornando um valor literal indicando
# se uma pessoa tem voto NEGADO, OPICIONAL ou OBRIGATÓRIO nas eleições


def voto(nasc):
    import time
    atual = time.localtime().tm_year
    idade = atual - nasc
    if idade >= 60 or 14 <= idade <= 17:
        obrigatoriedade = "Voto Opicional"
    elif 18 <= idade < 60:
        obrigatoriedade = "Voto Obrigatório"
    else:
        obrigatoriedade = "Não Vota"
    return [idade, obrigatoriedade]


# Programa Principal
nasc = int(input('Em que ano você nasceu?: '))
resultado = voto(nasc)
print(f'com {resultado[0]} anos: {resultado[1]}')
