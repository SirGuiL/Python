import random

nome = []
count = 1

while count <= 4:
    nome += [input('Digite o nome do aluno: ')]
    count += 1

print('O aluno sorteado foi: {}'.format(nome[random.randint(1, count)]))
