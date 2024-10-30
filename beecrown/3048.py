n = int(input())
count = 0
anterior = None
for i in range(0,n):
    f = int(input())
    if f != anterior:
        print('-',end='')    
        count += 1
    print(f)    
    anterior = f

print(count)