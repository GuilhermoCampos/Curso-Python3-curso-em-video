n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda Nota: '))
m = (n1 + n2)/2
if m < 5.0:
    print(f'Infelizmente você está \033[31mREPROVADO\033[m pois a média de {m} não é o suficiente para recuperação.')
elif 5 < m < 6.9:
    print('Você está de \033[33mRECUPERAÇÃO\033[m pois a média {} não é o suficiente para ser aprovado'.format(m))
elif m >= 7:
    print('PARABAINS você está \033[34mAPROVADO\033[m!!! {} é uma boa nota!!!'.format(m))
