from time import sleep

player = dict()
goals = list()
players = list()
option = str
totalgoals = 0

while True:
    if option == 'N':
        break

    player['name'] = input('Digite o nome do jogador: ')
    
    numgames = int(input('Digite a quantidade de jogos: '))

    for game in range(0, numgames):
        goals.append(int(input(f'Digite a quantidade de gols na {game + 1}ª partida: ')))

    player['goals'] = goals[:]
    
    for goal in goals:
        totalgoals += goal
    
    player['total'] = totalgoals
    player['games'] = numgames
    totalgoals = 0

    while True:
        option = input('Deseja continuar? [S/N] ').upper()

        if option in 'SN':
            break
    
    players.append(player.copy())
    goals.clear()


option = str

while True:
    if option == 'N':
        break

    print(f'{"cod":<5}', end='')
    print(f'{"nome":<15}', end='')
    print(f'{"gols":<25}', end='')
    print('total')

    for k, p in enumerate(players):
        print(f'{(k + 1):<5}{p["name"]:<15}{str(p["goals"]):<25}{p["total"]}')
    
    option = int(input('Digite o código do jogador para visualizar detalhes: '))
    if option <= len(players):
        print(f'Imprimindo os dados de {players[option-1]["name"]}...')
        sleep(1)

        print(f'O jogador tem uma média de {(players[option-1]["total"] / numgames):.2f} gols por partida')

        for x in range(0, players[option - 1]['games']):
            if players[option - 1]["goals"][x] == 1:
                print(f'{players[option - 1]["goals"][x]} gol na {x + 1}ª partida')
            elif players[option - 1]["goals"][x] > 1:
                print(f'{players[option - 1]["goals"][x]} gols na {x + 1}ª partida')
            else:
                print(f'não marcou gols na {x + 1}ª partida')
        
        while True:
            option = input('Deseja continuar? [S/N]').upper()

            if option in 'SN':
                break
    else:
        print('Código inválido')
