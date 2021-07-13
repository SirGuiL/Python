soma = 0
count = 0

for c in range(0, 500):
    if(c % 2 == 1 and c % 3 == 0):
        soma += c
        count += 1

print('Ao todo foram {} números somados\nResultando em {}'.format(count, soma))
a = input('a')