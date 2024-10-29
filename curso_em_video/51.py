primeiro_termo = int(input('Primeiro termo da p.a.: '))
razao = int(input('Razão da P.A.: '))

ultimo_termo = primeiro_termo + razao * 10 +1

for i in range (primeiro_termo, ultimo_termo, razao):
    if i != primeiro_termo:
        print(', ', end='', flush=True)

    print('{}'.format(i), end='', flush=True)

