from random import randint
from time import sleep

num = escolha = res = 0

print('ÍMPAR OU PAR')
print('1 - Par\n2 - Ímpar')

while True:
    escolha = int(input('Escolha ímpar ou par: '))
    if escolha > 2 or escolha < 0:
        print('Opção inválida')
        break
    num = int(input('Digite um número: '))
    n = randint(1, 10)

    if (num + n) % 2 == 0: res = 1
    else: res = 2

    if res == escolha: print(f'Eu escolhi {n} e você escolheu {num}, você venceu!')
    else: 
        print(f'Eu escolhi {n} e você escolheu {num}, eu venci!')
        break
    sleep(1)
