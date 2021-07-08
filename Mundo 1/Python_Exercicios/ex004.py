tipo = input('Digite algo: ')

print('O tipo primitivo de {} é {}'.format(tipo, type(tipo)))

print('Alpha', tipo.isalpha())
print('Numeric', tipo.isnumeric())
print('Alphanumeric', tipo.isalnum())
print('Lowercase', tipo.islower())
print('Uppercase', tipo.isupper())
print('Spaces', tipo.isspace())
print('Capitalized', tipo.istitle())
