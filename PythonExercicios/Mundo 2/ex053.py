frase = str(input('Digite uma frase: ')).strip().upper()
frases = frase.split()
tudojunto = ''.join(frases)
reverso = ''
for letras in range(len(tudojunto)-1, -1, -1):
    reverso += tudojunto[letras]
print(tudojunto, reverso)
if tudojunto == reverso:
    print('A Frase {} É um Políndromo'.format(frase))
else:
    print('A Frase {} NÃO É um Polínromo'.format(frase))
