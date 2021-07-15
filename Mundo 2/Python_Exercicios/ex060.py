num = int(input('Digite um número: '))
n = num
count = num

while count != 1:
    num *= count - 1
    count -= 1

print('{} fatorial é igual a {}'.format(n, num))

a = input('')