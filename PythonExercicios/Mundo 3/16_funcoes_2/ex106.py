# Um mini sistema que utiliza o interactie help do python.
# O Usuário vai digitar o comando e o manual ai aparecer.
# Quando o usuário digitar a palara 'FIM', o programa se encerrará.


def printcor(titulo):
    from time import sleep
    tam = 0
    texto = ' '
    if titulo == 1:
        texto = 'SISTEMA DE AJUDA PyHELP'
        tam = len(texto)
        print('\033[30:42m~\033[m' * (tam + 4))
        print(f'\033[30:42m  {texto}  \033[m')
        print('\033[30:42m~\033[m' * (tam + 4),)
    elif titulo == 2:
        texto = f'Acessando Manual do comando "{comando}"'
        tam = len(texto)
        print('\033[30:44m~\033[m' * (tam + 4))
        print(f'\033[30:44m  {texto}  \033[m')
        print('\033[30:44m~\033[m' * (tam + 4))
    elif titulo == 3:
        texto = 'ATÉ LOGO'
        tam = len(texto)
        print('\033[30:41m~\033[m' * (tam + 4))
        print(f'\033[30:41m  {texto}  \033[m')
        print('\033[30:41m~\033[m' * (tam + 4))
    sleep(1)


def comahelp(command):
    from time import sleep
    sleep(1)
    print('\033[7m', end='')
    help(comando)
    print('\033[m', end='')
    sleep(1)


while True:
    printcor(1)
    comando = str(input('Função ou Biblioteca >')).strip().lower()
    if comando == 'fim':
        printcor(3)
        break
    else:
        printcor(2)
        comahelp(comando)
