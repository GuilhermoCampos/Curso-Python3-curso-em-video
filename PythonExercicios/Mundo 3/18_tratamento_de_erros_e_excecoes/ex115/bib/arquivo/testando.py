from time import sleep
try:
    f = open('nomes.txt', 'r')
except:
    print('Falhou')
    f = open('nomes.txt', 'w+')
else:
    print('Conseguiu')
try:
    for c in range(10):
        f.write(f'Testando {c}\n')
except:
    print('não escreveu')
else:
    print('escreveu')
while True:
    try:
        read_file = f.read()
        print(read_file)
    except:
        print('não leu')
    else:
        print('leu')
        break
    sleep(2)