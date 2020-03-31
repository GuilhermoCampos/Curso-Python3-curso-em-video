from datetime import date
antu = date.today().year
idade = 0
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input('Qual ano de nascimento da {}º pessoa?: '.format(c)))
    idade = antu - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Ao todo Tivemos {} pessoas maiores de idade\nE tivemos {} pessoas menores de idade.'.format(maior, menor))
