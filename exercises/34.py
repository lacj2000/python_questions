salario = float(input('Digite o salário: R$ '))

percentual = 1.10

if salario <= 1250:
    percentual = 1.15

salario_aumento = salario * percentual

print('O salário após aumento é R$ {:.2f}'.format(salario_aumento))