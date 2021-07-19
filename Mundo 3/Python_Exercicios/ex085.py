lista = [[], []]
num = int
x = 1

for n in range(0, 7):
    num = int(input('Digite um valor numérico: '))

    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

lista[0].sort()
lista[1].sort()

print(f'Os números pares são', end=' ')
for p in lista[0]:
    if x + 1 == len(lista[0]):
        print(p, end=' e ')
    elif x == len(lista[0]):
        print(p, end='.')
    else:
        print(p, end=', ')
    x += 1

x = 1

print(f'\nOs números ímpares são', end=' ')
for i in lista[1]:
    if x + 1 == len(lista[1]):
        print(i, end=' e ')
    elif x == len(lista[1]):
        print(i, end='.')
    else:
        print(i, end=', ')
    x += 1
