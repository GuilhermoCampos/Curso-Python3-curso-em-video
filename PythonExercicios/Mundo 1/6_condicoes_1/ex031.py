km = float(input('Qual a distância da viagem em km?: '))
if km <= 200:
    v1 = km * 0.50
    print('O valor da passagem é de R${:.2f}'.format(v1))
else:
    v2 = km * 0.45
    print('O valor da passagem é de R${:.2f}'.format(v2))
#preço = km * 0.50 if km <=200 else km * 0.45