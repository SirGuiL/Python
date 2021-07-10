distancia = int(input('Digite a distância (em Km) da viagem: '))

if distancia <= 200:
    print('O valor da passagem é de R${:.2f}'.format(distancia * 0.5))
else:
    print('O valor da passagem é de R${:.2f}'.format(distancia * 0.45))
