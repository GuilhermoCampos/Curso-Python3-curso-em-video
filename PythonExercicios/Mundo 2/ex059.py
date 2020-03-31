from time import sleep
close = False
print('{}''\n       {:^}\n''{}'.format('-='*20, 'Bem Vindo a Calculadora!!!', '=-'*20))
privalor = int(input('Digite o Primeiro Valor: '))
segvalor = int(input('Digite o Segundo Valor: '))
while not close:
    print('''    [1] Somar
    [2] Subtrair
    [3] Multiplicar
    [4] Dividir
    [5] Porcentagem
    [6] Número Elevado
    [7] Maior Número
    [8] Digitar Novamente
    [9] Sair do Programa''')
    opcao = int(input('O Que você deseja Fazer?: '))
    if opcao == 1:
        total = privalor + segvalor
        sleep(1)
        print('O Resultado da Soma de {} + {} é {}'.format(privalor, segvalor, total))
    elif opcao == 2:
        total = privalor - segvalor
        sleep(1)
        print('O Resultado da Subtração de {} - {} é {}'.format(privalor, segvalor, total))
    elif opcao == 3:
        total = privalor * segvalor
        sleep(1)
        print('O Resultado da Multiplicação de {} x {} é {}'.format(privalor, segvalor, total))
    elif opcao == 4:
        total = privalor / segvalor
        sleep(1)
        print('O Resultado da Divisão de {} ÷ {} é {}'.format(privalor, segvalor, total))
    elif opcao == 5:
        total = privalor * (segvalor / 100)
        sleep(1)
        print('A porcentagem de {}% de {} é {}'.format(segvalor, privalor, total))
    elif opcao == 6:
        total = privalor ** segvalor
        sleep(1)
        print('O Número {} elevado a {} é {}'.format(privalor, segvalor, total))
    elif opcao == 7:
        if privalor > segvalor:
            total = privalor
        else:
            total = segvalor
        sleep(1)
        print('O Maior Valor entre {} e {} é {}'.format(privalor, segvalor, total))
    elif opcao == 8:
        privalor = int(input('Digite novamente o º1 valor: '))
        segvalor = int(input('Digite novamente o º2 valor: '))
    elif opcao == 9:
        close = True
        print('Obrigado por Utilizar a Calculadora e Volte Sempre!!! :D')
    else:
        print('Opção Inválida, Tente Novamente!!!')
    print('{}'.format('='*56))
    sleep(5)
