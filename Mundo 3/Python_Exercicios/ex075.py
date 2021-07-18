números = (
    int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: ')),
)
pares = []

num9 = números.count(9)

if num9 == -1: print('Não há nenhum nove')
elif num9 == 1: print('Há um nove')
else: print(f'há {num9} noves')

print(números)
print(f'O número 3 é o {números.index(3) + 1}º número')

for c in range(0, 4):
    if números[c] != 0:
        if números[c] % 2 == 0: 
            pares += [números[c]]

if len(pares) == 1: print(f'{pares} é o único número par.')
else: print(f'{pares} foram os números pares.')
