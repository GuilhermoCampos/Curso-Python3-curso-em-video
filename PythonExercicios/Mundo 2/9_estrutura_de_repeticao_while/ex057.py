checador = 'e'
sexo = str(input('Informeseu sexo [M/F]: ')).upper()
if sexo != 'F' and sexo != 'M':
    while checador == 'e':
        sexo = str(input('Dados inválidos. Por favor informe seu sexo: ')).upper()
        if sexo == 'F' or sexo == 'M':
            checador = 'c'
print('Sexo {} registrado com sucesso'.format(sexo))
