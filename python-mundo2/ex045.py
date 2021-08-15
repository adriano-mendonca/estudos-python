from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print('''Suas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')
play = int(input('Qual é a sua jogada? '))
pc = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print(10*'-=')
print(f'PC: {itens[pc]}')
print(f'PLAYER: {itens[play]}')
print(10*'-=')

if pc == 0: #Computador joga pedra
    if play == 0:
        print('EMPATE!')
    elif play == 1:
        print('Player é o vencedor!')
    else:
        print('Computador é o vencedor!')
elif pc == 1: #Computador joga papel
    if play == 0:
        print('Computador é o vencedor!')
    elif play == 1:
        print('EMPATE!')
    elif play == 2:
        print('Jogador é o vencedor!')
elif pc == 2: #Computador joga tesoura
    if play == 0:
        print('Jogador é o vencedor!')
    elif play == 1:
        print('Computador é o vencedor!')
    elif play == 2:
        print('EMPATE!')
else:
    print('Jogada inválida!')