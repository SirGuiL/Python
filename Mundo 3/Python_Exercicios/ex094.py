data = dict()
datalist = list()
option = str
age = 0

while True:
    if option == 'N':
        break

    data['name'] = input('Digite seu nome: ').title()
    
    while True:
        data['gender'] = input('Digite seu sexo: [M/F] ').upper()

        if data['gender'] in 'MF':
            if data['gender'] == 'M':
                data['gender'] = 'Masculino'
            else:
                data['gender'] = 'Feminino'
            break
        else:
            print('Código inválido.')
    
    data['age'] = int(input('Digite sua idade: '))

    while True:
        option = input('Deseja continuar? [S/N] ').upper()

        if option in 'SN':
            break
    age += data['age']
    datalist.append(data.copy())

print(f'\nForam cadastradas {len(datalist)} pessoas.')
print(f'A média de idade do grupo é {age/len(datalist)}')

print('\nLista de todas mulheres cadastradas: ')
for people in datalist:
    if people['gender'] == 'Feminino':
        print(people['name'])

print('\nLista de todas as pessoas com idade acima da média: ')
for people in datalist:
    if people['age'] >= age / len(datalist):
        print(people['name'])
