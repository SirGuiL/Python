cidade = input('Digite o nome de uma cidade: ')

res = (cidade.split()[0].lower().find('santo'))

if(res != -1 and cidade.split()[0].lower() == 'santo'):
    print("O nome da cidade começa com 'SANTO'.")

else:
    print("O nome da cidade não começa com 'SANTO'.")

cidade = input('Digite o nome de uma cidade: ')