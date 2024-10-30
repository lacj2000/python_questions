pesos = []
for i in range(0, 5, 1):
    pesos.append(float(input('{}º peso: '.format(i+1))))

maior = pesos[0]
menor = pesos[0]
for peso in pesos:
    if peso > maior:
        maior = peso
    if peso < menor:
        peso = peso


print('Maior peso: {} Menor peso: {}'.format(maior, menor))