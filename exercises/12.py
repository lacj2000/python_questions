price = float(input('Digite o preço do produto: '))

print('Preço: R${:.2f} Preço com desconto: R${:.2f} Desconto: R${:.2f}'.format(price, price * 0.95, price * 0.05))