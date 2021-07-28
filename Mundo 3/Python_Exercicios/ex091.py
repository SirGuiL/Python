from random import randint
from time import sleep

finaldata = list()
data = dict()
players = list()
dices = list()
counter = 1

for player in range(0, 4):
    players.append(input(f'Digite o {player + 1}º nome: '))



for dice in range(0, 4):
    print(f'Rodando o dado para {players[dice]}...')
    sleep(1)
    numdice = randint(1, 6)

    data[players[dice]] = numdice

    print(f'Seu dado deu {numdice}')

sort_dices = sorted(data.items(), key = lambda x:x[1], reverse=True)

print(players)
print(data)

numdice = 0

for player in sort_dices:
    sleep(1)

    if numdice == 0:
        numdice = player[1]
    elif player[1] != numdice:
        numdice = player[1]
        counter += 1
    
    print(f'{counter}º lugar: {player[0]} com {player[1]}')
    
    


a = input('a')