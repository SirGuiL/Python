from random import randint
from time import sleep

def draw():
    print('Sorteando os números...')
    sleep(0.5)
    for count in range(0, 5):
        num = randint(1, 100)
        numbers.append(num)
        print(f'{num} ', end='', flush=True)
        sleep(0.3)

def addEven(numbers):
    even = 0
    print('\nSomando os pares...')
    sleep(0.5)

    for number in numbers:
        if number % 2 == 0:
            even += number

    print(f'A soma dos pares resulta em {even}')


numbers = list()
draw()
addEven(numbers)
