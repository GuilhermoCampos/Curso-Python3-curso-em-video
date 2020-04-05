lista = list()
cinco = False
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
if 5 in lista:
    cinco = True
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números e são estes em ordem decrescente: {lista}')
if cinco is True:
    print('O número 5 está nesta lista')
else:
    print('O número 5 não faz parte dessa lista')
