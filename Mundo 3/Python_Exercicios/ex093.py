data = dict()
goals = list()
total = count = 0

data['name'] = input('Digite o nome do jogador: ')
numgames = int(input('Digite a quantidade de jogos: '))

for games in range(0, numgames):
    goals.append(int(input(f'Quantos gols ele fez na partida {games + 1}? ')))

for totalgoals in goals:
    total += totalgoals

data['goals'] = goals
data['total'] = total

for key, item in data.items():
    if key == 'goals':
        while count < numgames:
            if numgames > 1:
                if goals[count] == 1:
                    print(f'No {count + 1}º jogo marcou {goals[count]} gol')
                elif goals[count] > 1:
                    print(f'No {count + 1}º jogo marcou {goals[count]} gols')
                else:
                    print(f'Não marcou gols no {count + 1}º jogo')
            else:
                if goals[count] == 1:
                    print(f'Marcou 1 gol no jogo')
                elif goals[count] > 1:
                    print(f'Marcou {goals[count]} gols no jogo')
                else:
                    print(f'Não marcou gols no jogo')
            count += 1
    else:    
        print(f'{key}: {item}')

average = total / numgames

if average == 1:
    print(f'Tem uma média de {average} gol por partida')
else:
    print(f'Tem uma média de {average} gols por partida')
