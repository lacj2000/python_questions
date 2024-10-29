peso = float(input('Peso: '))
altura = float(input('Altura em metro: '))

imc = peso / altura ** 2
resultado = 'Obesidade morbida'
if imc < 18.5:
    resultado = 'abaixo do peso'
elif imc < 25:
    resultado = 'peso ideal'
elif imc < 30:
    resultado = 'sobrepeso'
elif imc < 40:
    resultado = 'obesidade'

print('IMC {}: {}'.format(imc, resultado))