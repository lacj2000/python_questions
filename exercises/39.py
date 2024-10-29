import datetime
ano_nascimento = int(input('Digite o seu ano de nascimento: '))

ano = datetime.datetime.now().year
idade = ano - ano_nascimento

if idade < 18:
    print('A epoca de alistamento é por volta de 18 anos, em {} anos procure a junta militar mais proxima!')
elif idade == 18:
    print('Você tem 18 anos, busque a junta militar mais próxima e faça seu alistamento! Verifique o site https://alistamento.eb.mil.br/alistamento !!!')
else: 
    print('Já passou da hora de se alistar, caso não tenha se alistado consulte a junta militar na sua região!')
    print('Você passou {} anos da epoca de se alistar'.format(idade - 18))