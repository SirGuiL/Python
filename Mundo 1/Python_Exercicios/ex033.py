num = []
count = 1

while count <= 3:
    num += [int(input('Digite um número: '))]
    count+=1

num.sort()

print('{} é o maior número'.format(num[2]))
