numeros_por_extenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 
    'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 
    'dezoito', 'dezenove', 'vinte'
)
numero = -1
while numero < 0 or numero >20:
    numero = int(input('Digite um número entre 1 e 20: '))
    if numero < 0 or numero >20:
        print('Digite um número valido!!!')


print('O número {} por extenso é \'{}\''.format(numero, numeros_por_extenso[numero]))
