e, s = map(int, input().split())
menor = s
for i in range(0, e):
    s += int(input())
    if menor > s:
        menor = s
print(menor) 