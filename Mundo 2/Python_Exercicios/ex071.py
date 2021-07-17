cedulastotal = 0
céd = 50
valor = int(input('Digite o valor que deseja sacar: '))
total = valor

while True:
    if total >= céd:
        total -= céd
        cedulastotal += 1

    else:
        print(f'Total de {cedulastotal} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        cedulastotal = 0
        if total == 0:
            break
