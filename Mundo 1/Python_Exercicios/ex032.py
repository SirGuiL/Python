from datetime import date

ano = int(input('Digite um ano: (0 para utilizar o ano atual.) '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0:
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))
