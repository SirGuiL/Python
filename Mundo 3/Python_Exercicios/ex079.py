lista = []
opc = str

while True:
    if opc == 'N':
        break

    num = int(input('Digite um número inteiro: '))

    if num not in lista:
        lista.append(num)
    else:
        print('O número já foi adicionado.')
    
    while True:
        opc = input('Deseja continuar? [S/N] ').upper()

        if opc in 'SN':
            break

lista.sort()

for c in lista:
    print(c, end=' ')

a = input('a')
    