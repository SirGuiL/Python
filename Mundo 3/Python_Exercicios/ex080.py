lista = []
maior = 0
menor = 0

for c in range(0, 5):
    num = int(input('Digite um número inteiro: '))

    if c == 0 or num > lista[-1]:
        print('Adicionado ao final da lista')
        lista.append(num)

    else:
        posição = 0
        while posição < len(lista):
            if num <= lista[posição]:
                lista.insert(posição, num)
                print(f'Adicionado a posição {posição}')
                break
            posição += 1

print(f'Valores digitados ordenados de forma crescente: {lista}')
