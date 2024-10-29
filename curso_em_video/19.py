from random import choice

alunos = []

for i in range(0,4):
    alunos.append(input('Digite o nome do {}º aluno: '.format(i+1)))


aluno_sorteado = choice(alunos)

print('Aluno Sorteado: {}'.format(aluno_sorteado))
