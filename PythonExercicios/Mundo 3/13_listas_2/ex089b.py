alunos = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('1º Nota: '))
    nota2 = float(input('2º Nota: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], [media]])
    cont = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break
print('='*40)
print(f'No. NOME           MÉDIA')
for n, a in enumerate(alunos):
    print(f'{n} | {a[0]:<15} | {a[2]}')
check = str(input('Deseja chegar individualmente?[S/N]: ')).strip().upper()[0]
if check != 'N':
    while True:
        n = int(input('Nº do Aluno: '))
        if n <= len(alunos) - 1:
            print(f'Notas de {alunos[n][0]} são: {alunos[n][1]}')
        stop = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
        if stop == 'N':
            break
