km = float(input('Digite a velocidade do carro: '))

if km > 80:
    print('Você está acima da velocidade e será multado no valor de R${}'.format((km - 80) * 7))
else:
    print('Você está dentro do limite de velocidade, continue assim.')
