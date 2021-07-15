n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
menu = 0

print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n')

while menu != 5:
    menu = int(input('Escolha uma opção: '))
    if (menu == 1):
        print('A soma entre {} e {} é igual a {}'.format(n1, n2, n1 + n2))
    elif (menu == 2):
        print('A multiplicação entre {} e {} resulta em {}'.format(n1, n2, n1 * n2))
    elif (menu == 3):
        if (n1 > n2):
            print('{} é maior que {}'.format(n1, n2))
        else:
            print('{} é maior que {}'.format(n2, n1))
    elif (menu == 4):
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))

        print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n')
    elif (menu == 5):
        print('Obrigado por utilizar o programa, até mais =)')
    else:
        print('Valor inválido.')
