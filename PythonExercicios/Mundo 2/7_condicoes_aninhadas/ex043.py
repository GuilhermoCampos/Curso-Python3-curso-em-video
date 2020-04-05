print('Bem vindo a calculadora de IMC!')
altura = float(input('Por Favor insira sua altura: (m) '))
peso = float(input('Por Favor insira seu peso: (Kg) '))
imc = peso / (altura**2)
if imc < 18.5:
    print('Com {:.1f} você está \033[32mAbaixo do Peso\033[m!!!'.format(imc))
elif 18.5 < imc <= 25:
    print('Com {:.1f} você está no \033[34mPeso Ideal\033[m!!!'.format(imc))
elif 25 < imc <= 30:
    print('Com {:.1f} você está com \033[33mSobrepreso\033[m!!!'.format(imc))
elif 30 < imc <= 40:
    print('Com {:.1f} você está com \033[35mObesidade\033[m!!!'.format(imc))
elif imc > 40:
    print('Com {:.1f} você está com \033[31mObesidade mórbida\033[m!!!'.format(imc))
