from datetime import date
ano = int(input('Que ano quer analizar? caso queira o ano atual coloque 0: '))
if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O ano de {} é um ano \033[35mBissexto! '.format(ano))
else:
    print('O ano de {} não é um ano \033[31mBisexto! '.format(ano))
