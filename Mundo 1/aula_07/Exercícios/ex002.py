print('O que deseja fazer?')
print('1 - adição')
print('2 - subtração')
print('3 - multiplicação')
print('4 - divisão')
print('5 - exponenciação')
print('6 - divisão inteira')
print('7 - resto de divisão')

opcao = int(input('_'))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

if(opcao == 1):
    print('O valor de {} mais {} é igual a {}'.format(n1, n2, n1 + n2))

elif(opcao == 2):
    print('O valor de {} menos {} é igual a {}'.format(n1, n2, n1 - n2))

elif(opcao == 3):
    print('O valor de {} multiplicado por {} é igual a {}'.format(n1, n2, n1 * n2))

elif(opcao == 4):
    print('O valor de {} dividido por {} é igual a {:.3f}'.format(n1, n2, n1 / n2))

elif(opcao == 5):
    print('O valor de {} elevado a {} é igual a {}'.format(n1, n2, n1 ** n2))

elif(opcao == 6):
    print('O valor da divisão inteira entre {} e {} é igual a'.format(n1, n2, n1 ** n2))

elif(opcao == 7):
    print('O valor do resto de divisão entre {} e {} é igual a {}'.format(n1, n2, n1 ** n2))

else:
    print('Opção inválida')
    print('Reinicie o programa e utilize uma opção válida.')
