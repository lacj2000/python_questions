numeros = (
    int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: ')),
)

print('O 9 apareceu {} vezes'.format(numeros.count(9)))
if 3 in numeros:
    print('O 3 apareceu primeiro na {}ª posição'.format(numeros.index(3)+1))
else:
    print('O 3 não aparece')
print('pares: {}'.format(' '.join(str(num) for num in numeros if num %2 == 0 )))