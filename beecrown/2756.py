i = 1
for e in range(7,2,-1):
    print(' '*e+chr(72-e), end='')
    if e < 7:
        print(' '*i+chr(72-e), end='')
        if e > 3:
            i+=2
    print()
for e in range(4, 8):
    print(' '*e+chr(72-e), end='')
    if e < 7:
        i-=2
        print(' '*i+chr(72-e), end='')
    print()