p, c, p2, c2 = map(int, input().split(' '))
if p * c == p2 * c2:
    print(0)
elif p * c > p2 * c2:
    print(-1)
else:
    print(1)