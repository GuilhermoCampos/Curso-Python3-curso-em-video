# Programa que tem uma função fatorial() que recebe dois Parâmetros: o primeiro que indica o número
# a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado
# ou não na tela o processo de cálculo do fatorial


def fatorial(numero, show=False):
    from time import sleep
    print(f'!{numero} = ', end='')
    sleep(1)
    c = numero
    f = 1
    while c > 0:
        if show:
            sleep(0.5)
            print(c, end='', flush=True)
            sleep(0.5)
            print(' x ' if c > 1 else ' = ', end='', flush=True)
        f *= c
        c -= 1
    return f


# Programa Principal
print('Calculadora fatorial')
num = int(input('Digite o número: !'))
mostrar = str(input('Deseja mostrar a conta?[S/N]: ')).strip().upper()[0]
if mostrar in 'S':
    show = True
else:
    show = False
print(fatorial(num, show))
