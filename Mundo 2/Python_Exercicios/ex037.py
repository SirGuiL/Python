num = int(input('Digite o número que deseja converter: '))

print('1 - Binário\n2 - Octal\n3 - Hexadecimal')

opcao = int(input('Digite o número da base de conversão escolhida: '))

if(opcao == 1):
    print('{} em base binária é igual a {}'.format(num, str(bin(num))[2:]))
elif(opcao == 2):
    print('{} em base octal é igual a {}'.format(num, str(oct(num))[2:]))
elif(opcao == 3):
    print('{} em base hexadecimal é igual a {}'.format(num, str(hex(num))[2:]))
else:
    print('Digite uma opção válida.')
