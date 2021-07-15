num = 0
count = 0
opc = 0

while opc != 999:
    num += opc
    opc = int(input('Digite um número inteiro: '))
    count += 1

print('Foram digitados {} números, e a soma deles é: {}'.format(count - 1, num))
a = input('a')