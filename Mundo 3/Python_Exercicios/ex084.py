pessoas = []
pessoa = []
maispesado = []
maisleve = []
numpesado = numleve = 0
opc = str
x = 1

while True:
    if opc == 'N':
        break

    pessoa.append(input('Digite seu nome: '))
    pessoa.append(float(input('Digite seu peso: ')))

    pessoas.append(pessoa[:])
    pessoa.clear()

    while True:
        opc = input('Deseja continuar? [S/N] ').upper()

        if opc in 'SN':
            break

pessoas.sort()

if len(pessoas) > 1:
    print(f'{len(pessoas)} pessoas foram cadastradas.')
else:
    print('Você cadastrou apenas uma pessoa.')

for p in pessoas:
    if p[1] >= numpesado:
        if len(maispesado) > 0:
            if maispesado[0][1] < p[1]:
                maispesado.clear()
                maispesado.append(p[:])
                numpesado = p[1]
            elif maispesado[0][1] == p[1]:
                maispesado.append(p[:])
        else:
            maispesado.append(p[:])

    if p[1] <= numleve or numleve == 0:
        if len(maisleve) > 0:
            if maisleve[0][1] > p[1]:
                maisleve.clear()
                maisleve.append(p[:])
                numleve = p[1]
            elif maisleve[0][1] == p[1]:
                maisleve.append(p[:])
        else:
            maisleve.append(p[:])


if len(maispesado) > 1:
    print('As pessoas mais pesadas são', end=' ')

    if len(maispesado) == 2:
        for p in maispesado:
            if x == 1:
                print(p[0], end=' e ')
            else:
                print(p[0], end=' ')
            x += 1
    else:
        for p in maispesado:
            if x + 1 == len(maispesado):
                print(p[0], end=' e ')
            elif x == len(maispesado):
                print(p[0], end=' ')
            else:
                print(p[0], end=', ')
            x += 1
    print(f'com {maispesado[0][1]}Kg')
else:
    print(f'{maispesado[0][0]} é a pessoa mais pesada com {maispesado[0][1]}Kg')

if len(maisleve) > 1:
    print(f'As pessoas mais leves são', end=' ')
    x = 1
    if len(maisleve) == 2:
        for p in maisleve:
            if x == 1:
                print(p[0], end=' e ')
            else:
                print(p[0], end=' ')
            x += 1
    else:
        for p in maisleve:
            if x + 1 == len(maisleve):
                print(p[0], end=' e ')
            elif x == len(maisleve):
                print(p[0], end=' ')
            else:
                print(p[0], end=', ')
            x += 1
    print(f'com {maisleve[0][1]}Kg')
else:
    print(f'{maisleve[0][0]} é a pessoa mais leve com {maisleve[0][1]}Kg')

print('-='*20)
print(f'{"Tabela de pessoas:":^40}')
print('-='*20)

for p in pessoas:
    print(f'{p[0]:<15}', end='')
    print(f'{"|":^10}', end='')
    print(f'{p[1]:>13}Kg')
