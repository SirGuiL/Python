# Fatiando uma string
frase = 'Curso de Python.'

print(frase[5]) # Começo
print(frase[5:10]) # Começo e fim
print(frase[5:10:2]) # Pulando de dois em dois
print(frase[:5]) # Onde vai terminar
print(frase[5:]) # Onde vai começar (continuando até terminar a string)
print(frase[5::3]) # Começa no 5 e vai até o final pulando de 3 em 3

# Análise de string
len(frase) # Tamanho da string
print(frase.count('o'))  # Quantidade de vezes que 'o' aparece na string
print(frase.count('o', 0, 13))  # Count com string fatiada
print(frase.find('deo'))  # Busca 'deo' dentro da string
print('Curso' in frase) # Vai buscar 'Curso' dentro da string
print(frase.replace('Python', 'JavaScript')) # Substitui 'Python' por 'Android'
print(frase.upper()) # Transforma a string em maiúsculo
print(frase.lower()) # Transforma a string em minúsculo
print(frase.capitalize()) # Todos caracteres para minúsculo, e a primeira letras para maiúscula
print(frase.title()) # Transforma todas primeiras letras em maiúsculo e todos demais em minúsculo
print(frase.strip()) # Remove os espaços sem utilidade na frase (começo e fim)
print(frase.lstrip()) # Remove os espaços sem utilidade no lado esquerdo da frase
print(frase.rstrip()) # Remove os espaços sem utilidade no lado direito da frase
print(frase.split()) # Divide a string baseando nos espaços

# Junção de strings
print('-'.join(frase)) # Separa letra por letra com '-'
print('-'.join(frase.split())) # Utilizando as separações das palavras com o split, faz a junção com '-'

print(frase)

a = input('a')