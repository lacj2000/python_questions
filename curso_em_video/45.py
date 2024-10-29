import random
import emoji

pedra = emoji.emojize(':oncoming_fist:', language='alias')
papel = emoji.emojize(':raised_hand:', language='alias')
tesoura = emoji.emojize(':victory_hand:', language='alias')


x = '1'

while x == '1':
    npc = random.randint(1,3)
    jogada = 0
    while jogada < 1 or jogada > 3:
        jogada = int(input('''Digite: 
              [1] {} pedra 
              [2] {} papel
              [3] {} tesoura
              '''.format(pedra, papel, tesoura)))
    npc_icon = tesoura
    if npc == 1:
        npc_icon = pedra
    elif npc == 2:
        npc_icon = papel

    print("npc: {}".format(npc_icon))
    if npc == jogada:
        print('empate!')
    # npc vitorias
    elif (npc == 1 and jogada == 3) or (npc == 2 and jogada == 1) or (npc == 3 and jogada == 2):
        print('Você perdeu!')
    else:
        print('Você Venceu!')
        
    x = input('''Digite: 
              [1] Jogar Jo-Ken-Po novamente...
              [0] Sair...
              ''')
    
