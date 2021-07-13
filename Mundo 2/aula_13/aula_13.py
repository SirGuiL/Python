# Laços de repetição
# Notas
num = int(input('Digite quantas notas deseja adicionar: '))
notas = []
nota = 0

print(nota)

for count in range(0, num):
    notas += [float(input('Digite a {}ª nota: '.format(count + 1)))]

for counter in range(0, len(notas)):
    nota += notas[counter]

media = nota / (counter + 1)

print('Você obteve {} de média'.format(media))

if media >= 7.5:
    print('Parabéns, você foi aprovado!')
elif media > 4:
    print('Você ficou de recuperação.')
else:
    print('Reprovado.')

# For
for c in range(0, 6): # Laço for indo de 0 a 6
    print(c)

for c in range(6, 0, -1): # Laço for indo de 6 a 0
    print(c)


# palíndromo

word = input('Digite uma palavra: ')

if word.strip() == word.strip()[::-1]:
    print('{} é um palíndromo'.format(word.strip().capitalize()))
else: 
    print('{} não é um palíndromo'.format(word.strip().capitalize()))
