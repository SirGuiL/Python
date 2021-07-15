num = int(input('Digite o tamanho que deseja na sequência: '))
counter = 0
n1 = 0
n2 = 1

print('{} -> {} -> '.format(n1, n2), end='')

while counter <= num:
    n3 = n1 + n2

    print('{} -> '.format(n3), end='')
    
    n1 = n2
    n2 = n3

    counter += 1
