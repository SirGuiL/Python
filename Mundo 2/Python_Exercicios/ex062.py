num = int(input('Digite o termo: '))
razao = int(input('Digite a razão da PA: '))
termo = num
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais

    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('...')
    
    mais = int(input('\nQuantos termos você quer mostrar a mais? '))

a = input('a')