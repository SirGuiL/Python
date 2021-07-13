nums = []
soma = 0
count = 0

for c in range(0, 6):
    nums += [int(input('Digite o {}º número: '.format(c+1)))]

for c in range(0, 6):
    if(nums[c] % 2 == 0):
        soma += nums[c]
        count += 1

print('A soma entre os {} valores pares resulta em {}'.format(count, soma))
