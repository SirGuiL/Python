salario = float(input('Digite seu salário: '))

if salario > 1250:
    salario += salario / 10
    print('Seu novo salário é R${:.2f}'.format(salario))
else:
    salario += salario * 0.15
    print('Seu novo salário é de R${:.2f}'.format(salario))
