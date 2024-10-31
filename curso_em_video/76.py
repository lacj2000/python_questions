produtos = (
    'Maçã', 3.50,
    'Banana', 1.20,
    'Laranja', 2.00,
    'Pão', 0.90,
    'Leite', 4.50,
    'Queijo', 12.00,
    'Arroz', 5.00,
    'Feijão', 6.00,
    'Café', 10.00,
    'Açúcar', 2.50,
)
print('='*33)
print('{: ^33}'.format('Listagem de produtos'))
print('='*33)
for i in range(0, len(produtos), 2):
    print('{: ^16}|{: ^16}'.format(produtos[i],'R$ {:.2F}'.format(produtos[i+1])))
    print('-'*33)
