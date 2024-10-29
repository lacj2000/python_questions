distancia = int(input('Qual a distancia da sua viagem em Km? '))
preco_km = 0.45
if distancia <= 200:
    preco_km = 0.5

preco = preco_km * distancia
print('A o preco da viagem de {} Km é R$ {:.2f}'.format(distancia, preco))