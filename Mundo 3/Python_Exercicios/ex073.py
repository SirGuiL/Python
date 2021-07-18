times = (
    'Náutico',
    'Coritiba',
    'Guarani',
    'Goiás',
    'Sampaio Corrêa',
    'Avaí',
    'Operário',
    'Vasco da Gama',
    'CRB',
    'Brusque',
    'CSA',
    'Vila Nova',
    'Botafogo',
    'Remo',
    'Brasil de Pelotas',
    'Cruzeiro',
    'Confiança',
    'EC Vitória',
    'Ponte Preta',
    'Londrina'
)

print('Os cinco primeiros:')

for cont in range(0, 5):
    print(f'{cont + 1}. {times[cont]}')

print('\nZona de rebaixamento:')

for cont in range (0, 4):
    print(f'{20 - cont}. {times[19 - cont]}')

sortedtimes = sorted(times)

print('\nTimes em ordem alfabética:')

for cont in range (0, 20):
    print(f'{cont + 1}. {sortedtimes[cont]}')

cruzeiro = times.index('Cruzeiro')

print(f'\nO time do Cruzeiro se encontra na {cruzeiro + 1}º posição.')
