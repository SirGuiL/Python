# Parte 1
# import e import from
import math
# from math import floor (Exemplo de exportação de uma única função)
import random

num = int(input('Digite um número: '))

print('Arredondado para cima: {}'.format(math.ceil(num))) # Arredonda para cima
print('Arredondado para baixo: {}'.format(math.floor(num))) # Arredonda para baixo 
print('Eliminando os números após a virgula: {}'.format(math.trunc(num))) # Elimina os números da virgula para frente
print('Elevado a 2: {}'.format(math.pow(num, 2))) # Potencia
print('Raiz quadrada: {}'.format(math.sqrt(num))) # Raiz quadrada
print('Fatorial: {}'.format(math.factorial(num))) # Fatorial

# Parte 2
print('Número float aleatório: {}'.format(random.random()))
print('Número int aleatório: {}'.format(random.randint(1, 100)))

num = int(input('Digite um número: '))