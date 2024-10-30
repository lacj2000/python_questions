
soma = 0
contador = 0


while True:
    numero = int(input('Digite um número: '))
    contador += 1 
    soma += numero 
    x = input('Digite 999 pra sair!')
    if x == '999':
        break

print('Soma: {}'.format(soma))
print('Quantidade: {}'.format(contador))
