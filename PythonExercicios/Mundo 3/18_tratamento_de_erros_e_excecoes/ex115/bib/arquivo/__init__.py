def abrir(path):
    try:
        open(path, 'r')
    except:
        print('Arquivo Não existe... Criando arquivo')
        open(path, 'w')
    else:
        print('conseguiu')


def ler(path):
    try:
        with open(path, 'r') as arquivo:
            ler_arquivo = arquivo.readlines()
    except Exception as erro:
        print('Erro ao ler o arquivo')
        print(erro.__class__)
    else:
        print('Arquivo lido com sucesso')
    return ler_arquivo


def escrever(path, texto):
    try:
        with open(path, 'a') as escrevendo:
            print('teste', file=escrevendo)
    except Exception as erro:
        print('Falha ao salvar no arquivo')
        print(erro.__class__)
    else:
        print('Salvo com sucesso')

abrir('nomes.txt')
#print(ler('nomes.txt'))
#escrever('nomes.txt', 'Teste')
arquivo = ler('nomes.txt')
lista = list()
lista.append(arquivo)
print(lista)
input()