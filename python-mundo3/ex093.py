dados = dict()
listaGols = list()
totalGols = 0
dados['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou?'))
for c in range(0, partidas):
  gols = int(input(f'Quantos gols na partida {c}? '))
  listaGols.append(gols)
  totalGols += gols
dados['gols'] = listaGols
dados['total'] = totalGols
print(10*'-=')
print(dados)
print(10*'-=')
for k, v in dados.items():
  print(f'O campo {k} tem o valor {v}.')
print(10*'-=')
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for j, g in enumerate(listaGols):
  print(f'\t=>Na partida {j}, fez {g} gols.')
print(f'Foi um total de {totalGols} gols.')
