lista = []
maior = menor = 0

for c in range(0, 5):
    lista.append(int(input('Digite um número inteiro: ')))

    if c == 0:
        maior = menor = lista[c]
    
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

print(f'O maior valor digitado foi o {maior} e o menor foi o {menor}')
print(f'O maior estava localizado na {lista.index(maior) + 1}ª posição e o menor na {lista.index(menor) + 1}ª posição')
