notas = []
count = 1

while count <= 2:
    notas += [float(input('Digite a {} nota: '.format(count)))]
    count += 1

media = (notas[0] + notas[1]) / 2

if(media < 5):
    print('Você infelizmente foi reprovado com a média de {}.'.format(media))
elif(media >= 5 and media < 7):
    print('Estude para o exame final, você ficou de recuperação com uma média de {}.'.format(media))
else:
    print('Parabéns, você foi aprovado com uma média de {}.'.format(media))
