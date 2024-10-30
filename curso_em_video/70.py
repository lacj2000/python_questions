total = 0
n_caros = 0
mais_barato = ''
mais_barato_preco = None

while True:
    nome = input('Nome produto: ')
    preco = float(input('Preço: '))

    if total == 0:
        mais_barato = nome
        mais_barato_preco = preco

    elif mais_barato_preco > preco: 
        mais_barato = nome
        mais_barato_preco = preco
    if preco > 1000:
        n_caros += 1

    total += preco
    
    dec = input("Adicionar Produto: [encerrar: N]").strip().upper()
    if dec == 'N':
        break


print('A soma total é: {:.2f}'.format(total))
print('Numero de produtos acima de R$ 1000: {}'.format(n_caros))
print('O produto mais barato é: {}'.format(mais_barato))