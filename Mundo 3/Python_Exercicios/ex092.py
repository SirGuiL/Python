from datetime import datetime
from time import sleep

data = dict()

data['name'] = input('Digite seu nome: ').title()

borndate = int(input('Digite seu ano de nascimento: '))

while True:
    option = input('Já fez aniversário esse ano? [S/N] ').upper()

    if option in 'SN':
        if option == 'S':
            data['age'] = datetime.now().year - borndate
        elif option == 'N':
            data['age'] = datetime.now().year - borndate - 1
        break

data['ctps'] = int(input('Carteira de trabalho (Digite 0 caso não tenha): '))

if data['ctps'] != 0:
    data['hiring'] = int(input('Digite o ano de contratação: '))
    data['salary'] = int(input('Digite seu salário: '))
    data['retirement'] = data['age'] + ((data['hiring'] + 35) - datetime.now().year)

print('=-'*30)
print(f'{"Imprimindo informações...":^60}')
print('=-'*30)
for key, value in data.items():
    sleep(1)
    print(f'{key}: {value}')
