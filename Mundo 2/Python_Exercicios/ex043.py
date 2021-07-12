peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / altura**2

if imc < 18.5:
    print('Você está abaixo do peso.')
    print('Seu IMC é: {:.2f}'.format(imc))
elif imc < 25:
    print('Você está no peso ideal.')
    print('Seu IMC é: {:.2f}'.format(imc))
elif imc < 30:
    print('Você está com sobrepeso.')
    print('Seu IMC é: {:.2f}'.format(imc))
elif imc < 40:
    print('Você está com obesidade.')
    print('Seu IMC é: {:.2f}'.format(imc))
else:
    print('Você está com obesidade mórbida.')
    print('Seu IMC é: {:.2f}'.format(imc))
