print('', '\033[30;44m-=-\033[m'*20, '\n \033[30;44m              Analizador de Triangulos 2.0                  \033[m')
print('', '\033[30;44m-=-\033[m'*20)
n1 = float(input('Primeiro Seguimento: '))
n2 = float(input('Segundo Seguimento: '))
n3 = float(input('Terceiro Seguimento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print('Os Seguimentos acima \033[34mPODEM\033[m formar um triangulo!')
    if n1 == n2 == n3:
        print('E o Triangulo é \033[32mEquilátero\033[m!!!')
    elif n1 == n2 or n2 == n3 or n1 == n3:
        print('E o Triangulo é \033[36mIsósceles\033[m!!!')
    elif n1 != n2 and n2 != n3 and n1 !=n3:
        print('E o Triangulo é \033[35mEscaleno\033[m!!!')
else:
    print('Os Seguimentos acima \033[31mNÃO PODEM\033[m formar um triangulo!')
