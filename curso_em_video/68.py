from random import randint

winner = True
counter = 0

while winner == True:
    computer = randint(1,5) 
    player = int(input('Impar ou par? Digite um numero: '))

    sum = computer + player

    if computer % 2 == player % 2:
        counter += 1
        print('A soma é {}, você venceu! essa é a {}ª vitória'.format(sum, counter)) 
    else:
        if counter > 0:
            print('A soma é {}, você perdeu! A sequencia era de {} vitória(s)'.format(sum, counter)) 
        else:
            print('A soma é {}, você perdeu! Não ganhou nenhuma!'.format(sum, counter)) 
        break
