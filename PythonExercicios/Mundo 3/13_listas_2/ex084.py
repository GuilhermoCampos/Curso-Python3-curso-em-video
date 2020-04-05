dados = list()
pessoas = list()
pesados = list()
leves = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
for p, d in enumerate(pessoas):
    if p == 0 or d[1] > maior:
        maior = d[1]
    if p == 0 or d[1] < menor:
        menor = d[1]
for p, d in enumerate(pessoas):
    if d[1] == maior:
        pesados.append(d[0])
    if d[1] == menor:
        leves.append(d[0])
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior}Kg de: {pesados}')
print(f'O menor peso foi {menor}Kg de: {leves}')
