# Variáveis composta (Dicionários)

# dados = dict()
dados = {
    'nome': 'Guilherme',
    'idade': 18
}

print(dados['nome']) # Retorna Guilherme
print(dados['idade']) # Retorna 18

dados['sexo'] = 'M' # Adiciona o elemento sexo e adiciona a informação M

print(dados['sexo']) # Retorna M

del dados['idade'] # Deleta o elemento idade

filme = {
    'titulo': 'Star Wars',
    'ano': 1997,
    'diretor': 'George Lucas'
}

print(filme.values()) # Retorna os valores do dicionário
print(filme.keys()) # Retorna as chaves do dicionário
print(filme.items()) # Retorna o dicionário completo

for key, value in filme.items():
    print(f'O {key} é {value}')

locadora = list()

locadora.append(filme.copy())

print(locadora)

for cont in range(0, 3):

    titulo = input('Digite o nome do filme: ')
    ano = int(input('Digite o ano do filme: '))
    diretor = input('Digite o nome do diretor: ') 

    filme['titulo'] = titulo
    filme['ano'] = ano
    filme['diretor'] = diretor

    locadora.append(filme.copy())

print(locadora)

a = input('a')