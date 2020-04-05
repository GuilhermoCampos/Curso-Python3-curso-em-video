f1 = 0
f2 = 1
termos = 2
fn = 0
print('', '-'*30, '\n    Sequência de Fibonacci\n', '-'*30)
qnt = int(input('Quantos termos você quer mostrar?: '))
print('0 → 1 → ', end='')
while termos != qnt:
    fn = f1 + f2
    f1 = f2
    f2 = fn
    print(fn, '→ ', end='')
    termos += 1
print('fim')