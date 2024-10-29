n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
media = ( n1 + n2 )/2

if media < 5:
    print('Reprovado!')
elif media < 7:
    print('Recuperação!')
else:
    print('Aprovado!!! Parabéns')
