soma_idade = 0
numero_mulheres_novas = 0
homem_mais_velho = 0
homem_mais_velho_idade = 0

for i in range(0,4):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]')).strip()
    soma_idade += idade
    if sexo[0].upper() == 'M' and homem_mais_velho_idade < idade:
        homem_mais_velho = nome 
        homem_mais_velho_idade = idade 
    if sexo[0].upper() == 'F' and idade < 20:
        numero_mulheres_novas += 1

media_idades = soma_idade / 4

print('A média de idade {} ano(s)'.format(media_idades))
print('O homem mais velho é o {} com {} anos'.format(homem_mais_velho, homem_mais_velho_idade))
print('O número de mulheres com menos de 20 anos é {}'.format(numero_mulheres_novas))

