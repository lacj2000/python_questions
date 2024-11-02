notas = map(float, input().split())
pesos = [2, 3, 4, 1]

soma_ponderada = sum(nota * peso for nota, peso in zip(notas, pesos))
soma_pesos = sum(pesos)
media_ponderada = soma_ponderada / soma_pesos

print(f'Media: {media_ponderada:.1f}')
if media_ponderada >= 7.0:
    print(f'Aluno aprovado.')
elif media_ponderada < 5.0:
    print(f'Aluno reprovado.')
else:
    print(f'Aluno em exame.')
    nota_exame = float(input())
    print(f'Nota do exame: {nota_exame:.1f}')
    media_final = (media_ponderada + nota_exame )/2
    if media_final >= 5.0:
        print(f'Aluno aprovado.')
    else:
        print(f'Aluno reprovado.')
    print(f'Media final: {media_final:.1f}') 