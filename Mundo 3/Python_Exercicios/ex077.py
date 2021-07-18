palavras = (
    'Teste',
    'Copo',
    'Lanterna',
    'Mesa',
    'Travesseiro',
    'Mouse',
    'Cadeira'
)

for palavra in palavras:
    print(f'\nEm {palavra.upper()} encontramos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')