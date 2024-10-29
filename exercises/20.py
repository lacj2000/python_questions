from random import sample

alunos = []

for i in range(0,4):
    alunos.append(input('Digite o nome do {}º aluno: '.format(i+1)))


sequencia_de_alunos = sample(alunos, k = len(alunos))

print('Ordem de apresentação: {}'.format(sequencia_de_alunos))
