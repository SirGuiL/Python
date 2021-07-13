num = int(input('Digite um número: '))
count = 0

for c in range(1, num):
    if(num % c == 0):
        count += 1

if(count > 1):
    print('O número não é primo.')
else:
    print('O número é primo')

a = input('a')