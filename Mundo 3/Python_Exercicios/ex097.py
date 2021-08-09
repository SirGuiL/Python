def write(phrase):
    length = len(phrase) + 4
    print('~'*length)
    print(f'  {phrase}')
    print('~'*length)

phrase = input('Digite uma frase: ')

write(phrase)
