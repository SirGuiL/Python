from random import randint
grupoA = []
grupoB = []
times = [
    'Palmeiras',
    'Atlético-MG',
    'Fortaleza',
    'RB Bragantino',
    'Athletico-PR',
    'Flamengo',
    'Ceará SC',
    'Bahia',
    'Fluminense',
    'Santos',
    'Atlético-GO',
    'Corinthians',
    'Juventude',
    'São Paulo',
    'Internacional',
    'América-MG',
    'Cuiabá',
    'Sport Recife',
    'Grêmio',
    'Chapecoense'
]
num = int
c = 0
arrayTime1 = []
arrayTime2 = []

while True:
    num = randint(0, 19)

    if num <= len(times):
        time = times[num]
        grupoA.append(times[num])
        times.remove(time)
    
    if len(grupoA) == 10:
        break

grupoB = times[:]

grupoA.sort()
grupoB.sort()

print('Grupo A:')
for c in grupoA: # Retorna a lista de times (em ordem alfabética) do grupo A
    print(c)

print('\nGrupo B:')
for b in grupoB: # Retorna a lista de times (em ordem alfabética) do grupo A
    print(b)

x = input('x')