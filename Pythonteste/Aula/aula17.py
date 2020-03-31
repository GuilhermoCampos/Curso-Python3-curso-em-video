# m.sort(reverse=True)
# num[2] = 3
# num.append(7)
# num.insert(0, 4)
# print(num)
# del num[0]
# num.pop(1)
# num.remove(3)
# print(num)
valores = list()
for dado in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Em {c} achei o valor {v}')
