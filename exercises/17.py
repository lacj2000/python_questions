from math import pow, sqrt

cateto_oposto = float(input('Digite o tamanho do cateto oposto: '))
cateto_adjacente = float(input('Digite o tamanho do cateto adjacente: '))

quadrado_oposto = pow(cateto_oposto,2)
quadrado_adj = pow(cateto_adjacente, 2)
suma_quadrado = quadrado_oposto + quadrado_adj
hipotenusa = sqrt(suma_quadrado)

print('hipotenusa: {}'.format(hipotenusa))
