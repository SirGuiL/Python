nomes = []
idades = []
sexo = []
soma = 0
maisvelho = 0
menos20 = 0

for c in range(0, 4):
    nomes += [input('Digite o nome da {}ª pessoa: '.format(c + 1))]
    idades += [int(input('Digite a idade da {}ª pessoa: '.format(c + 1)))]
    sexo += [input('Digite o sexo da {}ª pessoa: '.format(c + 1))]
    print('')

for c in range(0, 4):
    soma += idades[c]

for c in range(0, 4):
    if sexo[c].lower() == 'masculino':
        if c > 0:
            if idades[c] > idades[c - 1]:
                maisvelho = c
        elif c == 0:
            maisvelho = c
    
    if sexo[c].lower() == 'feminino':
        if idades[c] < 20:
            menos20 += 1

print('A média de idade do grupo é: {}'.format(soma / len(idades)))
print('O nome do homem mais velho é: {}'.format(nomes[maisvelho]))
print('Quantidade de mulheres com menos de 20 anos: {}'.format(menos20))