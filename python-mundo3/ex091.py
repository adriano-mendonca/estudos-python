from random import randint
from time import sleep
from operator import itemgetter
jogada = {'jogador1': randint(1, 6),
          'jogador2': randint(1, 6),
          'jogador3': randint(1, 6),
          'jogador4': randint(1, 6)}
print('Valores sorteados: ')
rank = list()
for j1, j2 in jogada.items(): #j1 = jogadores // j2 = jogada
    print(f'{j1} tirou {j2} no dado.')
    sleep(1)
print(30*'-=')
rank = sorted(jogada.items(), key=itemgetter(1), reverse=True)
print(f'{"== RANKING DOS JOGADORES ==":^30}')
for i, v in enumerate(rank):
    print(f'    {i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)