from random import randint

print('Adivinhe o número que estou pensando:\nDica: É um número de 0 a 10\nBoa sorte =)')
num = int(input(''))
count = 0

randomNum = randint(1, 10)

while num != randomNum:
    if (num - randomNum < 3 and num - randomNum > -3):
        print('Foi por muito pouco!')
    else:
        print('Você errou.')
    num = int(input('Tente novamente!\n'))
    count += 1

print('Parabéns, você acertou!! \o/')
print('Foram necessárias {} tentativas'.format(count))
