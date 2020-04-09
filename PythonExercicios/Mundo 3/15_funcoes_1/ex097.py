def escreva(texto):
    print('~' * (len(texto) + 4))
    print(f'  {texto}')
    print('~' * (len(texto) + 4))


# Programa Principal
text = str(input('Digite: '))
escreva(text)
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')
