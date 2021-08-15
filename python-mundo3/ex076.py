print(40*'-')
print(f'{"LISTAGEM DE PREÇOS": ^40}')
print(40*'-')
list = ('Lápis', '1.75', 'Borracha', '2.00', 'Caderno', '15.90', 'Estojo', '25.00', 'Tranferidor', '4.20',
        'Compasso', '9.99', 'Mochila', '120.32', 'Canetas', '22.30', 'Livro', '34.90')
for p in range(0, len(list)):
    if p % 2 == 0:
        print(f'{list[p]:.<30}R$', end='')
    else:
        print(f'{list[p]: >8}')
print(40*'-')