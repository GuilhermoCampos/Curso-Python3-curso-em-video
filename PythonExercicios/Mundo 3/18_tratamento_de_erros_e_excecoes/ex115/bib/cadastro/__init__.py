def cadastrar(lista):
    pessoa = dict()
    while True:
        try:
            nome = str(input('Nome: '))
        except:
            print('\033[31mNão foi possivel adicionar o nome, tente novamente!\033[m')
            continue
        else:
            print('\033[32mNome adicionado com sucesso!\033[m')
            break
    while True:
        try:
            idade = int(input('Idade: '))
        except:
            print('\033[31mNão foi possivel adicionar a idade, tente novamente!\033[m')
            continue
        else:
            print('\033[32mIdade adicionada com sucesso!\033[m')
            break
    pessoa['nome'] = nome
    pessoa['idade'] = idade
    lista.append(pessoa.copy())
    pessoa.clear()
    return lista

