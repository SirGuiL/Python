from datetime import date

idades = []
maior = 0
menor = 0

for c in range(0, 7):
    idades += [int(input('Digite o ano de nascimento: '))]

for c in range(0, 7):
    if(date.today().year - idades[c] < 18):
        menor += 1
    else:
        maior += 1

print('{} já atingiram a maioridade.'.format(maior))
print('{} ainda não atingiram a maioridade.'.format(menor))
