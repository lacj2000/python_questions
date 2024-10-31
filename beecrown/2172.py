'''while True:
    x, m = map(int, input().split(' '))
    if (x, m) == (0,0):
        break
    print(x*m)
'''

import sys

input = sys.stdin.read
data = input().strip().splitlines()
results = []
    
for line in data:
    x, m = map(int, line.split())
    if (x, m) == (0, 0):
        break
    results.append(x * m)

print('\n'.join(map(str, results)))

