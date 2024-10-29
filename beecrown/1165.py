testes =  int(input(''))

numeros = []
for i in range(testes): 
    numeros.append(int(input('')))

for numero in numeros:
    primo = True
    raiz = (numero) ** (1/2)

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
        print('{} nao eh primo'.format(numero), flush=True)
    else:
        print('{} eh primo'.format(numero), flush=True)