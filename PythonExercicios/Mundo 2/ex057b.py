sexo = str(int('Informe seu Sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por Favor, Informe seu sexo: ')).stip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
