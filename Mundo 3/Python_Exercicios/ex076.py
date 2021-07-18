produtos = (
    'caneta',
    200,
    'lápis',
    100,
    'borracha',
    300
)

print('-'*40)
print(f'{"Tabela de preços":^40}')
print('-'*40)

for c in range(0, len(produtos), 2):
    print(f'{produtos[c]:.<30}', end='')
    print(f'R${(produtos[c + 1]/100):>7.2f}')

print('-'*40)
