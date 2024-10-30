from random import randint

numero_pensado = randint(1,10)
tentativas = 0
while True:
    numero = int(input('Descubra que número entre 0 e 10 estou pensando: '))
    tentativas += 1
    if (numero == numero_pensado):
        print("Parabéns Você acertou!")
        break
    else:
        print("Melhor sorte na próxima tentativa!")

print('O número pensado foi {} e você escolheu {}'.format(numero_pensado, numero))
print('Foram nescessárias {} tentativas'.format(tentativas))