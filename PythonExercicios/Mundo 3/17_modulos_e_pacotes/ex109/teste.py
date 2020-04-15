# Modifique as funções que foram criadas no desafio 107 para que
# elas aceitem um parâmetro a mais, informando se o valor retornado
# por elas vai ser ou não formatado pela função moeda(), desenvolvido
# no desfio 108.
import moeda

num = float(input('Digite um valor: '))

print(f'O dobro do valor {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'A metade do valor {moeda.moeda(num)} é {moeda.metade(num, True)}')
print(f'O valor {moeda.moeda(num)} aumentado em 10% é {moeda.aumentar(num, 10, True)}')
print(f'O valor {moeda.moeda(num)} diminuido em 10% é {moeda.diminuir(num, 10, True)}')
