casa = float(input('Preço da Casa: '))
salario = float(input('Salario Mensal: '))
anos = int(input('Pagar em quantos anos: '))

numero_prestacoes = anos * 12
prestacao_mensal = casa / numero_prestacoes
percetual_renda = prestacao_mensal / salario * 100

if percetual_renda <= 30:
    print('Parcelamento aprovado')
    print('O valor da prestação mensal é R${:.2f}'.format(prestacao_mensal))
    print('Serão {} parcelas comprometendo {:.2f}%'.format(numero_prestacoes))
else:
    print('Parcelamento Negado')
    print('O valor da prestação mensal seria de R${:.2f}'.format(prestacao_mensal))
    print('Seriam {} parcelas comprometendo {:.2f} \% da renda mensal'.format(numero_prestacoes, percetual_renda))