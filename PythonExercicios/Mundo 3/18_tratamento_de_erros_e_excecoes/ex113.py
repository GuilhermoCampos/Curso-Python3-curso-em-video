# Rescreva a função leiaInt() que fizemos no desafio 104, incluindo
# agora a possibiliade da digitação de um número de tipo inválido.
# Aproveite e rie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            num = int(input(f'{msg}'))
        except (ValueError, TypeError): 
#        except Exception as error:
#           print(f'Tivemos um problema com {error.__class__}')
            print('\033[31mERRO: Por favor, Digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar este número\033[m')
            return 0
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(f'{msg}'))
        except (TypeError, ValueError):
#        except Exception as error:
#           print(f'Tivemos um problema com {error.__class__}')
            print('\033[31mERRO: Por favor, Digite um número real válido!\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar este número\033[m')
            return 0
        else:
            break
    return num


inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
