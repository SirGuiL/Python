import random

nome = []
count = 1
x = 1
nums = []

while count <= 4:
    nome += [input('Digite o nome do aluno: ')]
    count += 1

while x <= 4:
    num = random.randint(1, 4)

    if(num in nums):
        x += 0
        
    else:
        nums += [num]
        print('{} - {}'.format(x, nome[num-1]))
        x += 1
