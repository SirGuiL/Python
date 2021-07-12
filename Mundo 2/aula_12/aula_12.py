nome = input('Digite seu nome: ')

if (len(nome.strip()) == 0):
    print('Digite um nome =(')
else:
    if(len(nome.strip()) >= 10):
        print('Você tem um nome grande.')
    elif(len(nome.strip()) <= 4):
        print('Você tem um nome pequeno.')

    print('Tenha um ótimo dia, {}!'.format(nome))
