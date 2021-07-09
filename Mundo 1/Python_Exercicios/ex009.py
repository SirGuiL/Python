num = int(input('Digite um número: '))
count = 1

# for x in range(10):
#     print('{} X {} = {}'.format(num, x + 1, num * (x + 1)))

while count <= 10:
    print('{} X {} = {}'.format(num, count, num * (count)))
    count+=1
