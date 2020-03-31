v1 = int(input('Adicione o primeiro valor: '))
v2 = int(input('Adicione o segundo valor: '))
if v1 > v2:
    print('O \033[34mPrimeiro\033[m valor que é {} é o maior.'.format(v1))
elif v2 > v1:
    print('O \033[32mSegundo\033[m valor ou seja {} é o maior.'.format(v2))
elif v1 == v2:
    print('\033[31mNÃO\033[m Existe valor maior, os dois são \033[33mIGUAIS\033[m')