termo = int(input('Digite o Primeiro Termo da PA: '))
razao = int(input('Digite a Razão: '))
acumulador = termo
contador = 0
while contador != 10:
    print(acumulador, '→ ' if contador != 9 else '', end='')
    acumulador += razao
    contador += 1
