# Crie um pequeno sistema modularizado que permita cadastrar 
# pessoas pelo seu nome e idade em um arquivo de texto simples.
#
# O sistema vai ter 2 opções: cadastrar uma nova pessoa e 
# listar todos as pessoas cadastradas.
#
# Crie um pequeno sistema modularizado que permita cadastrar
# pessoas pelo seu nome e idade em um arquivo de texto simples.

from time import sleep
from bib import *

# Função iniciando o arquivo para verificar se ele existe, caso não exista cria um arquivo txt.

abrir('nomes.txt')

# Loop infinito que permite a repetição do menu até o usuário descidir sair

while True:

    # Iniciando função que irá mostrar as opções do menú e irá receber a resposta de qual função iniciar

    opcao = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])

    # A 1º opção do programa irá ler os dados de um arquivo e mostrar eles na tela

    if opcao == 1:
        try:
            arquivo = ler('nomes.txt')
            listar(interpretar(arquivo))
        except:
            print('Não foi Possivel ler a lista')
        else:
            continue

    # A 2º opção do programa irá cadastrar mais uma pessoa na lista

    elif opcao == 2:
        cadastrar('nomes.txt')
        continue

    # A 3º opção do programa irá fechar o programa

    elif opcao == 3:
        linha(60)
        print(f'{"Saindo do sistema... Até logo":^60}')
        linha(60)
        sleep(2)
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
        sleep(2)
        continue
