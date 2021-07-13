pesos = []

for c in range(0, 5):
    pesos += [float(input('Digite o peso da {}ª pessoa: '.format(c + 1)))]

pesos.sort()

print('{:.2f}Kg é o mais pesado'.format(pesos[4]))
print('{:.2f}Kg é o mais leve'.format(pesos[0]))
