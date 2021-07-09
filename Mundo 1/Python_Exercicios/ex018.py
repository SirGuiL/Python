import math

angulo = float(input('Digite o ângulo: '))

rad = math.radians(angulo)

print('\nSeno: {}\nCosseno: {}\nTangente: {}'.format(math.sin(rad), math.cos(rad), math.tan(rad)))
