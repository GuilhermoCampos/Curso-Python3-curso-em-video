expressao = str(input('Digite a sua expressão: '))
abre = fecha = 0
for c in expressao:
    if c == '(':
        abre += 1
    if c == ')':
        fecha += 1
if abre == fecha:
    print('Sua Expressão é Válida!')
elif abre != fecha:
    print('Sua Expressão NÃO é valida!')
