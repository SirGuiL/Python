from random import randint
from time import sleep

print('1 - Pedra\n2 - Papel\n3 - Tesoura')
num = int(input('Escolha o código de pedra, papel ou tesoura: '))

pcnum = randint(1, 3)

if pcnum == 1: pcstring = 'Pedra'
elif pcnum == 2: pcstring = 'Papel'
else: pcstring = 'Tesoura'

print('jo')
sleep(1)
print('ken')
sleep(1)
print('po')
sleep(1)

print('Eu escolhi {}.'.format(pcstring.lower()))

if num == 1:
    if pcnum == 1:
        print('Empatamos!')
    elif pcnum == 2:
        print('Eu venci!')
    else:
        print('Você venceu!')

elif num == 2:
    if pcnum == 1:
        print('Você venceu!')
    elif pcnum == 2:
        print('Empatamos!')
    else:
        print('Eu venci!')

elif num == 3:
    if pcnum == 1:
        print('Eu venci!')
    elif pcnum == 2:
        print('Você venceu!')
    else:
        print('Empatamos!')
