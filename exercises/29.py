velocidade = int(input('Digite a velocidade do Carro em Km: '))

if (velocidade > 80):
    multa = (velocidade - 80) * 7
    print('Você foi multado!'.title())
    print('A multa foi de R$ {:.2f}'.format(multa))
else:
    print('Parabéns! Continue respeitando a leis de transito!')