valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
anos = int(input('Em quantos anos pretende pagar? '))

meses = anos * 12

valor_mensal = valor_casa / meses

if(valor_mensal > salario * 0.3):
    print('Empréstimo negado.')
else:
    print('Empréstimo aprovado.')
    print('Você pagará parcelas no valor de R${:.2f} por mês'.format(valor_mensal))
