soma = 0
contador = 0
menor = 0
maior = 0

while True:
    numero = int(input('Digite um número: '))
    contador += 1 
    soma += numero 
    if contador == 1:
        menor = numero
        maior = numero
    
    if numero < menor:
        menor = numero

    if numero > maior:
        maior = numero

    x = input('Digite 999 pra sair!')
    if x == '999':
        break

media = soma/contador

print('Media: {}'.format(media))
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))