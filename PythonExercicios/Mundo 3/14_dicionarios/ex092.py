# Programa que lê nome, ano de nascimento e carteira de trabalho e cadastra(com idade) em um dicionário
# se por acaso a CTPS for iferente de Zero, o dicionário receberá também o ano de contratação e salário.
# Calcular e acrescentar alem da idade, com quantos anos a pessoa vai se aposentar.
import time
sexo = temctps = ' '
ano = time.localtime().tm_year
pessoa = dict()
pessoa['nome'] = str(input('Digite o nome: ')).strip()
while sexo not in 'MF':
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
pessoa['sexo'] = sexo
pessoa['idade'] = time.localtime().tm_year - int(input('Ano de Nascimento: '))
while temctps not in 'SN':
    temctps = str(input('Tem CTPS?[S/N]: ')).strip().upper()[0]
if temctps == 'S':
    pessoa['ctps'] = int(input('Número CTPS: '))
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = int(input('Salário: '))
    pessoa['anos de contribuição'] = time.localtime().tm_year - pessoa['contratação']
    if pessoa['sexo'] == 'M':
        tempoRestante = 35 - pessoa['anos de contribuição']
        if pessoa['idade'] >= 61:
            pessoa['ano de aposentadoria'] = time.localtime().tm_year + tempoRestante
            pessoa['idade de aposentadoria'] = pessoa['idade'] + tempoRestante
        else:
            idadeRestante = 61 - pessoa['idade']
            tempoAposentadoria = (idadeRestante - tempoRestante) + tempoRestante
            pessoa['ano de aposentadoria'] = time.localtime().tm_year + tempoAposentadoria
            pessoa['idade de aposentadoria'] = pessoa['idade'] + tempoAposentadoria
    if pessoa['sexo'] == 'F':
        tempoRestante = 30 - pessoa['anos de contribuição']
        if pessoa['idade'] >= 56:
            pessoa['ano de aposentadoria'] = time.localtime().tm_year + tempoRestante
            pessoa['idade de aposentaoria'] = pessoa['idade'] + tempoRestante
        else:
            idadeRestante = 56 - pessoa['idade']
            tempoAposentadoria = (idadeRestante - tempoRestante) + tempoRestante
            pessoa['ano de aposentadoria'] = time.localtime().tm_year + tempoAposentadoria
            pessoa['idade de aposentaoria'] = pessoa['idade'] + tempoAposentadoria
print('-='*62)
for k, v in pessoa.items():
    print(f'- {k}: {v}')
