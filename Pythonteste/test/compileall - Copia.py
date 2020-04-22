import compileall
try:
    copilar = str(input('Arquivo a copilar: '))
    local = compileall.compile_dir(copilar)
except Exception as erro:
    print('não compilado', erro.__class__)
else:
    print('Compilado', local)
    input()
input()