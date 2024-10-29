city = input('Cidade: ')

word = city.lower().split(' ')[0]

if (word == 'santo'):
    print('Inicia com \'santo\'')
else:
    print('Não inicia com \'santo\'')
