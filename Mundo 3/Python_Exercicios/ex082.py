lista = []
pares = []
ímpares = []
opc = str

while True:
    if opc == 'N':
        break

    num = int(input('Digite um número inteiro: '))
    lista.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        ímpares.append(num)

    while True:
        opc = input('Quer continuar? [S/N] ').upper()

        if opc in 'SN':
            break

pares.sort()
ímpares.sort()

print(f'Lista completa: {lista}')
print(f'Lista dos pares: {pares}')
print(f'Lista dos ímpares: {ímpares}')
