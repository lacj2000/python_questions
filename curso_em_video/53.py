frase = input('Digite algo: ')

frase_cleaned = frase.lower().replace(' ', '')
frase_reversa = frase_cleaned[::-1]

eh_palidromo = False
for i in range(0,len(frase_cleaned)):
    if frase_cleaned[i] == frase_reversa[i]:
        eh_palidromo = True
    else:
        eh_palidromo = False
        break

if eh_palidromo:
    print('A frase \'{}\' é um palidromo '.format(frase))
else: 
    print('A frase \'{}\' não é um palidromo'.format(frase))
