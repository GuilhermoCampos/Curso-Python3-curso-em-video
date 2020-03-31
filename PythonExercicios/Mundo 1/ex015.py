d = int(input('Quantos dias alugados?:'))
km = float(input('Quantos de kilometros percorridos?: '))
t = (km * 0.15) + (d * 60)
print('O total a ser pago é R${:.2f}'.format(t))
