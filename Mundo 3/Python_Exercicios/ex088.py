from random import randint
from time import sleep

lista = list()
jogos = list()

print('-'*39)
print(f'{"Gerador de palpites da MEGA SENA":^39}')
print('-'*39)

numjogos = int(input('Quantos jogos devem ser gerados: '))

if numjogos > 1:
    print('-'*39)
    print('-'*10, f'Sorteando {numjogos} jogos','-'*10)
    print('-'*39)
elif numjogos == 0:
    print('Erro: você não pode pedir para sortear 0 jogos.')
    while True:
        a = input('Feche o programa.')
else:
    print('-'*39)
    print(f'{"Sorteando 1 jogo":^39}')
    print('-'*39)

for j in range(0, numjogos):
    count = 0
    while count < 6:
        num = randint(1, 60)

        if num not in lista:
            lista.append(num)
            count += 1
    
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    sleep(1)
    print(f'jogo {j + 1}: {jogos[j]}')

print('-'*39)
print(f'{"Boa sorte!":^39}')
print('-'*39)
