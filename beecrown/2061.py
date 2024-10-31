a, r = map(int, input().split(' '))
for i in range(0, r):
    if (input() == 'fechou'):
        a += 1
    else:
        a -= 1
print(a)