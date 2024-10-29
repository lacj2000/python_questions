soma = 0
contagem = 0
for i in range(1, 500, 1):
    if i % 2 != 0 and i % 3 == 0:
        soma += i
        contagem += 1 

print('A soma dos {} valores multiplos de 3 não pares é {}'.format(contagem, soma))