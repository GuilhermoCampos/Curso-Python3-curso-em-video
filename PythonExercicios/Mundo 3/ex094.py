# Um programa que lê nome e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. no final, mostra:
# A) Quantas pessoas cadastradas
# B) A média de idade
# C) Uma lista com mulheres
# D) Uma lista com idade acima da média.
pessoas = list()
pessoa = dict()
idades = list()
mulheres = list()
maismed = list()
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo not in 'MF':
        while sexo not in 'MF':
            print('ERRO! Por favor apenas M ou F: ')
            sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'F':
        mulheres.append(nome)
    idade = int(input('Idade: '))
    idades.append(idade)
    media = sum(idades) // len(idades)
    pessoa['nome'] = nome; pessoa['sexo'] = sexo; pessoa['idade'] = idade
    pessoas.append(pessoa.copy())
    continuar = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
    if continuar not in 'SN':
        while continuar not in 'SN':
            print('ERRO! Digite apenas S ou N: ')
            continuar = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
for k, v in enumerate(pessoas):
    if v['idade'] > media:
        maismed.append(v.copy())
print(f'A) Foram cadastradas {len(pessoas)} pessoas.')
print(f'B) A média de idade é de {media}.')
print(f'C) As mulheres cadastradas foram: ', end='')
for c in mulheres:
    print(c, end='; ')
print()
print('D) Lista das pessoas que estão acima da média de idade:')
for c in maismed:
    for k, v in c.items():
        print('  →', k, '=', v, end='; ')
    print()
