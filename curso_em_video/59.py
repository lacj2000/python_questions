def get_numbers():
    n1 = float(input('1ª entrada:'))
    n2 = float(input('2ª entrada:'))
    return [n1, n2]

def is_equals(n1, n2):
    return n1 == n2

def get_maior(n1, n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return None
    
action = 4

menu = """
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Exibir Números
[0] Sair
"""

n1 = 0
n2 = 0

while action != 0:
    try: 
        if action == 1:
            print('Soma: {}'.format(n1+n2))
        elif action == 2:
            print('Produto: {}'.format(n1*n2))
        elif action == 3:
            if is_equals(n1, n2):
                print('São Iguais!!!')
            else: 
                print('O maior é {}'.format(get_maior(n1,n2)))
        elif action == 4:
            n1, n2 = get_numbers()
        elif action == 5:
            print('Número 1: {} Número 2:{}'.format(n1, n2))
        else:
            print('Ação inválida!')
        action = int(input(menu))
    except ValueError: 
        print('Digite um valor válido...')
    except KeyboardInterrupt:
        print('Chau Chau')
        break