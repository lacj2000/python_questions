number = int(input('Digite um numero: '))

print('Taboada de {:-^10}'.format(number))
for i in range(1,11):
    print('{} X {} = {:.1f}'.format(number, i, i*number))