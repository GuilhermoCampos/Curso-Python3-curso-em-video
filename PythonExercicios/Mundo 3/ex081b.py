lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números e são estes em ordem decrescente: {lista}')
if 5 in lista:
    print('O número 5 está nesta lista')
else:
    print('O número 5 não faz parte dessa lista')
