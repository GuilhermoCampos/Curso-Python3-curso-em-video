import py_compile
try:
    copilar = str(input('Arquivo a copilar: '))
    local = py_compile.compile(copilar)
except Exception as erro:
    print('não compilado', erro.__class__)
else:
    print('Compilado', local)
    input()
input()