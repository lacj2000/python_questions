x = 0
while x >= 0:
    x = int(input('Digite um número para saber sua tabuada (sair: -1): '))
    if x > 0:
        for i in range(1, 11):
            print('{} X {}  = {}'.format(x, i, x * i))
        print('-'*20)
        