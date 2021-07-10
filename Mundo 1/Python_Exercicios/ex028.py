import random

print('Adivinhe o número que estou pensando:\nDica: É um número de 0 a 10\nBoa sorte =)')
num = int(input(''))

randomNum = random.randint(1, 10)

if num == randomNum:
    print('Parabéns, você acertou!!')
elif (num - randomNum < 3 and num - randomNum > -3):
    print('Foi por muito pouco!')
else:
    print('Boa tentativa, mas não foi dessa vez =)')

print('Eu pensei em {} =)'.format(randomNum))
