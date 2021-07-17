idade = mais18 = homens = menos20 = 0
sexo = opc = str

while True:
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo [F/M]: ').upper()
    if sexo not in 'FM': 
        print('Digite um sexo válido.')
        break

    if idade > 18: mais18 += 1

    if sexo == 'M': homens += 1

    if sexo == 'F' and idade < 20: menos20 += 1

    opc = input('Deseja continuar? [S/N] ').upper()

    if opc != 'S': break

print(f'{mais18} tem mais de 18 anos\n{homens} homens\n{menos20} mulheres tem menos de 20 anos.')
print('Fim do programa.')
