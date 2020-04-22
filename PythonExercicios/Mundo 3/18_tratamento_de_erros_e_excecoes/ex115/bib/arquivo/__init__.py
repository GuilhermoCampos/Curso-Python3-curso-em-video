def abrir(path):
    """
    Função que verifica se o arquivo existe,
    caso o arquivo não exista, cria o arquivo.
    :param path: Caminho para o arquivo
    """
    try:
        arquivo = open(path, 'r')
    except:
        print('Arquivo Não existe... Criando arquivo')
        arquivo = open(path, 'w')
    else:
        pass
    arquivo.close()


def ler(path):
    """
    Função que abre um arquivo e copia o que estiver dentro para uma lista.
    :param path: Caminho para o arquivo
    :return: Lista com o conteudo do arquivo
    """
    try:
        with open(path, 'r') as arquivo:
            ler_arquivo = arquivo.readlines()
    except Exception as erro:
        print('Erro ao ler o arquivo')
        print(erro.__class__)
    else:
        pass
    arquivo.close()
    return ler_arquivo


def salvar(path, texto):
    """
    Função que escreve e salva um texto em um arquivo.
    :param path: Caminho para o arquivo
    :param texto: texto a ser salvo no arquivo
    """
    try:
        with open(path, 'a') as escrevendo:
            print(texto, file=escrevendo)
    except Exception as erro:
        print('Falha ao salvar no arquivo')
        print(erro.__class__)
    else:    
        pass
    escrevendo.close()    

