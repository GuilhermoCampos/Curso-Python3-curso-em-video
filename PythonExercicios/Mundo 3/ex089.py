alunos = list()
nome = list()
notas = list()
while True:
    nome.append(str(input('Digite o Nome do aluno: ')).strip())
    notas.append(float(input('Primeira nota: ')))
    notas.append(float(input('Segunda nota: ')))
    nome.append(notas[:])
    alunos.append(nome[:])
    notas.clear()
    nome.clear()
    cont = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break
print('='*40)
print(f'No. NOME           MÉDIA')
for n, a in enumerate(alunos):
    print(f'{n} | {alunos[n][0]:<15} | {(alunos[n][1][0] + alunos[n][1][1]) / 2:.1f}')
check = str(input('Deseja chegar individualmente?[S/N]: ')).strip().upper()[0]
if check != 'N':
    while True:
        n = int(input('Nº do Aluno: '))
        print(f'Notas de {alunos[n][0]} são: {alunos[n][1]}')
        stop = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
        if stop == 'N':
            break
