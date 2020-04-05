import math
ang = float(input('Digite o ângulo:'))
angr = math.radians(ang)
sen = math.sin(angr)
cos = math.cos(angr)
tan = math.tan(angr)
print('Dado o ângulo {}\nO Seno é {:.2f} \nO Cosseno é {:.2f}\nA Tangente é {:.2f}'.format(ang, sen, cos, tan))
