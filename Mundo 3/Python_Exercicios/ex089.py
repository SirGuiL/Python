from time import sleep

alunos = list()

while True:
    while True:
        nome = input('Digite o nome do aluno: ').strip()
    
        if nome != '':
            break
        else:
            print('Digite algum nome.')
    
    while True:
        nota1 = float(input('Digite a primeira nota do aluno: '))

        if nota1 >= 0:
            break
        else:
            print('A nota deve ser no mínimo 0.')
    
    while True:
        nota2 = float(input('Digite a segunda nota do aluno: '))

        if nota2 >= 0:
            break
        else:
            print('A nota deve ser no mínimo 0.')
    
    media = (nota1 + nota2) / 2

    alunos.append([nome, nota1, nota2, media])

    while True:
        opc = input('Deseja continuar? [S/N]').upper()

        if opc in 'SN':
            break
    
    if opc == 'N':
        print('Processando resultados...')
        sleep(1)
        break

print(f'{"NOME":<20} | {"MÉDIA":>20}')
for aluno in alunos:
    print(f'{aluno[0]:<20} | {aluno[3]:>20}')

while True:
    opc = 'a'
    opc = input('Deseja mostrar a nota individual de algum aluno? [S/N] ').upper()

    if opc in 'SN':
        if opc == 'N':
            break

        elif opc == 'S':
            print('1 - Primeira nota\n2 - Segunda nota')
            nota = int(input('Digite qual nota quer mostrar: '))

            if nota == 1 or nota == 2:
                for i, a in enumerate(alunos):
                    print(f'{i + 1} - {a[0]}')

                while True:
                    aluno = int(input('Digite o número do aluno: '))

                    if aluno > len(alunos):
                        print('Número inválido.')
                    
                    else:
                        print(f'O aluno {alunos[aluno - 1][0]} tirou {alunos[aluno - 1][nota]} na {nota}ª avaliação')
                        break
            
            else:
                print('Número inválido.')
