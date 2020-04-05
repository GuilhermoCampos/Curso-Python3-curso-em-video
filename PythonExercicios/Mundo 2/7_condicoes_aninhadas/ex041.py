from datetime import date
atual = date.today().year
nascimento = int(input('Data de nascimento: '))
idade = atual - nascimento
print(f'O Atleta tem {idade}')
if idade <=9:
    print('Categoria \033[33mMirim\033[m')
elif idade <= 14:
    print('Categoria \033[32mInfantil\033[m')
elif idade <= 19:
    print('Categoria \033[34mJunior\033[m')
elif idade <= 25:
    print('Categoria \033[31mSênior\033[m')
else:
    print('Categoria \033[35mMASTER\033[m')
