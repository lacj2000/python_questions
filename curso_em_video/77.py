def check_vogais(palavra):
    vogais = ('a', 'e', 'i', 'o', 'u')
    has = []
    for v in vogais:
        has.append(v) if v in palavra else None
    return ' '.join(has)

palavras = (
    'banana',
    'maçã',
    'laranja',
    'uva',
    'manga',
    'abacaxi',
    'morango',
    'kiwi',
    'cereja',
    'pera'
)


for palavra in palavras:
    print('A palavra {} possui as seguinte vogais {}'.format(palavra, check_vogais(palavra)))