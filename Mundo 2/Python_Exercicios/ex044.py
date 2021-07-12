valor = float(input('Digite o preço do produto: '))

print('1 - Dinheiro/Cheque (10{} de desconto)'.format('%'))
print('2 - À vista no cartão (5{} de desconto)'.format('%'))
print('3 - Em até 2x no cartão (Preço normal)')
print('4 - 3x ou mais no cartão (20{} de juros)'.format('%'))

formapagamento = int(input('\nDigite o código da forma de pagamento: '))

if(formapagamento == 1):
    valor = valor - valor*0.1
elif(formapagamento == 2):
    valor = valor - valor*0.05
elif(formapagamento == 4):
    valor = valor + valor*0.2
elif(formapagamento > 4):
    print('Código inválido.')
    exit()

print('Valor final: R${}'.format(valor))
