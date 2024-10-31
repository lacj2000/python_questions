brasileirao_2024 = (
    'Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Internacional',
    'São Paulo', 'Bahia', 'Cruzeiro', 'Vasco da Gama', 'Atlético-MG',
    'Grêmio', 'Criciúma', 'Fluminense', 'EC Vitória', 'Corinthians',
    'Athletico-PR', 'Bragantino', 'Juventude', 'Cuiabá', 'Atlético-GO'
)

brasileirao_alfa = sorted(brasileirao_2024)

print('='*30)
print('{: ^30}'.format('Brasileirão 2024'))
print('='*30)

print('{: ^30}'.format('G4 - Libertadores 2025\n'))
for i in range(0,4):
    print('\033[;32m{}º - {}\033[m'.format(i+1, brasileirao_2024[i]))
print('-'*30)

print('{: ^30}'.format('Z4 - Rebaixados\n'))
for i in range(15,20):
    print('\033[;31m{}º - {}\033[m'.format(i+1, brasileirao_2024[i]))
print('-'*30)

print('{: ^30}'.format('Times\n'))
for i in range(0,20):
    print('{}'.format(brasileirao_alfa[i]))
print('-'*30)

print('O Flamengo está em {}ª posição'.format(brasileirao_2024.index('Flamengo')+1))
