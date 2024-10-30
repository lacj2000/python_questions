n = int(input('Digite a quantidade de numeros de fibonacci para serem exibidos: '))

anterior = 0
atual = 1

i = 1
while i <= n:
    if n == i:
        print('{} '.format(atual))
        break
    print('{}, '.format(atual), end='')
    p_anterior = atual
    atual = anterior + atual
    anterior = p_anterior
    i += 1