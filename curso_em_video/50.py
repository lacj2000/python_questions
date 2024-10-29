numeros = []

for _ in range(0,6):
    numeros.append(int(input('Digite um número inteiros: ')))

soma = 0
for numero in numeros:
    if numero % 2 == 0:
        soma += numero

print('Soma dos números pares é {}'.format(soma))