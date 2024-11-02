#resultado = ''
while True:
    n = int(input())
    if n == 0:
        break
    t = input()
    w = False
    possibilidades = 0
    cont = 0

    for i in range(n):
        if i + 3 <= n and t[i:i+3] in ['XX.', '.XX', 'X.X']:
            w = True
            break
        
        if t[i] == '.':
            cont += 1
        if (i == cont - 1 and t[i] == 'X') or (i == n - 1 and t[i] == '.'):
            if cont % 2 != 0 or cont in [3, 4, 5]:
                possibilidades += 1 
            
            cont = 0 


        # Meio:
            #   5  : x....x : win
            # pares >= 6
            #   6  : ...... -> ..x... : lose 
            #   6  : x......x -> x..x...x : win | mas tem de ser no meio msm
            #   8  : ........ -> ...X....  -> x..X.... -> x..X...X len 8 é 
            # impares >=7
            #   7  :  ....... -> ...x... : win
            #   7  :  x.......x -> x...x...x : win

        
    if possibilidades % 2 != 0 or w:
        print('S')
#        resultado += 'S\n'
    else:
        print('N')
#        resultado += 'N\n'

#print(resultado.strip())
