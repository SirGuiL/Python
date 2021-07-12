lados = []
count = 1

while count <= 3:
    lados += [float(input('Digite o valor da reta: '))]
    count += 1

lados.sort()

if lados[2] <= lados[1] + lados[0]:
    if(lados[2] == lados[1] and lados[1] == lados[0]):
        print('É um triângulo equilátero.\nTodos os lados são iguais.')
    elif((lados[2] == lados[1] and lados[1] != lados[0]) or (lados[1] == lados[0] and lados[0] != lados[2]) or (lados[0] == lados[2] and lados[2] != lados[1])):
        print('É um triângulo isósceles.\nDois lados são iguais.')
    else:
        print('É um triângulo escaleno.\nTodos os lados são diferentes.')

else:
    print('É impossível formar um triângulo com essas retas')

a = input('a')