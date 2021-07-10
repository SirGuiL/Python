lados = []
count = 1

while count <= 3:
    lados += [float(input('Digite o valor da reta: '))]
    count += 1

lados.sort()

if lados[2] <= lados[1] + lados[0]:
    print('É possível formar um triângulo com essas 3 retas.')

else:
    print('É impossível formar um triângulo com essas retas')
