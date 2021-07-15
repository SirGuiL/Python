sexo = input('Digite seu sexo: [F/M]').upper()

while sexo not in 'MF':
    sexo = input('Dados inválidos, digite seu sexo: ').upper()

if(sexo == 'M'):
    print('Bem vindo.')
else:
    print('Bem vinda.')
