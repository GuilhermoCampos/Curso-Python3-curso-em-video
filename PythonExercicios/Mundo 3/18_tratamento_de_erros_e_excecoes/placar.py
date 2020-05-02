# Manipulação do Arquivo


def abrir(path):
    try:
        a = open(path, 'tr')
    except:
        print('Criando Arquivo...')
        a = open(path, 'w+')
    finally:
        a.close()


def ler(path):
    try:
        f = open(path, 'tr')
        arquivo = f.readlines()
        f.close()
        abriu = True
    except:
        abriu = False
    if abriu:    
        return arquivo
    else:
        print('Não foi possivel ler o arquivo')


def gravar(path, wra, gravacao):
    try:
        f = open(path, wra)
        abriu = True
    except Exception as erro:
        print(f'Não foi possivel devido erro: "{erro.__class__}"')
    if abriu:
        f.write(gravacao)
        f.close


def adicionar(arquivo):
    nome = str(input('Nome:'))
    pont = 0
    gravar(arquivo, 'a', f'{nome};{pont}\n')


def modificar(arquivo):
    pass

# Manipulação Da Interface


def linhas(simb, tam):
    lin = simb * tam
    print(f'{lin}')


def cabecalho(titulo):
    linhas('=', 60)
    print(f'|{titulo:^58}|')
    linhas('=', 60)


def menu(lista):
    cabecalho('Menu Principal')
    for p, i in enumerate(lista):
        print(f'| {p+1} - {i:<53}|')
    linhas('=', 60)
    opc = leiaInt('Escolha uma Opção: ')
    return opc


def placar(arquivo):
    lista = list()
    pessoa = list()
    for linha in arquivo:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        lista.append(dado[:])
    return lista


def mostrar(arquivo):
    cabecalho('Placar')
    print(f'| {"Nome":^27}||{"Pontuação":^27} |')
    linhas("=", 60)
    for c in arquivo:
        print(f'| {c[0]:<28}{c[1]:>24} pts |')
    linhas('=', 60)
    pass


# Funções extras


def leiaInt(txt):
    while True:
        try:
            num = int(input(txt))
        except:
            print('Por favor insira um número inteiro válido')
            continue
        else:
            return num
        

def clear():
    import os
    os.system('cls')


# Programa Principal
opc = menu(['Ler Placar', 'Adicionar Pontuação', 'Adicionar Pessoa' , 'Sair'])
#print(opc)
abrir('test.txt')
#gravar('test.txt', 'a', 'Guilherme;13\n') 
#adicionar('test.txt')
arquivo = ler('test.txt')
clear()
mostrar(placar(arquivo))
input()

# Função adicionar pessoa
# Função somar ao placar
#
#
