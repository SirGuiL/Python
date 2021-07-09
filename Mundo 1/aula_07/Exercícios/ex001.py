nome = input('Digite seu nome: ')

# Utilizando 20 caracteres para a variavel nome
print('Prazer em conhecê-lo {:20}!'.format(nome)) 
# Utilizando 20 caracteres para a variavel nome e alinhando a direita
print('Prazer em conhecê-lo {:>20}!'.format(nome))
# Utilizando 20 caracteres para a variavel nome e alinhando a esquerda 
print('Prazer em conhecê-lo {:<20}!'.format(nome)) 
# Utilizando 20 caracteres para a variavel nome e alinhando ao centro
print('Prazer em conhecê-lo {:^20}!'.format(nome)) 
# Utilizando 20 caracteres para a variavel nome e alinhando ao centro e cercado pelos caracteres escolhidos
print('Prazer em conhecê-lo {:=^20}!'.format(nome))

n = input('a')