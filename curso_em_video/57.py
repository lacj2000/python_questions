
while True:
    sexo = str(input('Sexo: [M/F]')).strip()
    if sexo in ['M', 'F']:
        break
    else:
        print('Valor incorreto, digite novamente!')