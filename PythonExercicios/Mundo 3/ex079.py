num = list()
while True:
    nov = (int(input('Digite um número: ')))
    if nov not in num:
        num.append(nov)
        print('Número adicionado com sucesso')
    else:
        print('Número repetido, falha ao adicionar')
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break
num.sort()
print(f'Os números digitados foram {num}')
