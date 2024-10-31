sum = 0

for i in range(0, int(input())):
    a, b = map(int,input().split(' '))
    sum += (a % 1000 + 0.5) * b

print(f'{sum:.2f}')
