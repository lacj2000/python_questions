primeiro_termo = int(input('Primeiro termo da p.a.: '))
razao = int(input('Razão da P.A.: '))

ultimo_termo = primeiro_termo + razao * 10 +1

termos = 1
atual = primeiro_termo
while termos <= 10:
    if atual != primeiro_termo:
        print(', ', end='', flush=True)

    print('{}'.format(atual), end='', flush=True)

    atual += razao
    termos += 1
print()