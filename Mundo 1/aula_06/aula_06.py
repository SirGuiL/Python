# Primeira parte da aula
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

soma = n1 + n2

print('A soma entre {0} e {1} é {2}'.format(n1, n2, soma))

# Segunda parte da aula
palavra = input('Digite uma palavra: ')
numero = input('Digite um número: ')

print(palavra.isnumeric()) # Diz se é um número
print(palavra.isalpha())
print(numero.isalpha()) # Diz se é uma palavra
print(numero.isnumeric()) 
print(palavra.isalnum()) # Diz se é alfanumérico