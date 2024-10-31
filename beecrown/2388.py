x = int(input())
sum = 0
for i in range(0, x):
    t = input().split(' ')
    sum += int(t[0]) * int(t[1]) 
print(sum)