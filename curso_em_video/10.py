money = float(input('Digite o total de dinheiro: R$ '))
unit_dolar = float(input('Digite o preço do dólar: $ '))

print('Com R$ {:.2f} reais é possivel comprar $ {:.2f} dólares.'.format(money, money/unit_dolar))