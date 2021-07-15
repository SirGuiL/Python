num = 0
resp = 'S'
counter = 0

while resp != 'N':
    num += int(input('Digite um valor: '))
    resp = input('Deseja continuar? [S/N] ').upper()
    counter += 1

print('A média dos números é: {}'.format(num / counter))
