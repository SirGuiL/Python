prodmaisbarato = ''
nome = opc = str
soma = mais1000 = preço = maisbarato = 0

while True:
    if opc == 'N':
        break

    nome = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto: '))

    if maisbarato == 0:
        maisbarato = preço
        prodmaisbarato = nome

    if preço < maisbarato: 
        maisbarato = preço
        prodmaisbarato = nome
    
    if preço > 1000: mais1000 += 1
    
    soma += preço

    while True:
        opc = input('Deseja continuar? [S/N]: ').upper()
        if opc == 'S':
            break
        elif opc == 'N':
            break

print(f'Total gasto: R${soma:.2f}\n{mais1000} custaram mais de R$1000,00\n{prodmaisbarato} foi o produto mais barato.')
