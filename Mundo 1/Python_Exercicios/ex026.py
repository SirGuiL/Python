frase = input('Digite uma frase: ')

if(frase.count('A') > 1):
    print("A letra 'A' aparece {} vezes".format(frase.count('A')))
    print('Aparece pela primeira vez na posição {}'.format(frase.find('A') + 1))
    print('Aparece pela ultima vez na posição {}'.format(len(frase) - frase[::-1].find('A')))
elif(frase.count('A') == 1):
    print("A letra 'A' aparece {} vez na posição {}".format(frase.count('A'), frase.find('A')))
else:
    print("A letra 'A' não aparece na frase")
