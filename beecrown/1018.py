n = int(input(''))

n100 = n // 100
resto = n % 100
n50 = resto // 50
resto = resto % 50 
n20 = resto // 20
resto = resto % 20 
n10 = resto // 10
resto = resto % 10 
n5 = resto // 5
resto = resto % 5 
n2 = resto // 2
resto = resto % 2 
n1 = resto // 1

print('''{}
{} nota(s) de R$ 100,00
{} nota(s) de R$ 50,00
{} nota(s) de R$ 20,00
{} nota(s) de R$ 10,00
{} nota(s) de R$ 5,00
{} nota(s) de R$ 2,00
{} nota(s) de R$ 1,00'''.format(n, n100, n50, n20, n10, n5, n2, n1))
