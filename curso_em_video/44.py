preco = float(input('Preço do produto: R$'))
pag = -1
while pag < 0 or pag > 4:
    pag = int(input('''
    [1] À vista (dinheiro/cheque) 10%
    [2] À vista (cartão) 5%
    [3] Em até 2x (cartão)
    [4] 3x ou Mais (cartão)
'''))
taxa = 1.20
if pag == 1:
    taxa = 0.9
elif pag == 2:
    taxa = 0.95
elif pag == 3:
    taxa = 1
elif pag == 4:
    taxa = 1.20

valor_final = preco * taxa

print('Valor final com do produto é R${}'.format(valor_final))