import datetime
ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))

ano = datetime.datetime.now().year
idade = ano - ano_nascimento
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 20:
    print('Sênior')
else:
    print('Master')