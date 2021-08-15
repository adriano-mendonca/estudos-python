from random import randint
from time import sleep
jogo = []
jogos = []
print(30*'-')
print(f'{"JOGA NA MEGA SENA":^30}')
print(30*'-')
x = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= x:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
    tot += 1
print('-='*3, f'SORTEANDO {x} JOGOS', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print(4*'-=', ' < BOA SORTE ! > ', 4*'-=')
