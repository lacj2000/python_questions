from math import factorial
from collections import Counter

cache = {}

MOD = 100000007

def f_c(n):
    if n in cache:
        return cache[n]
    
    f =  factorial(n)
    cache[n] = f
    return f

while True:
    p = input()
    if p == '0':
        break
    n = len(p)
    f = f_c(n)
    r = Counter(p)
    rf = 1
    for l in r.values():
        rf  *= f_c(l)
    rep = f//rf
    rep %= MOD
    print(f'{rep}', flush=True)