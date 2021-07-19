lista = []
números = cinco = 0
opc = str

while True:
    if opc == 'N':
        break

    num = int(input('Digite um número inteiro: '))

    if num == 5:
        cinco += 1

    if num not in lista:
        números += 1

    lista.append(num)

    while True:
        opc = input('Deseja continuar? [S/N] ').upper()

        if opc in 'SN':
            break

if len(lista) == 1:
    print('Foi digitado apenas um valor.')
else:
    print(f'Foram digitados {len(lista)} valores')

if números == 1: 
    print('Não houve números diferentes pois apenas um número foi digitado.')
else: 
    print(f'Foram digitados {números} valores diferentes')

lista.sort(reverse=True)

print(f'A lista ordenada de forma decrescente fica da seguinte forma: {lista}')

if 5 not in lista: 
    print('O valor 5 não foi digitado.')
else:
    if cinco == 1: 
        print('O valor 5 foi digitado apenas uma vez')
    else:
        print(f'O valor 5 foi digitado {cinco}x')
