soma = 0
quantidade = 0
atual = 0

while atual != 999:
    try: 
        atual = int(input('Digite um número (sair - 999): '))
        if(atual != 999):
            soma += atual
            quantidade += 1
    except ValueError: 
        print('Digite um valor válido...')
    
    except KeyboardInterrupt:
        print('Finalizando')
        break

print('{} número(s) foram digitados e sua soma é {}'.format(quantidade, soma))