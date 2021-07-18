from random import randint

números = (
    randint(0, 100),
    randint(0, 100),
    randint(0, 100),
    randint(0, 100),
    randint(0, 100)
)

print(f'Os valores sorteados foram: {números}')

print(f'{sorted(números)[4]} foi o maior valor e {sorted(números)[0]} foi o menor.')
