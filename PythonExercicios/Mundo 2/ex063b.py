t1 = 0
t2 = 1
cnt = 0
print('' ,'-'*22, '\n', 'Sequência de Fibonacci', '\n', '-'*22)
vezes = int(input('Quantos termos deseja exibir?: '))
if vezes == 1:
    print(t1, '→ ', 'Fim')
elif vezes == 2:
    print(t1, '→', end='')
    print(t2, '→ ', end='')
    print('Fim')
elif vezes > 2:
    print(t1, '→', t2, '→ ', end='')
    vezes -= 2
    while cnt <= vezes:
        cnt += 1
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        print(t3, '→', end='')
    print('Fim')
