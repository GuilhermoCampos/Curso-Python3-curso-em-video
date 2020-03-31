mais18 = homem = mul20 = 0
while True:
    print('-'*20, 'Ficha de Dados', '-'*20)
    idade = int(input('Idade: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        mais18 += 1
    if sex == 'M':
        homem += 1
    if sex == 'F' and idade < 20:
        mul20 += 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar?: ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'''No total foram inseridos dados de {mais18} pessoas com mais de 18 anos, 
{homem} Homens, e {mul20} Mulheres com menos de 20 anos.
Acabou!''')
