extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete',
           'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    continua = ' '
    while not 0 <= num <= 20:
        num = int(input('tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {extenso[num]}.')
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continua == 'N':
        break
