val = float(input('Digite o valor em metros: '))
#cm = val * float(10**2)
#mm = val * float(10**3)
#print('O valor em metros é {}, em centímetros é {} e em milímetros é {}.'.format(val, cm, mm))
print('{} kilometros \n{}hectometros \n{} decametros \n{} metros \n{} decimetros \n{} centimetros \n{} milimetros \n{} micrometros \n{} nanometros  '.format(val*10**-3, val*10**-2, val*10**-1, val*10**0, val*10**1, val*10**2, val*10**3, val*10**4, val*10**5))
