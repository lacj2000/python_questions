x = int(input())
p = [1, 3, 5, 10, 25, 50, 100]
r = None
for i in p:
    if x <= i:
        r = i
        break

print(f'Top {r}')