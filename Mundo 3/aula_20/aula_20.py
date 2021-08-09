# funções em python (def)
def mostraLinha():
    print('-'*30)

def mensagem(msg):
    mostraLinha()
    print(f'{msg:^30}')
    mostraLinha()

def soma(*num):
    count = 0
    for valor in num:
        count += valor
        if valor == num[len(num) - 1]:
            print(f'{valor}', end=' ')
        else:
            print(f'{valor} +', end=' ')
    print(f'= {count}')

def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1


# programa principal
values = [1, 3, 7, 4]
mostraLinha()
mensagem('mensagem pelo parametro')
soma(2, 1, 6)
print(values)
dobra(values)
print(values)
a = input('a')