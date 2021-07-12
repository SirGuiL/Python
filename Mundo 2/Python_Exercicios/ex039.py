from datetime import date

ano = int(input('Digite o ano de seu nascimento: '))

if(date.today().year - ano < 18):
    print('Você ainda vai se alistar.')
    if(18 - (date.today().year - ano) == 1):
        print('Falta {} ano para seu alistamento.'.format(18 - (date.today().year - ano)))
    else:
        print('Faltam {} anos para seu alistamento.'.format(18 - (date.today().year - ano)))
elif(date.today().year - ano == 18):
    print('É hora de se alistar.')
else:
    print('Já passou da hora de se alistar.')

    if((date.today().year - ano) - 18 == 1):
        print('Devia ter se alistado a {} ano'.format((date.today().year - ano) - 18))
    else:
        print('Devia ter se alistado a {} anos'.format((date.today().year - ano) - 18))
