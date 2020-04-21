# Crie um pequeno sistema modularizado que permita cadastrar 
# pessoas pelo seu nome e idade em um arquivo de texto simples.
#
# O sistema vai ter 2 opções: cadastrar uma nova pessoa e 
# listar todos as pessoas cadastradas.
#
# Crie um pequeno sistema modularizado que permita cadastrar
# pessoas pelo seu nome e idade em um arquivo de texto simples.
from bib.interface import *
from bib.cadastro import *
from bib.listagem import *
from time import sleep
lista = list()
while True:
    opcao = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if opcao == 1:
        listar(lista)
        continue
    elif opcao == 2:
        cadastrar(lista)
        continue
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
