lar = float(input('Qual A Largura da parede em metros?: '))
alt = float(input('Qual A Altura da Parede em metros?: '))
area = lar * alt
tin = area / float(2)
print('Para pintar uma parede de dimensão {}m x {}m, onde terá {}m² de área. \nserão necessarios {}L de tinta.'.format(lar, alt, area, tin))
