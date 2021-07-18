from random import randint
from time import sleep

grupoA = [
    'América-MG',
    'Atlético-MG',
    'Bahia',
    'Ceará SC',
    'Corinthians',
    'Flamengo',
    'Fluminense',
    'Fortaleza',
    'Internacional',
    'Sport Recife'
]

grupoB = [
    'Palmeiras',
    'RB Bragantino',
    'Athletico-PR',
    'Santos',
    'Atlético-GO',
    'Juventude',
    'São Paulo',
    'Cuiabá',
    'Grêmio',
    'Chapecoense'
]

arrayTime1 = []
arrayTime2 = []
jogos = []

while True:
    time = randint(0, 9)

    if time not in arrayTime1:
        arrayTime1.append(time)
    
    if len(arrayTime1) == 10:
        break

while True:
    time = randint(0, 9)

    if time not in arrayTime2:
        arrayTime2.append(time)
    
    if len(arrayTime2) == 10:
        break

for c in range(0, 10):
    if c == 0:
        print('Abertura da rodada.')
    elif c == 9:
        print('Encerramento da rodada')
    else:
        print(f'jogo {c + 1}')

    if c % 2 == 0:
        casa = arrayTime1[c]
        fora = arrayTime2[c]
        print(f'{grupoA[casa]} X {grupoB[fora]}')
        jogos.append(f'{grupoA[casa]} X {grupoB[fora]}')
    else:
        casa = arrayTime2[c]
        fora = arrayTime1[c]
        print(f'{grupoB[casa]} X {grupoA[fora]}')
        jogos.append(f'{grupoB[casa]} X {grupoA[fora]}')

    
    while True:
        confirm = input('Confirme esse jogo: [S/N] ').upper()

        if confirm in 'SN':
            if confirm == 'N':
                print('Que pena.')
                break
            else:
                print('Continuando...')
                sleep(1)
                break

print('\n')

for c in range(0, 10):
    print(jogos[c])

a = input('a')