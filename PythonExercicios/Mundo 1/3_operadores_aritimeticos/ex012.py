pro = float(input('Qual o preço do produto?: R$'))
desc = pro - float(pro*0.05)
print('Este produto na promoção irá custar R${:.2f}, pois tem 5% de desconto'.format(desc))
