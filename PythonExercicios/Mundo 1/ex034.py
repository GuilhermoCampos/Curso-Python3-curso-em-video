sal = float(input('Qual o salário do funcionário?: R$'))
if sal > 1250.00:
    print('O salário terá um aumento de 10% então será R${}'.format(sal + (sal * 0.10)))
else:
    print('O salário terá um aumento de 15% então será R${}'.format(sal + (sal * 0.15)))
