a = float(input('Digite o 1º lado: '))
b = float(input('Digite o 2º lado: '))
c = float(input('Digite o 3º lado: '))


if a < b + c and  b < a + c and c < a + b:
    tipo = 'escaleno'
    if a == b and b == c:
        tipo = 'equilátero'
    elif a == b or b == c:
        tipo = 'isósceles'
        
    print('Os segmentos de retas FORMAM um triângulo {}!'.format(tipo))


    
else:
    print('Os segmentos de retas NÂO FORMAM um triângulo!')