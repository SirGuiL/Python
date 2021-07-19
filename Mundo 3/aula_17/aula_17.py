# Variáveis compostas [lista]
lanche = [
    'hambúrguer', 
    'suco', 
    'pizza', 
    'pudim'
]

lanche[2] = 'picolé' # As listas são mutáveis

lanche.append('cookie') # Adiciona um item no final da lista

print(lanche[0])

lanche.insert(0, 'cachorro quente') # Adiciona um item no indice 1

print(lanche[0])


lanche.remove('picolé') # remove o picolé da lista
del lanche[3] # remove o indice 3
lanche.pop(3) # da mesma forma que o del, remove o indice 3
lanche.pop() # remove o último elemento

print(lanche)

valores = list(range(4, 11)) # Lista com range

print(valores)

valores.sort(reverse=True)

print(valores)
print(f'A lista valores tem {len(valores)} elementos.')

if 3 in valores:
    valores.remove(3)
else:
    print('Não encontrei o número 3.')

números = []

números.append(1)
números.append(4)
números.append(7)

print(números)

for count in range(0, 5):
    números.append(int(input('Digite um valor: ')))

for c, v in enumerate(números):
    print(f'Na posição {c} encontrei o valor {v}!')
