from time import sleep
cont = maior = menor = total = soma = 0
while True:
    num = int(input('Digite um valor [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    elif maior < num:
        maior = num
    elif menor > num:
        menor = num
    total += num
print(f'Você digitou {cont} números e a soma total desses números é {total}.')
print(f'O maior número foi {maior} e o menor foi {menor}.')
sleep(3)
print('Fim.')
