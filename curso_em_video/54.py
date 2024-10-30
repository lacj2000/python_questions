import datetime

anos = []
for i in range(0, 7, 1):
    anos.append(int(input('{}º ano de nacimento: '.format(i+1))))

ano_atual = datetime.datetime.now().year

count_maiores = 0
count_menores = 0

for ano in anos:
    idade =  ano_atual - ano
    if idade >= 18:
        count_maiores += 1
    else:
        count_menores += 1
print('{} pessoas são maiores de idade e {} são menores'.format(count_maiores, count_menores))