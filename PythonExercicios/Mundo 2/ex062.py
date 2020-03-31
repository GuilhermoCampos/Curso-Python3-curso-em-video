termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
contador = 0
acumulador = termo
continuar = 1
while contador != 10:
    print(acumulador, '→ ', end='')
    acumulador += razao
    contador += 1
print('PAUSA')
while continuar != 0:
    continuar = int(input('Quer mostrar mais quantos termos?: '))
    for c in range(0, continuar):
        print(acumulador, '→ ', end='')
        acumulador += razao
        contador += 1
    if continuar != 0:
        print('PAUSA')
print('Progressão finalizada com {} termos mostrados, Obrigado.'.format(contador))
