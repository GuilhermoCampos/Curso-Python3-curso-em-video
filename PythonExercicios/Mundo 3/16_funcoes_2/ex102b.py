def fatorial(n, show=False):
    """
    Calcula o Fatorial de um número.
    :param n: Número a ser calculado.
    :param show: (opcional) Mostrar a conta.
    :return: Valor fatorial de um número n.
    """
    from time import sleep
    f = 1
    print(f'!{n} = ', end='', flush=True)
    sleep(1)
    for c in range(n, 0, -1):
        f *= c
        if show:
            sleep(0.5)
            print(c, end='', flush=True)
            sleep(0.5)
            print(' X ' if c > 1 else ' = ', end='', flush=True)
    sleep(1)
    return f


print(fatorial(5, True))
