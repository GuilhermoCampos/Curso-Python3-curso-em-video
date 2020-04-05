frase = str(input('Digite uma frase: ')).lower().strip()
print('A Letra "A" Aparece {} vezes'.format(frase.count('a')))
print('A letra "A" aparece pela primeira vez na posição: {}'.format(frase.find('a') + 1))
print('A Letra "A" aparece pela última vez nas posição: {}'.format(frase.rfind('a') + 1))
