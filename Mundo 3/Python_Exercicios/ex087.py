matriz = [
    [[], [], []], 
    [[], [], []], 
    [[], [], []]
]
pares = 0
terceira = 0
maior = 0

for r in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Digite o valor da coluna {c + 1} da linha {r + 1}: '))
        if num % 2 == 0:
            pares += num
        
        if c == 2:
            terceira += num

        if r == 1:
            if maior == 0:
                maior = num
            else:
                if num > maior:
                    maior = num

        matriz[r][c].append(num)

for r in range(0, 3):
    for c in range(0, 3):
        print(matriz[r][c], end=' ')
    print('')

print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {terceira}.')
print(f'O maior valor da 2ª linha é {maior}.')
