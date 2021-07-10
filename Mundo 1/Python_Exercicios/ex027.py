nome = input('Digite seu nome: ')

if(len(nome.split()[0]) == len(nome)):
    print('Você tem apenas um nome')
else:
    print('Primeiro nome: {}'.format(nome.split()[0]))
    print('Ultimo nome: {}'.format(nome.split()[::-1][0]))
