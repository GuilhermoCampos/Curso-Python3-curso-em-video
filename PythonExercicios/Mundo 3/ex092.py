# Programa que lê nome, ano de nascimento e carteira de trabalho e cadastra(com idade) em um dicionário
# se por acaso a CTPS for iferente de Zero, o dicionário receberá também o ano de contratação e salário.
# Calcular e acrescentar alem da idade, com quantos anos a pessoa vai se aposentar.
import time
ano = time.localtime().tm_year
pessoa = dict()
pessoa['nome'] = str(input('Digite o nome: ')).strip()
pessoa['idade'] = time.localtime().tm_year - int(input('Ano de Nascimento: '))
pessoa['ctps'] = int(input('Número CTPS [0 caso não tenha]: '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = int(input('Salário: '))
    tempoDeServico = time.localtime().tm_year - pessoa['contratação']
    tempoRestante = 35 - tempoDeServico
    pessoa['aposentadoria'] = pessoa['idade'] + tempoRestante
print('-='*62)
for k, v in pessoa.items():
    print(f'- {k} tem o valor {v}')
