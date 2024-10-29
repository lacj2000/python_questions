
numero =  int(input('Digite um número: '))

primo = True
raiz = (numero) ** (1/2)
divisor = -1

print(raiz)

if numero % 2 == 0 and numero != 2:
    primo = False
    divisor = 2
i = 3
while i <= raiz + 1 and primo:
    if numero % i == 0: 
        primo = False
        divisor = i
        break
    i += 2

if primo == False:
    print('O número {} é divisível por {}'.format(numero, divisor))
else:
    print('O número {} é primo'.format(numero))