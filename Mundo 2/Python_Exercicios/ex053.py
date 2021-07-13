import unicode

phrase = input('Digite uma frase: ')

phrasejoin = unidecode(''.join(phrase.strip().split()).lower())

if phrasejoin == phrasejoin[::-1]:
    print('{} é um palíndromo'.format(phrase.strip().capitalize()))
else:
    print('{} não é um palíndromo'.format(phrase.strip().capitalize()))
