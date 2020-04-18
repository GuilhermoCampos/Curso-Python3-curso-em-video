# Dentro do pacote utilidadesCeV que criamos no desafio 11. temos
# um módulo chamado dado. Crie uma função chamada leiaDinheiro()
# que seja capaz de funcionar como a função input(), mas com uma
# validação de dados para aceitar apenas valores que sejam monetários.

from utilidadescev import moeda
from utilidadescev import dado

# Programa Principal
num = dado.leiadinheiro('Digite um valor: ')
moeda.resumo(num, 80, 35)
input('Enter para sair')
