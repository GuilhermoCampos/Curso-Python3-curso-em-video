# Programa que tem uma função notas() que pode receber várias notas de alunos e vai retornar
# um dicinário com as seguintes informações
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - Média da turma
# - Situação(opcional)


def notas(*n, sit=False):
    """
    → Função para analizar notas e situações de varios alunos
    :param n: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou não adiciona a situação
    :return: dicionário com varias informações sobre a situação da turma.
    """
    di = dict()
    li = list()
    for c in n:
        li.append(c)
    di['quantidade'] = len(li)
    di['maior'] = max(li)
    di['menor'] = min(li)
    di['media'] = (sum(li) / len(li))
    if sit:
        if di['media'] < 4:
            di['situacao'] = 'Ruim'
        elif di['media'] < 6:
            di['situacao'] = 'Razoavel'
        elif di['media'] < 8:
            di['situacao'] = 'Boa'
        elif di['media'] <= 10:
            di['situacao'] = 'Ótima'
    return di


# Programa Principal
resp = notas(5.5, 9.5, 9.5, sit=True)
print(resp)
