from datetime import date

ano = int(input('Digite seu ano de nascimento: '))

idade = date.today().year - ano

if(idade <= 9):
    print('Você se encaixa na categoria mirim.')
elif(idade <= 14):
    print('Você se encaixa na categoria infantil.')
elif(idade <= 19):
    print('Você se encaixa na categoria junior.')
elif(idade == 20):
    print('Você se encaixa na categoria sênior.')
else:
    print('Você se encaixa na categoria master.')

a = input('a')