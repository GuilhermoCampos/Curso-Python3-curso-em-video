# Crie um código em Python que teste se o site Pudim está acessivel pelo computador usado.

import urllib.request

try:
    abrir = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Não foi possivel acessar esse site')
else:
    print('O site está funcionando corretamente')
input()