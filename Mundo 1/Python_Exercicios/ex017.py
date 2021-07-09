import math

catetoAdjacente = float(input('Digite o valor do cateto adjacente: '))
catetoOposto = float(input('Digite o valor do cateto oposto: '))

hipotenusa = math.hypot(catetoAdjacente, catetoOposto)
print('\nMedidas do triângulo retângulo: \nCateto Adjacente: {}\nCateto Oposto: {}\nHipotenusa: {}'.format(catetoAdjacente, catetoOposto, hipotenusa))
