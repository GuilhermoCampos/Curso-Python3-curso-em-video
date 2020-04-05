# Crie um programa que leia ários números inteiros pelo teclado. No final da execução mostre a média entre todos os
# valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.
parar = ''
soma = cont = maior = menor = 0
while not parar == 'n':
    num = int(input('Digite um número: '))
    parar = str(input('Deseja Continuar?[S/N]: ')).lower().strip()
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
media = soma / cont
print(f'A média entre os {cont} números digitados é {media}, o maior número foi {maior} e o menor foi {menor}.')
