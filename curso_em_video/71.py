print('='*30)
print('{: ^30}'.format('Banco ABC'))
print('='*30)

saque = int(input('Valor a sacar: R$'))

n50 = saque // 50
n20 = (saque % 50) // 20
n10 = (saque % 20) // 10
n5 = (saque % 10) // 5
n1 = (saque % 5) // 1

print('''
Total de {} cédulas de R$50 
Total de {} cédulas de R$20 
Total de {} cédulas de R$10 
Total de {} cédulas de R$5 
Total de {} cédulas de R$1 

Volte Sempre! tenha um bom dia! 
      
'''.format(n50, n20, n10, n5, n1))
