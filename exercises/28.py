from random import randint

numero_pensado = randint(1,5)

numero = int(input('Descubra que número entre 0 e 5 estou pensando: '))

if (numero == numero_pensado):
    print("Parabéns Você Venceu!")
elif(numero + 1 == numero_pensado or numero - 1 == numero_pensado): 
    print("Passou perto, melhor sorte na próxima!")
else:
    print("Melhor sorte na próxima!")

print('O número pensado foi {} e você escolheu {}'.format(numero_pensado, numero))
