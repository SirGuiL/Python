from math import pow, sqrt

catetoAdjacente = float(input('Digite o valor do cateto adjacente: '))
catetoOposto = float(input('Digite o valor do cateto oposto: '))

hipotenusa = sqrt(pow(catetoAdjacente, 2) + pow(catetoOposto, 2))

print('\nMedidas do triângulo retângulo: \nCateto Adjacente: {}\nCateto Oposto: {}\nHipotenusa: {}'.format(catetoAdjacente, catetoOposto, hipotenusa))
