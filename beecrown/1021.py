n = float(input(''))
n = int(n * 100) 

n100 = n // 10000
resto = n % 10000
n50 = resto // 5000
resto = resto % 5000
n20 = resto // 2000
resto = resto % 2000
n10 = resto // 1000
resto = resto % 1000
n5 = resto // 500
resto = resto % 500
n2 = resto // 200
resto = resto % 200

m1 = resto // 100
resto = resto % 100
m50 = resto // 50
resto = resto % 50
m25 = resto // 25
resto = resto % 25
m10 = resto // 10
resto = resto % 10
m05 = resto // 5
resto = resto % 5
m01 = resto // 1

print(f'''NOTAS:
{n100} nota(s) de R$ 100.00
{n50} nota(s) de R$ 50.00
{n20} nota(s) de R$ 20.00
{n10} nota(s) de R$ 10.00
{n5} nota(s) de R$ 5.00
{n2} nota(s) de R$ 2.00
MOEDAS:
{m1} moeda(s) de R$ 1.00
{m50} moeda(s) de R$ 0.50
{m25} moeda(s) de R$ 0.25
{m10} moeda(s) de R$ 0.10
{m05} moeda(s) de R$ 0.05
{m01} moeda(s) de R$ 0.01''')
