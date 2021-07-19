matriz = [
    [[], [], []], 
    [[], [], []], 
    [[], [], []]
]

for r in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Digite o valor da coluna {c + 1} da linha {r + 1}: '))
        matriz[r][c].append(num)

for r in range(0, 3):
    for c in range(0, 3):
        print(matriz[r][c], end=' ')
    print('')
