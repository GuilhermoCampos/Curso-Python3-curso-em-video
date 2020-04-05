import math
ang = float(input('Valor do ângulo: '))
rad = (ang * 3.1415)/180
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print('Dado ângulo {}\nSeno igual a {:.2f}\nCosseno igual a {:.2f}\nTangente igual a {:.2f}'.format(ang, sen, cos, tan))
