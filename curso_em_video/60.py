numero = int(input('Número:'))

i = numero
fatorial_w = numero
while i != 1:
    i = i - 1
    fatorial_w *= i
print('Fatorial com while é {}'.format(fatorial_w))

fatorial = 1
for i in range(numero, 1, -1):
    fatorial *= i
print('Fatorial com for é {}'.format(fatorial))