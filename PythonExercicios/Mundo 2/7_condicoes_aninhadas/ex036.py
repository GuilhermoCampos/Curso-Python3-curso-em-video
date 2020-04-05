print('-=-'*24)
print('  ', 'Bom Dia! Bem Vindo ao teste de crédito para emprestimo bancário!')
print('-=-'*24)
casa = float(input('Por favor insira o valor da casa: R$'))
salario = float(input('Por Favor insira a sua renda: R$'))
tempo = float(input('Por Favor diga em quantos anos pretende pagar: '))
prestacao = casa / (tempo * 12)
if prestacao > (salario * 0.30):
    print('Desculpe! Mas seu empréstimo foi \033[1;31mNEGADO\033[m!!!', end='')
    print('Pois excede 30% do seu salário, o valor da prestação seria de R${:.2f}'.format(prestacao))
else:
    print('Parabéns! O seu pedido de empréstimo foi \033[32mAPROVADO\033[m', end='')
    print('o valor mensal é de R$\033[33m{:.2f}\033[m'.format(prestacao))
