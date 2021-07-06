nome = input('Digite seu nome: ')
print('Digite seu sexo: ')
sexo = input('1 - Masculino; \n2 - Feminino. \n')
if(sexo == '1'):
    print('Bem-vindo', nome)
elif(sexo == '2'):
    print('Bem-vinda', nome)
else:
    print('Digite um número válido.')
