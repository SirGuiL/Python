aluno = dict()

aluno['nome'] = str(input('Digite o nome do aluno: ')) 
aluno['média'] = float(input('Digite a média do aluno: '))

if aluno['média'] >= 7.5:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] >= 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

if aluno['situação'] == 'Reprovado':
    print(f'{aluno["nome"].title()} tirou {aluno["média"]} de média, logo ele está de {aluno["situação"].upper()}.')
else:
    print(f'{aluno["nome"].title()} tirou {aluno["média"]} de média, logo ele está {aluno["situação"].upper()}.')

a = input('a')