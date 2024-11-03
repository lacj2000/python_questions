hi, mi, hf, mf = map(int,input().split())


i = hi*60 + mi
f = hf*60 + mf
if f <= i:
    f += 24*60
d  = f - i

h = d // 60
m = d % 60

print(f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)')