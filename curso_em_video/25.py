nome = input('digite seu nome: ')

silva = 'silva' in nome.lower()

if silva:
    print("Tem 'silva' no nome.")
else:   
    print("Não tem 'silva' no nome.")