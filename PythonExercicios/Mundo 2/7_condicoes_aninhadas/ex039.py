from datetime import date
from time import sleep
atual = date.today().year
nascimento = int(input('Digite o ano de seu nascimento: '))
idade = atual - nascimento
print('Analizando...')
sleep(2)
print('Você tem {} anos'.format(idade))
if idade < 18:
    print(f'Ainda falta \033[34m{18-idade}\033[m anos, seu alistamento será em {(18-idade)+atual}.')
elif idade == 18:
    print('\033[32mJá é hora de se alistar!!!')
elif idade > 18:
    print('Caso ainda não tenha se alistado você está \033[31m{}\033[m anos atrasado'.format(idade - 18))
