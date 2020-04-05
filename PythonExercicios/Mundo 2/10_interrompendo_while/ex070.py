tot = mais1000 = mbarato = cont = 0
menor = continuar = ' '
while True:
    prod = str(input('Produto: '))
    preco = float(input('Preço: '))
    tot += preco
    cont += 1
    continuar = ' '
    if cont == 1 or mbarato > preco:
        mbarato = preco
        menor = prod
    if preco > 1000:
        mais1000 += 1
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O Total da compra foi de R${tot:.2f}')
print(f'O número de itens acima de R$1000 foi de {mais1000}')
print(f'O item mais barato foi {menor} custando R${mbarato:.2f}')
