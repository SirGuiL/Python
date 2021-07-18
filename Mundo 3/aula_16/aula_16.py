# Variáveis compostas (tuplas)
lanche = ('hambúrguer', 'suco', 'pizza', 'pudim')

for cont in range(0, len(lanche)):
    print(f'Vou comer {lanche[cont]} na posição {cont}')

for comida in lanche:
    print(f'Vou comer {comida}')

for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}')

print(sorted(lanche))
print(lanche)
# As tuplas são imutáveis

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b

print(c)
print(len(c))
print(c.count(5)) # Quantas vezes aparecem o número 5
print(c.index(4)) # A posição do número 4

del(c) # Apagando a tupla C (serve para qualquer coisa em Python)
