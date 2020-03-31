valor = float(input('Digite o Valor que quer aplicar o desconto: R$'))
desci = float(input('Digite o desconto que quer aplicar: '))
descf = desci / 100
final = valor - (descf * valor)
print('O valor R${} com {}% de desconto será R${:.2f}'.format(valor, desci, final))
