nome = input('Digite sue nome: ')

print('Com todas letras maiúsculas: {}'.format(nome.upper()))
print('Com todas letras minúsculas: {}'.format(nome.lower()))
print('Quantidade de letras do nome completo: {}'.format(len(''.join(nome.split()))))
print('Quantidade de letras do primeiro nome: {}'.format(len(nome.split()[0])))
