from time import sleep

lista = []
pares = []
ímpares = []
opc = str

while True:
    if opc == 'N':
        break

    num = int(input('Digite um número inteiro: '))
    lista.append(num)

    while True:
        opc = input('Quer continuar? [S/N] ').upper()

        if opc in 'SN':
            break

for count in range(0, 2):
    if count == 0:
        print('Analisando os números...')
    else:
        print('Processando os números pares e ímpares...')
    sleep(1)

for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        ímpares.append(c)

pares.sort()
ímpares.sort()

print(f'Lista completa: {lista}')
print(f'Lista dos pares: {pares}')
print(f'Lista dos ímpares: {ímpares}')
