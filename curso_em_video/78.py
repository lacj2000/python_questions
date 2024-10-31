numeros = []

for _ in range(0,5):
    numeros.append(int(input('{}º numero: '.format(_+1))))

maior = max(numeros)
menor = min(numeros)


print('Maior: {} | pos.: {}'.format(maior, numeros.index(maior)+1))
print('Menor: {} | pos.: {}'.format(menor,  numeros.index(menor)+1))