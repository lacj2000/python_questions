numeros = []

while True:
    numeros.append(float(input('Digite mais um numero: ')))
    
    x = input('Digite 999 pra sair!')
    if x == '999':
        break

print('Itens únicos: {}'.format(sorted(set(numeros))))
