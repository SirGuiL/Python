# Variáveis Compostas (Listas) parte 2

dados = list()
pessoa = list()

dados.append('Guilherme')
dados.append(18)

pessoa.append(dados[:])

print(pessoa)
print(pessoa[0][0]) # Retorna Guilherme
print(pessoa[0][1]) # Retorna 18

pessoa.clear() # Limpa a lista
print(pessoa)

galera = [['Guilherme', 18], ['Ana', 22], ['João', 56], ['Maria', 29]]

for p in galera:
    print(f'{p[0]} tem {p[1]} anos.')

a = input('a')