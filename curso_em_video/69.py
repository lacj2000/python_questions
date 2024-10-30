maiores = 0
homens = 0
mulheres_menor_20 = 0 
while True:
    print('-='*15)
    print('Cadastre uma nova pessoa')
    print('-='*15)
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo: [M/F]')).strip().upper()
        if sexo == 'F' or sexo == 'M':
            break
    if idade >=18:
        maiores +=1
    
    if sexo[0] == 'M':
        homens +=1
    
    if sexo[0] == 'F' and idade < 20:
        mulheres_menor_20 += 1
    
    print('-'*30)
    cont = input('Continuar: [S/N] ')
    print('-'*30)
    if cont == 'N':
        break

print("""
Nº maiores de idades: {}
Nº de homens: {}
Nº de mulheres com menos de 20 : {}
""".format(maiores, homens, mulheres_menor_20))



