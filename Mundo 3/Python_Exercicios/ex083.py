expressão = input('Digite uma expressão numérica: ')

if expressão.count('(') == expressão.count(')'):
    print('A quantidade de parênteses está correta.')
else:
    print('A quantidade de parênteses está inválida.')
