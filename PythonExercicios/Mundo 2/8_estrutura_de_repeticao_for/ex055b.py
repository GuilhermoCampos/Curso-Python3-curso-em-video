maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o Peso(kg) da {}º pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O Maior peso registrado foi de {}kg, enquanto o Menor peso Registrado foi de {}kg.'.format(maior, menor))
