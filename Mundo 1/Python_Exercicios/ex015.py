dias = int(input('Digite a quantidade de dias alugado: '))
km = float(input('Digite a quantidade de quilometros rodados: '))

print('Total a pagar: R${:.2f}'.format((60 * dias) + (0.15 * km)))
