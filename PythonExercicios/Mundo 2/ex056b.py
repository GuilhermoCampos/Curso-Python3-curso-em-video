media = 0
mmenos20 = 0
hmvelho = 'Ninguém'
hmvelhoid = 0
for pessoa in range(1, 5):
    print('{}'' {}º PESSOA''{}'.format('-'*5, pessoa, '-'*5))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    media += idade
    if p == 1 and sexo in 'Mm':
        hmvelhoid = idade
        hmvelho = nome
    if sexo in 'Mm' and idade > hmvelhoid:
        hmvelho = nome
        hmvelhoid = idade
    if sexo in 'Ff' and idade < 20:
        mmenos20 += 1
media = media / 4
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(hmvelhoid, hmvelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mmenos20))
