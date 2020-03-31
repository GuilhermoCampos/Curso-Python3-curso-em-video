frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
tudojunto = ''.join(palavras)
reverso = ''
reverso = tudojunto[::-1]
#for letra in range(len(tudojunto) -1, -1, -1):
#    reverso += tudojunto[letra]
print(tudojunto, reverso)
if reverso == tudojunto:
    print('Essa Frase é um Palindromo')
else:
    print('Essa Frase não é um Palindromo')
