def ficha(n='', g=0):
    if n == '':
        n = '<desconhecido>'
    print(f'O jogador {n} fez {g} gols no campeonato.')


nome = str(input('Nome do jogador: '))
gols = input('Número de Gols: ')
if len(gols) == 0:
    gols = 0
ficha(nome, gols)
