dia = input('Digite o dia do seu nascimento: ')
mes = input('Digite o mês do seu nascimento: ')
ano = input('Digite o ano do seu nascimento: ')

print('Você nasceu no dia', dia, 'do', mes, 'de', ano, ', certo? (s para sim e n para não)')

confirm = input('')

if(confirm == 's'):
    print('Você nasceu no dia', dia, '/', mes, '/', ano)
elif(confirm == 'n'):
    print('Poxa, reinicie o programa e preencha novamente :(')
else:
    print('Resposta inválida.')
