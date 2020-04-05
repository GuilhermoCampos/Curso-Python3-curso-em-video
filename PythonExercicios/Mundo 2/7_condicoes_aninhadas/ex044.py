print('{:=^40}'.format(' Lojado '))
preco = float(input('Por favor insira o valor do produto: R$'))
print("""FORMAS DE PAGAMENTO:
[ 1 ] Dinheiro ou Cheque
[ 2 ] = à vista no Cartão 
[ 3 ] = até 2x no cartão
[ 4 ] = 3x ou mais no cartão""")
forma = int(input('Por Favor selecione uma opção de pagamento: '))
if forma == 1:
    print(f'O Produto de valor R${preco:.2f} no dinheiro ou cheque fica R${(preco*0.9):.2f} com 10% de desconto')
elif forma == 2:
    print('O Produto de valor R${:.2f} à vista no cartão fica {:.2f} com 5% de desconto'.format(preco, (preco*0.95)))
elif forma == 3:
    print('O Produto de valor R${:.2f} em até 2x no cartão tem o preço normal'.format(preco))
elif forma == 4:
    parcelas = int(input('Quantas parcelas? '))
    print(f'pagando em {parcelas}x no cartão, o produto tem o preço de '
          f'{(preco*1.20)/parcelas:.2f} durante {parcelas} meses com 20% de juros')
else:
    print('A opção é invalida para pagamento pagamento, tente novamente!')