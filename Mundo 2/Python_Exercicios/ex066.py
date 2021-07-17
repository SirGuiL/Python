num = soma = count = 0

while True:
    num = int(input('Digite um número: (999 para o programa)'))
    if num == 999: break
    count += 1
    soma += num

if count > 1: print(f'A soma entre os {count} números é {soma}')
else: print(f'Você só digitou um número, logo a soma é {soma}')
