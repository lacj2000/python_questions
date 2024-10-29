numero = int(input('Digite um número: '))
base = 0

while base < 1 or base > 3:
    base = int(input("""Converta o número para base: 
    [1] binário1
    [2] octal
    [3] hexadecimal
"""))
    
if base == 1:
    print('O número {} em binário é {}'.format(numero, bin(numero)))
    pass
elif base == 2:
    print('O número {} em octal é {}'.format(numero, oct(numero)))
    pass
elif base == 3:
    print('O número {} em hexadecimal é {}'.format(numero, hex(numero)))
    pass
else:
    print('Base inválida')