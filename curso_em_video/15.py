dias = int(input('Dias alugados: '))
kms = int(input('Km rodados: '))

total = kms * 0.15 + dias * 60

print('O total a pagar é R${:.2f}'.format(total))