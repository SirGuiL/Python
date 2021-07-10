# Parte 1
tempo = int(input('Quantos anos tem seu carro? '))

print('Carro novo' if tempo <= 3 else 'Carro velho') # Condição simplificada

print('----Fim----')

# Parte 2
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1+n2)/2

print('Você obteve {} de média: {}'.format(media))

if media >= 7.5:
    print('Aprovado!')
else:
    print('Reprovado')
