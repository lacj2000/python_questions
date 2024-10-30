primeiro_termo = int(input('Primeiro termo da p.a.: '))
razao = int(input('Razão da P.A.: '))

ultimo_termo = primeiro_termo + razao * 10 +1

termos = 10
atual = primeiro_termo
while termos >= 1:

    print('{}'.format(atual), end='', flush=True)

    atual += razao
    termos -= 1

    if termos == 0:
        termos = int(input('\nGostaria de vizualizar quantos termos a mais? '))
    else:
        print(', ', end='', flush=True)
print()