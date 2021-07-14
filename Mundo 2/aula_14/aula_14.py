n = 0
r = 'S'

while r == 'S':
    n += int(input('Digite um valor: '))
    r = input('Deseja continuar? [S/N] ').upper()

print('A soma dos valores é {}'.format(n))

# Somando pares e impares em um laço while
num = 1
par = impar = 0

while num != 0:
    num = int(input('Digite um valor: '))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1

print('{} pares e {} ímpares'.format(par, impar))
