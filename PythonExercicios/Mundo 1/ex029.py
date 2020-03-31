v = float(input('Qual foi a velocidade ?: '))
m = (v - 80) * 7.00
if v > 80:
    print('MULTADO! Você escedeu o limite de velocidade de 80km/h, sua multa é de: R${:.2f}'.format(m))
print('Dirija com cuidado! tenha um bom dia.')
