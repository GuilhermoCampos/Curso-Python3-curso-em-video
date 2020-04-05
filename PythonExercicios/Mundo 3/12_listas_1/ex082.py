lista = []
lista_par = list()
lista_impar = list()
while True:
    valor = int(input('Digite um número: '))
    lista.append(valor)
    if valor % 2 == 0:
        lista_par.append(valor)
    if valor % 2 != 0:
        lista_impar.append(valor)
    cont = str(input('Deseja Continuar?: ')).upper().split()[0]
    if cont == 'N':
        break
lista.sort(), lista_par.sort(), lista_impar.sort()
print(f'Os números digitados foram: {lista}')
print(f'Os números pares foram: {lista_par}')
print(f'Os números impares foram: {lista_impar}')
