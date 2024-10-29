a = int(input('Digite o 1º numero: '))
b = int(input('Digite o 2º numero: '))
c = int(input('Digite o 3º numero: '))
maior = c
menor = c

if a > b and  a > c:
    maior = a
elif b > a and  b > c:
    maior = b

if a < b and  a < c:
    menor = a
elif b < a and  b < c:
    menor = b



print('Maior: {} '.format(maior))
print('Menor: {} '.format(menor))