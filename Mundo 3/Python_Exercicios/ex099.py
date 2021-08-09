from time import sleep

def higher(*num):
    count = higherNumber = 0

    print('Os valores digitados foram:')
    for number in num:
        print(f'{number} ', end='', flush=True)
        sleep(0.3)
        if higherNumber == 0:
            higherNumber = number
        elif number >= higherNumber:
            higherNumber = number
        count += 1

    print(f'\nForam informados {count} valores')
    print(f'O maior número digitado foi {higherNumber}')


higher(10, 5, 8, 4, 2)
